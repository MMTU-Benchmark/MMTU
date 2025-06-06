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

class AREvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        self.answer_key = "Arithmetic-Relationship"
        self.default_result = {"precision": None, "recall": None, "y_pred_eval": []}
    
    def preprocess(self, y, labeled_formulas):
        if y == "JSONParsingError" or y is None:
            y = []
        elif type(y) == str:
            y = [y]
        elif type(y) == list:
            y = [str(x) for x in y]
        else:
            # print("Unknown type", type(y))
            # print(y)
            # raise Exception("Unknown type")
            y = []
        assert type(y) == list
        y = [re.sub(r"\s+", "", x) for x in y]
        y = [x for x in y if x in labeled_formulas]
        return set(y)
    
    def _evaluate_one(self, y_true, y_pred, labeled_formulas):
        y_true_set = set(y_true)
        y_pred_set = self.preprocess(y_pred, labeled_formulas)

        if len(y_true_set) == 0:
            return {
                "recall" : None,
                "precision" : None if len(y_pred_set) == 0 else 0,
                "y_pred_eval" : list(y_pred_set)
            }
        
        if len(y_pred_set) == 0:
            return {
                "recall" : 0,
                "precision" : None,
                "y_pred_eval" : list(y_pred_set)
            }

        tp_set = y_true_set.intersection(y_pred_set)
        
        res = {
            "precision" : len(tp_set) / len(y_pred_set) if len(y_pred_set) > 0 else 0,
            "recall" : len(tp_set) / len(y_true_set),
            "y_pred_eval" : list(y_pred_set)
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
                row_eval = self._evaluate_one(row_res["y_gt"], row_res["y_pred"], row_res["labeled_formulas"])
            except:
                row_eval = self.default_result
            for k, v in row_eval.items():
                row_res[k] = v
                
            result.append(row_res)
        result = pd.DataFrame(result)
        return result