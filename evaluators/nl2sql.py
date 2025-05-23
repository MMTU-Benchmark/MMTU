import pandas as pd
import sqlite3
import json
import re
import os
from tqdm import tqdm

from .base_evaluator import BaseEvaluator

def are_lists_equal(list1, list2):
    # Check if the lengths of the lists are equal
    if len(list1) != len(list2):
        return False
    
    # Iterate through the elements of the lists
    for i in range(len(list1)):
        # Check if the lengths of the sublists are equal
        if len(list1[i]) != len(list2[i]):
            return False
        
        # Compare the elements of the sublists
        for j in range(len(list1[i])):
            if list1[i][j] != list2[i][j]:
                try:
                    if abs((float(list1[i][j]) -  float(list2[i][j])) / float(list2[i][j])) < 0.01 and abs(float(list1[i][j]) -  float(list2[i][j])) < 0.01:
                        return True
                except:
                    return False
                return False
    
    # If all comparisons pass, the lists are equivalent
    return True

def safe_to_numeric(x):
    try:
        return pd.to_numeric(x)  # Try converting without an errors parameter.
    except Exception:
        return x  # Return the original value if conversion fails.
    
import time
# Create a function to limit query execution time
def execute_with_timeout(cursor, query, timeout_ms):
    start_time = time.time()
    timeout_s = timeout_ms / 1000.0

    # Define the progress handler callback
    def progress_handler():
        if time.time() - start_time > timeout_s:
            # Returning a non-zero value aborts the query
            return 1
        return 0

    # Set the progress handler
    cursor.connection.set_progress_handler(progress_handler, 1000)  # Called every 1000 instructions

    try:
        cursor.execute(query)
        rst = cursor.fetchall()  # Fetch the results
        headers = [description[0] for description in cursor.description]
        df = pd.DataFrame(rst, columns=headers)
        return df  # Return the results if query succeeds
    except sqlite3.OperationalError as e:
        # print(f"Operational error: {e}")
        if str(e) == "interrupted":
            print(f"Query timed out at {time.time() - start_time} seconds")
        else:
            raise  # Re-raise other operational errors
    finally:
        # Reset the progress handler after execution
        cursor.connection.set_progress_handler(None, 0)

class NSEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()

    def _evaluate_one(self, sql, table_path, gt_path): # type: ignore
        """Evaluate the generated SQL query against the ground truth."""
        table_path = os.path.expandvars(table_path)
        assert os.path.exists(table_path), f"Table path {table_path} does not exist.  Please make sure that you have downloaded the MMTU data. See README for more details."
        gt_path = os.path.expandvars(gt_path)
        assert os.path.exists(gt_path), f"Ground truth path {gt_path} does not exist.  Please make sure that you have downloaded the MMTU data. See README for more details."

        # Load the table and ground truth
        gt = pd.read_csv(gt_path)
        gt_rst = gt.map(lambda x: safe_to_numeric(x)).fillna("None").values.tolist()

        y_pred_res = None
        if table_path.endswith(".csv"):
            table = pd.read_csv(table_path, keep_default_na=False)
            conn = sqlite3.connect(":memory:")
            table.to_sql("table", conn, index=False)
        elif table_path.endswith(".sqlite"):
            conn = sqlite3.connect(table_path)
        else:
            raise Exception("Unknown table format")
        
        try:
            # Execute the SQL query on the table
            y_pred_res = execute_with_timeout(conn.cursor(), sql, 15000).map(lambda x: safe_to_numeric(x)).fillna("None").values.tolist()  # Set timeout to 15 seconds
            # y_pred_res = pd.read_sql_query(sql, conn).map(lambda x: safe_to_numeric(x)).fillna("None").values.tolist()
        except Exception as e:
            y_pred_res = "SQLExecutionError"
        finally:
            conn.close()

        flag = False
        errorMsg = ""
        if sql != "SQLCodeBlockNotFound" and y_pred_res != "SQLExecutionError":
            # if len(y_true_res) == len(y_pred_res):
            # flag = y_true_res == y_pred_res
            flag = are_lists_equal(y_pred_res, gt_rst)
            if gt_rst in [[], [[]], [["None"]]] and y_pred_res in [[], [[]], [["None"]]]:
                flag = True
            if not flag:
                y_pred_res_flatten = [item for sublist in y_pred_res for item in sublist]
                y_true_res_flatten = [item for sublist in gt_rst for item in sublist]
                if (len(y_pred_res) == len(gt_rst)) and set(y_true_res_flatten).issubset(set(y_pred_res_flatten)):
                    errorMsg = "superset" 
                elif (len(y_pred_res) == len(gt_rst)) and set(y_pred_res_flatten).issubset(set(y_true_res_flatten)) and y_pred_res_flatten not in [[], ["None"]]:
                    errorMsg = "subset"
                else:
                    errorMsg = "others"
            # else:
                # errorMsg = "others"
        else:
            errorMsg = "compile/execution error"
        return {
            "correct": 1 if flag else 0,
            "y_pred_rst": y_pred_res,
            "y_true_rst": gt_rst,
            "error": errorMsg
        }

    def _get_pred(self, completion):
        pattern = re.compile(r"```sql(.*?)```", re.DOTALL)
        matches = re.findall(pattern, completion)
        if len(matches) == 0:
            if completion.lower().strip().startswith("select"):
                return completion
            return "SQLCodeBlockNotFound"
        return matches[-1].strip()

    def parse_raw_result(self, raw_result, n_jobs=1):
        args = []
        result = []
        for _, row in tqdm(raw_result.iterrows(), total=len(raw_result), ncols=80):
            row_res = json.loads(row.metadata)
            row_res["metadata"] = row.metadata
            row_res["prompt"] = row.prompt
            if "choices" in row:
                row_res["prompt"] = row.prompt
                row_res["completion"] = row.choices[0]["text"]
            elif "response" in row:
                row_res["completion"] = row.response
            else:
                raise Exception("Unknown format")
            row_res["prompt_tokens"] = row.prompt_tokens if "prompt_tokens" in row else None
            row_res["completion_tokens"] = row.completion_tokens if "completion_tokens" in row else None
            row_res["model_name"] = row.model_name if "model_name" in row else None
            row_res["time_taken"] = row.time_taken if "time_taken" in row else None
            # row_res["method"] = row_res["sampleMethod"] + row_res["numSamples"]
            # row_res["prompt_completion"] = row_res["prompt"] + "\n" + row_res["completion"]
            row_res["y_pred"] = self._get_pred(row_res["completion"])
            row_res["y_true"] = row_res["label"]
            
            # evaluate each row
            if row_res["dataset"] != "WikiSQL":
                args.append([row_res["y_pred"], row_res["sqlite_path"], os.path.join(row_res["case_path"], "result_gt.csv")])
                row_eval = self._evaluate_one(row_res["y_pred"], row_res["sqlite_path"], os.path.join(row_res["case_path"], "result_gt.csv"))
            else:
                args.append([row_res["y_pred"], os.path.join(row_res["case_path"], "data.csv"), os.path.join(row_res["case_path"], "result_gt.csv")])
                row_eval = self._evaluate_one(row_res["y_pred"], os.path.join(row_res["case_path"], "data.csv"), os.path.join(row_res["case_path"], "result_gt.csv"))
            for k, v in row_eval.items():
                row_res[k] = v
                
            result.append(row_res)
        result = pd.DataFrame(result)
        return result
    
    def _compute_metric(self, res):
        acc = res["correct"].values.mean()
        metric = {
            "acc": acc
        }
        return metric

