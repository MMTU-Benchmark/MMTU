from .base_evaluator import BaseEvaluator

import os
import json
import re
import ast
import pandas as pd

class SemanticJoinEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        self.answer_key = "output"
        self.gt_key = "label"
        
    def _evaluate_one(self, y_true, y_pred):
        correct = 0
        try:
            assert isinstance(y_true, list), "y_true should be a list"
            assert isinstance(y_pred, list), f"y_pred should be a list: {y_pred}"
            
            df_true = pd.DataFrame(y_true)
            df_pred = pd.DataFrame(y_pred)
            
            assert len(df_true.columns) == 2, "y_true should have 2 columns"
            assert len(df_pred.columns) == 2, "y_pred should have 2 columns"
            
            df_true.columns = ["col1", "col2"]
            df_pred.columns = ["col1", "col2"]
            
            df_true.sort_values(by=["col1", "col2"], inplace=True)
            df_pred.sort_values(by=["col1", "col2"], inplace=True)
            df_true.drop_duplicates(subset=["col1", "col2"], inplace=True)
            df_pred.drop_duplicates(subset=["col1", "col2"], inplace=True)
            df_true.reset_index(drop=True, inplace=True)
            df_pred.reset_index(drop=True, inplace=True)

            # Assuming df1 and df2 are your two DataFrames
            common_rows = pd.merge(df_true, df_true, how='inner', on=["col1", "col2"])
            num_common_rows = len(common_rows)
            correct = num_common_rows / len(df_true)
            assert correct >= 0, "correct should be greater than or equal to 0"
            assert correct <= 1, f"correct should be less than or equal to 1, len(df_true): {len(df_true)}, len(df_pred): {len(df_pred)}, num_common_rows: {num_common_rows}"
            # if df_true.equals(df_pred):
            #     correct = 1
            if correct < 0 or correct > 1:
                print(f"Error: correct value out of bounds: {correct}, len(df_true): {len(df_true)}, len(df_pred): {len(df_pred)}")
                exit(1)
            
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