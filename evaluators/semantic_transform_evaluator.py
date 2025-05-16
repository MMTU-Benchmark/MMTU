from .base_evaluator import BaseEvaluator

import os
import json
import re
import ast
import pandas as pd
import random

class SemanticTransformEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        self.answer_key = "output"
        self.gt_key = "label"
        
    def _evaluate_one(self, y_true, y_pred):
        correct = 0

        # Hard code for row permutation
        # y_true = pd.DataFrame({"y_true": y_true}).sample(frac=1, random_state=42)["y_true"].values.tolist()
        try:
            if len(y_true) == len(y_pred):
                correct = sum([1 if y_true[i] == y_pred[i] else 0 for i in range(len(y_true))]) / len(y_true)
        except Exception as e:
            print(f"Error comparing y_true and y_pred: {e}")
            correct = 0
        
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