from collections import defaultdict
import numpy as np
import pandas as pd
import utils.utils as utils
import os
from .base_evaluator import BaseEvaluator
from multiprocessing import Pool
import json
import re

class FDEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        self.answer_key = "Functional-Dependency"
        self.default_result = {"precision": None, "recall": None}
    
    def preprocess(self, y):
        y_processed = set()
        if y == "JSONParsingError" or y is None:
            return set()
        
        if type(y) == list:
            for item in y:
                if type(item) == list and len(item) == 2:
                    try:
                        y_processed.add(tuple(item))
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
        
        return y_processed
    
    def _evaluate_one(self, y_true, y_pred):
        y_true_set = set([tuple(x) for x in y_true])
        try:
            y_pred_set = self.preprocess(y_pred)
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
            "recall" : len(tp_set) / len(y_true_set)
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