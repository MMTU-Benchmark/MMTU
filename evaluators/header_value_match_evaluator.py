from .base_evaluator import BaseEvaluator

import os
import json
import re
import ast
import pandas as pd

class HeaderValueMatchEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        self.answer_key = "column_headers"
        self.gt_key = "label"
        
    def _evaluate_one(self, y_true, y_pred):
        correct = 0
        try:
            assert isinstance(y_true, list), "y_true should be a list"
            assert isinstance(y_pred, list), f"y_pred should be a list: {y_pred}"
            
            y_true = [x.strip() for x in y_true]
            y_pred = [x.strip() for x in y_pred]
            
            # ## hard code for permutation
            # df_dummy = pd.DataFrame(columns=y_true)
            #         # Keep first 3 columns
            # first_cols = df_dummy.iloc[:, :3]

            # # Shuffle the rest
            # remaining_cols = df_dummy.iloc[:, 3:]
            # shuffled_cols = remaining_cols.sample(frac=1, axis=1, random_state=42)
            # df_dummy = pd.concat([first_cols, shuffled_cols], axis=1)
            
            # y_true = list(df_dummy.columns)
            
            if len(y_true) == len(y_pred):
                correct = sum([1 if y_true[i] == y_pred[i] else 0 for i in range(len(y_true))]) / len(y_true)
            
        except Exception as e:
            pass
        
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