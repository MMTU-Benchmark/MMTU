from .base_evaluator import BaseEvaluator

import os
import json
import re
import ast
import pandas as pd

class FormulaPredictContextEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        self.answer_key = "formula"
        self.gt_key = "formula"
        
    def _evaluate_one(self, y_true, y_pred):
        correct = 0
        y_true = y_true.replace("$", "").strip()
        y_pred = y_pred.replace("$", "").strip()
        if y_true == y_pred:
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