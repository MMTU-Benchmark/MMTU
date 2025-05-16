from collections import defaultdict
import numpy as np
import pandas as pd
import utils.utils as utils
import os
from .base_evaluator import BaseEvaluator
from multiprocessing import Pool
import json
import re
from tqdm import tqdm
import ast

class EquiJoinDetectEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        self.answer_key = "joins"
        self.default_result = {"precision": None, "recall": None}
        
    def extract_json_answer(self, text, answer_key):
        assert answer_key is not None
        if text.startswith("<think>"):
            match = re.match(r"<think>(.*?)</think>(.*)", text, re.DOTALL)
            text = match.group(2) if match else text
            
        def extract_last_json(text):
            end = text.rfind('}')
            if end == -1:
                return None  # No closing brace found

            stack = []
            for i in range(end, -1, -1):  # Walk backwards from last '}'
                if text[i] == '}':
                    stack.append('}')
                elif text[i] == '{':
                    stack.pop()
                    if not stack:
                        json_str = text[i:end+1]
                        return json_str
            return "JSONParsingError"  # No matching opening brace found
        
        match = extract_last_json(text)

        if match:
            try:
                result = json.loads(match)
                if answer_key in result:
                    return result[answer_key]
            except:
                try:
                    result = ast.literal_eval(match)
                    if answer_key in result:
                        return result[answer_key]
                except:
                    pass
        return "JSONParsingError"
    
    def _evaluate_one(self, y_true, y_pred):
        def preprocess(y_pred):
            rsts = []
            if y_pred == "JSONParsingError":
                return set()
            assert isinstance(y_pred, list), f"y_pred should be a list, got {type(y_pred)}\n {y_pred}"
            for item in y_pred:
                assert isinstance(item, dict), "item should be a dict"
                rst = (item.get("from_table"), item.get("from_column"), item.get("to_table"), item.get("to_column"))
                rsts.append(rst)
            return set(rsts)
        
        y_true_set = set([tuple(x) for x in y_true])
        try:
            y_pred_set = preprocess(y_pred)
        except Exception as e:
            y_pred_set = set()

        if len(y_true_set) == 0:
            return {
                "recall" : None,
                "precision" : None if len(y_pred_set) == 0 else 0,
            }
        
        if len(y_pred_set) == 0:
            return {
                "recall" : 0,
                "precision" : None,
            }

        tp_set = y_true_set.intersection(y_pred_set)
        
        res = {
            "precision" : len(tp_set) / len(y_pred_set) if len(y_pred_set) > 0 else 0,
            "recall" : len(tp_set) / len(y_true_set),
        }
        return res
    
    def _compute_metric(self, res):        
        prec = res["precision"].dropna().mean()
        recall = res["recall"].dropna().mean()
        if not prec == 0 or not recall == 0:
            f1 = 2 * prec * recall / (prec + recall)
        else:
            f1 = 0
        metric = {
            "prec": prec,
            "recall": recall,
            "f1": f1
        }
        return metric

    def parse_raw_result(self, raw_result, n_jobs=1):
        # return a DataFrame of parsed results
        result = []
        for _, row in tqdm(raw_result.iterrows(), total=len(raw_result), ncols=80, desc="Parsing results"):
            row_res = json.loads(row.metadata)
            row_res["metadata"] = row.metadata
            row_res["prompt"] = row.prompt
            if "choices" in row:
                row_res["prompt"] = row.prompt
                row_res["completion"] = row.choices[0]["text"]
            elif "response" in row:
                row_res["completion"] = row.response
            else:
                raise Exception("Unknown format")
            if row_res["completion"] is None:
                row_res["completion"] = ""
            row_res["prompt_tokens"] = row.prompt_tokens if "prompt_tokens" in row else None
            row_res["completion_tokens"] = row.completion_tokens if "completion_tokens" in row else None
            row_res["model_name"] = row.model_name if "model_name" in row else None
            row_res["time_taken"] = row.time_taken if "time_taken" in row else None
            # row_res["label"] = self._get_gt(row_res)
            row_res["prompt_completion"] = row_res["prompt"] + "\n" + row_res["completion"]
            row_res["y_pred"] = self._get_pred(row_res["completion"])
            row_res["y_gt"] = self._get_gt(row_res)
            
            # evaluate each row
            try:
                row_eval = self._evaluate_one(row_res["y_gt"], row_res["y_pred"])
            except Exception as e:
                row_eval = self.default_result
            for k, v in row_eval.items():
                row_res[k] = v
                
            result.append(row_res)
        result = pd.DataFrame(result)
        return result