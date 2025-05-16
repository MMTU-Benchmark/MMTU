from .base_evaluator import BaseEvaluator

import os
import json
import re
import ast
import pandas as pd

class DataTransformReshapeEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        
    def _get_gt(self, metadata):
        # return the GT answer
        return {"label": metadata["label"], "alternative_label": metadata["alternative_label"]}
        
    def extract_json_answer(self, text, answer_key):
        pattern = r'{[^}]*}'  # Regex pattern to match strings inside curly braces while keeping the braces
        matches = re.findall(pattern, text)
        for match in matches:
            try:
                result = json.loads(match)
                return result
            except:
                try:
                    result = ast.literal_eval(match)
                    return result
                except:
                    continue
                continue
        return "JSONParsingError"
        
    def _evaluate_one(self, y_true, y_pred):
        if y_pred == "JSONParsingError":
            return {"correct": 0}
        correct = 0
        y_true_label = y_true["label"]
        y_true_alternative_label = y_true["alternative_label"]
        
        if type(y_true_label) == dict:
            y_true_label = [y_true_label]
        try:
            assert type(y_true_label) == list, f"y_true_label and y_true_alternative_label should be list, but got {type(y_true_label)} and {type(y_true_alternative_label)}"
        except:
            return {"correct": 0}
        if type(y_pred) == dict:
            y_pred = [y_pred]
        
        y_pred_eval = []
        for op in y_pred:
            assert type(op) == dict, f"op: {op}, y_pred: {y_pred}"
            if "transformation" in op:
                op["operator"] = op.pop("transformation")
            y_pred_eval.append(op)
        
        if len(y_pred_eval) == len(y_true_label):
            FLAG = True
            for op_pred, op_gt in zip(y_pred_eval, y_true_label):
                if op_pred != op_gt:
                    FLAG = False
                    break
            if FLAG:
                correct = 1
        
        if y_true_alternative_label:
            if type(y_true_alternative_label) == dict:
                y_true_alternative_label = [y_true_alternative_label]
            assert type(y_true_alternative_label) == list, f"y_true_label and y_true_alternative_label should be list, but got {type(y_true_label)} and {type(y_true_alternative_label)}"
        
            if len(y_pred_eval) == len(y_true_alternative_label):
                FLAG = True
                for op_pred, op_gt in zip(y_pred_eval, y_true_alternative_label):
                    if op_pred != op_gt:
                        FLAG = False
                        break
                if FLAG:
                    correct = 1 
        
        res = {
            "correct": correct,
        }
        return res
    
    def _compute_metric(self, res):
        acc = res["correct"].values.mean()
        metric = {
            "acc": acc,
        }
        return metric