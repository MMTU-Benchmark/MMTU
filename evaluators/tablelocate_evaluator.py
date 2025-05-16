from .base_evaluator import BaseEvaluator

import os
import json
import re
import ast
import pandas as pd

class TableLocateEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        self.answer_key = "cell"
    
    def _get_gt(self, metadata):
        # return the GT answer
        gt = metadata["needle_value"]
        # try:
        #     gt = float(gt)
        #     gt = round(gt, 10)
        # except:
        #     return metadata["needle_value"]
        return gt
        
    def _evaluate_one(self, y_true, y_pred):
        correct = 0
        if str(y_true) == str(y_pred):
            correct = 1
        try:
            if float(y_true) == float(y_pred):
                correct = 1
        except:
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
    
    def save_viz(self, result, viz_dir):
        import matplotlib.pyplot as plt
        from matplotlib.colors import LinearSegmentedColormap
        import seaborn as sns
        cmap = LinearSegmentedColormap.from_list("custom_cmap", ["#F0496E", "#EBB839", "#0CD79F"])
        
        
        model_name = viz_dir.split("/")[-1]
        task_name = viz_dir.split("/")[-2]
        
        for (dataset, version, note), group_df in result.groupby(["dataset", "version", "note"]):
            df = group_df.copy()
        
            def round_by_interval(x, interval):
                if type(x) == list:
                    return [(int((i-1) / interval) +1 ) * interval for i in x]
                return (int((x-1) / interval) +1 ) * interval

            df["needle_row_idx_bin5"] = round_by_interval(df["needle_row_idx"].values.tolist(), 5)
            df["needle_col_idx_bin5"] = round_by_interval(df["needle_col_idx"].values.tolist(), 5)

            x_axis = "needle_row_idx_bin5"
            y_axis = "needle_col_idx_bin5"
            value = "correct"

            fig, ax = plt.subplots(figsize=(10, 8))
            acc_x_y = df.groupby([x_axis, y_axis])[value].mean().reset_index()
            acc_x_y = acc_x_y.pivot(index=y_axis, columns=x_axis, values=value)
            sns.heatmap(
                        acc_x_y, 
                        cbar=True, 
                        annot=True,
                        fmt=".2f", 
                        cmap=cmap, 
                        ax=ax
                        # vmin=0, 
                        # vmax=1
                        )
            ax.set_title(f"{value}")
            ax.invert_yaxis()
            fig.suptitle(f"Task: {task_name}, Dataset: {dataset}, Version: {version}, Model: {model_name}\n Note: {note}", fontsize=18)  # Increase suptitle font size
            fig.savefig(f"{viz_dir}/{dataset}_{version}_{model_name}.png")
            print(f"Saving {viz_dir}/{dataset}_{version}_{model_name}.png")
            plt.close(fig)
            
            x_axis = "needle_row_idx"
            y_axis = "needle_col_idx"
            value = "correct"
            
            fig, ax = plt.subplots(figsize=(100, 80))
            acc_x_y = df.groupby([x_axis, y_axis])[value].mean().reset_index()
            acc_x_y = acc_x_y.pivot(index=y_axis, columns=x_axis, values=value)
            sns.heatmap(
                        acc_x_y, 
                        cbar=True, 
                        annot=True,
                        fmt=".2f", 
                        cmap=cmap, 
                        ax=ax,
                        annot_kws={"size": 20}  # Increase font size for annotations
                        # vmin=0, 
                        # vmax=1
                        )
            ax.set_title(f"{value}", fontsize=24)  # Increase title font size
            ax.tick_params(axis='both', which='major', labelsize=20)  # Increase tick label font size
            ax.invert_yaxis()
            fig.suptitle(f"Task: {task_name}, Dataset: {dataset}, Version: {version}, Model: {model_name}", fontsize=28)  # Increase suptitle font size
            fig.savefig(f"{viz_dir}/{dataset}_{version}_{model_name}_100x100.png")
            print(f"Saving {viz_dir}/{dataset}_{version}_{model_name}_100x100.png")
            plt.close(fig)