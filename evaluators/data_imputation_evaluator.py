from .base_evaluator import BaseEvaluator

import os
import json
import re
import ast
import pandas as pd

class DataImputationEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        self.answer_key = "value"
        
    def _evaluate_one(self, y_true, y_pred):
        correct = 0
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