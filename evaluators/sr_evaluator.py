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

class SREvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        self.answer_key = "String-Relationship"
        self.default_result = {"precision": None, "recall": None}
    
    def preprocess(self, y, labeled_data):
        y_processed = []
        if y == "JSONParsingError" or y is None:
            return set()
        
        if type(y) == list:
            for item in y:
                if type(item) == list and len(item) == 2:
                    try:
                        y_processed.append(tuple([tuple(item[0]), item[1]]))
                    except Exception as e:
                        print("Error in tuple conversion", item)
                        print(e)
                        raise e
                else:
                    print("Unknown format", item)
                    print(y)
                    raise Exception("Unknown format")
        else:
            print("Unknown type", type(y))
            print(y)
            raise Exception("Unknown type")
        # y_processed = [x for x in y_processed if list([x[0], x[1]]) in labeled_data]
        return set(y_processed)
    
    def _evaluate_one(self, y_true, y_pred, labeled_data):
        y_true_set = set([(tuple(x[0]), x[1]) for x in y_true])
        try:
            y_pred_set = self.preprocess(y_pred, labeled_data)
        except Exception as e:
            y_pred_set = set()

        if len(y_true_set) == 0:
            return {
                "recall" : None,
                "precision" : None if len(y_pred_set) == 0 else 0,
                "y_pred_eval": y_pred_set
            }
        
        if len(y_pred_set) == 0:
            return {
                "recall" : 0,
                "precision" : None,
                "y_pred_eval": y_pred_set
            }

        tp_set = y_true_set.intersection(y_pred_set)
        
        res = {
            "precision" : len(tp_set) / len(y_pred_set) if len(y_pred_set) > 0 else 0,
            "recall" : len(tp_set) / len(y_true_set),
            "y_pred_eval": y_pred_set
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
                row_eval = self._evaluate_one(row_res["y_gt"], row_res["y_pred"], row_res["labeled_data"])
            except:
                row_eval = self.default_result
            for k, v in row_eval.items():
                row_res[k] = v
                
            result.append(row_res)
        result = pd.DataFrame(result)
        return result