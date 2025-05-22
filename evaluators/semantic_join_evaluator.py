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
        precision = None
        recall = None
        # f1 = None
        
        try:
            assert isinstance(y_true, list), "y_true should be a list"
            assert isinstance(y_pred, list), f"y_pred should be a list: {y_pred}"
            
            df_true = pd.DataFrame(y_true)
            df_pred = pd.DataFrame(y_pred)
            
            assert len(df_true.columns) == 2, "y_true should have 2 columns"
            assert len(df_pred.columns) == 2, "y_pred should have 2 columns"
            
            df_true.columns = ["col1", "col2"]
            df_pred.columns = ["col1", "col2"]
            
            df_pred = df_pred.astype({"col1": str, "col2": str})
            df_true = df_true.astype({"col1": str, "col2": str})
            
            df_true.sort_values(by=["col1", "col2"], inplace=True)
            df_pred.sort_values(by=["col1", "col2"], inplace=True)
            df_true.drop_duplicates(subset=["col1", "col2"], inplace=True)
            df_pred.drop_duplicates(subset=["col1", "col2"], inplace=True)
            df_true.reset_index(drop=True, inplace=True)
            df_pred.reset_index(drop=True, inplace=True)

            # Assuming df1 and df2 are your two DataFrames
            common_rows = pd.merge(df_true, df_pred, how='inner', on=["col1", "col2"])
            num_common_rows = len(common_rows)
            precision = num_common_rows / len(df_pred) if len(df_pred) > 0 else 0
            recall = num_common_rows / len(df_true) if len(df_true) > 0 else 0
            
        except Exception as e:
            res = {
                "precision": None,
                "recall": 0,
            }
            return res
        
        res = {
                "precision": precision,
                "recall": recall,
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