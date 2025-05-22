from .base_evaluator import BaseEvaluator

import os
import json
import re
import ast
import pandas as pd

class TNIAHEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        self.answer_key = ["row", "column"]

    def _get_pred(self, completion):
        # return the predicted answer
        pred = {}
        for key in self.answer_key:
            ans = self.extract_json_answer(completion, key)
            if ans == "JSONParsingError":
                return "JSONParsingError"
            pred[key] = ans
        return pred
    
    def _get_gt(self, metadata):
        # return the GT answer
        tbl_path = os.path.join(metadata["case_path"], "data.csv")
        tbl_path = os.path.expandvars(tbl_path)
        df = pd.read_csv(tbl_path, nrows=1)
        col_name = df.columns[metadata["needle_col_idx"]]
        return {"row": metadata["needle_row_idx"], "column": col_name}
        
    def _evaluate_one(self, y_true, y_pred):
        if not isinstance(y_true, dict) or not isinstance(y_pred, dict):
            return {"correct": 0, "row_correct": 0, "col_correct": 0}
        
        try:
            if int(y_true["row"]) == int(y_pred["row"]):
                row_correct = 1
            else:
                row_correct = 0
        except:
            row_correct = 0
            
        if  str(y_true["column"]).strip().lower() == str(y_pred["column"]).strip().lower():
            col_correct = 1
        else:
            col_correct = 0
        
        if row_correct == 1 and col_correct == 1:
            correct = 1
        else:
            correct = 0
        
        res = {
            "correct": correct,
            "row_correct": row_correct,
            "col_correct": col_correct
        }
        return res
    
    def _compute_metric(self, res):
        acc = res["correct"].values.mean()
        row_acc = res["row_correct"].values.mean()
        col_acc = res["col_correct"].values.mean()
        metric = {
            "acc": acc,
            "row_acc": row_acc,
            "col_acc": col_acc
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
            # group_df.to_csv(makedir([debug_dir], f"{dataset}_{version}_{model_name}.csv"), index=False)
            # group_df.to_excel(makedir([debug_dir], f"{dataset}_{version}_{model_name}.xlsx"), index=False)
            def round_by_interval(x, interval):
                if type(x) == list:
                    return [(int((i-1) / interval) +1 ) * interval for i in x]
                return int(x / interval) * interval
            
            df = group_df.copy()
            df["needle_row_idx_bin5"] = round_by_interval(df["needle_row_idx"].values.tolist(), 5)
            df["needle_col_idx_bin5"] = round_by_interval(df["needle_col_idx"].values.tolist(), 5)
            
            x_axis = "needle_col_idx_bin5"
            y_axis = "needle_row_idx_bin5"
            values= ["correct", "col_correct", "row_correct"]
            
            fig, axes = plt.subplots(1, 3, figsize=(30, 8))
            for ax, val in zip(axes, values):
                acc_x_y = df.groupby([x_axis, y_axis])[val].mean().reset_index()
                acc_x_y = acc_x_y.pivot(index=y_axis, columns=x_axis, values=val)
                sns.heatmap(acc_x_y, 
                            cbar=True, 
                            annot=True,
                            fmt=".2f", 
                            cmap=cmap, 
                            ax=ax,
                            vmin=0, 
                            vmax=1
                            )
                ax.set_title(f'{val}')
                # ax.invert_yaxis()
            fig.suptitle(f"Task: {task_name}, Dataset: {dataset}, Version: {version}, Model: {model_name}\nNote: {note}")
            fig.savefig(f"{viz_dir}/{dataset}_{version}_{model_name}.png")
            print(f"Visualization Saved to: {viz_dir}/{dataset}_{version}_{model_name}.png")
            fig.clear()
            plt.close(fig)
            
            fig = plt.figure(figsize=(8, 8))
            acc_x_y = df.groupby([x_axis, y_axis])["correct"].mean().reset_index()
            acc_x_y = acc_x_y.pivot(index=y_axis, columns=x_axis, values="correct")
            ax = sns.heatmap(acc_x_y, 
                        cbar=True, 
                        annot=True,
                        fmt=".2f", 
                        cmap=cmap, 
                        vmin=0, 
                        vmax=1
                        )
            ax.set_xlabel("Column Index")
            ax.set_ylabel("Row Index")
            # Move x-axis ticks and title to top
            ax.xaxis.set_ticks_position('top')
            ax.xaxis.set_label_position('top')
                # ax.invert_yaxis()
            # fig.suptitle(f"Task: {task_name}, Dataset: {dataset}, Version: {version}, Model: {model_name}\nNote: {note}")
            fig.set
            fig.savefig(f"{viz_dir}/{dataset}_{version}_{model_name}_correct.pdf")
            print(f"Visualization Saved to: {viz_dir}/{dataset}_{version}_{model_name}_correct.pdf")
            
            try:
                import numpy as np

                context_length_values = df["context_length"].values.tolist()
                bins = np.linspace(min(context_length_values), max(context_length_values), 11)  # 11 edges for 10 bins
                bin_indices = np.digitize(context_length_values, bins, right=True)
                df["context_length_bin"] = bin_indices
                
                context_length_bins = df["context_length_bin"].unique()
                context_length_bins.sort()

                for context_length_bin in context_length_bins:
                    # print(f"For context_length_bin {context_length_bin} with mean context length {df.groupby('context_length_bin')['context_length'].mean()[context_length_bin]}")
                    fig, axes = plt.subplots(1, 3, figsize=(30, 8))
                    for ax, val in zip(axes, values):
                        acc_x_y = df[df["context_length_bin"] == context_length_bin].groupby([x_axis, y_axis])[val].mean().reset_index()
                        acc_x_y = acc_x_y.pivot(index=y_axis, columns=x_axis, values=val)
                        sns.heatmap(acc_x_y, 
                                    cbar=True, 
                                    annot=True,
                                    fmt=".2f", 
                                    cmap=cmap, 
                                    ax=ax,
                                    vmin=0, 
                                    vmax=1
                                    )
                        ax.set_title(f'{val}')
                        # ax.invert_yaxis()
                    fig.suptitle(f"Task: {task_name}, Dataset: {dataset}, Version: {version}, Model: {model_name}\nMean context length: {df.groupby('context_length_bin')['context_length'].mean()[context_length_bin]}. Total cases: {len(df[df['context_length_bin'] == context_length_bin])}", multialignment='center')
                    fig.savefig(f"{viz_dir}/{dataset}_{version}_{model_name}_context_length_{context_length_bin}.png")
                    print(f"Visualization Saved to: {viz_dir}/{dataset}_{version}_{model_name}_context_length_{context_length_bin}.png")
                    plt.close(fig)
            except:
                print("context_length_bin visualization failed")
                pass