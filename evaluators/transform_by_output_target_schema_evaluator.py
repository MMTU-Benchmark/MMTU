from .base_evaluator import BaseEvaluator
import utils
import pandas as pd
import re
import numpy as np
import os
import time
from multiprocessing import Pool
import subprocess
from pandas.errors import EmptyDataError
import json
import shutil

class TransformByTargetSchemaEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        # self.answer_key = "output_value"

        self.run_time_executive = "python3"
        self.run_time_file = "transform.py"
        self.pl = "python"
        self.codeBlockNotFound = f"{self.pl}CodeBlockNotFound"
        self.executionError = f"{self.pl}ExecutionError"
        
    def _evaluate_row(self, y_pred, case_path, source_files, exec_dir):        
        target_pred_res = pd.DataFrame()
        target_gt = pd.DataFrame()
        
        target_gt_list = []
        target_pred_res_list = []
        
        target_gt_columns = []
        target_pred_res_columns = []
        
        error_msg = ""
        
        assert os.path.exists(case_path)
        test_id = case_path.split("/")[-1]
        
        cur_exec_dir = f"{exec_dir}/{test_id}"
        if y_pred == self.codeBlockNotFound:
            pass
        else:
            cur_dir = os.getcwd()
            try:
                os.mkdir(cur_exec_dir)
                os.chdir(cur_exec_dir)

                for src_file in source_files:
                    assert os.path.exists(os.path.join(case_path, src_file))
                    shutil.copy(os.path.join(case_path, src_file), os.path.join(cur_exec_dir, src_file.replace("test_", "source_")))
                    # print(f"Copying {src_file} to {cur_exec_dir} as {src_file.replace('test_', 'source_')}")

                assert os.path.exists(os.path.join(case_path, "target.csv"))
                shutil.copy(os.path.join(case_path, "target.csv"), os.path.join(cur_exec_dir, "target.csv"))

                with open(self.run_time_file, "w") as f:
                    f.write(y_pred)

                target_gt = pd.read_csv("target.csv", index_col=0).fillna('nan')
                target_gt = target_gt.astype({col: 'float' for col in target_gt.select_dtypes(include='number').columns})

                target_gt_list = target_gt.to_numpy().tolist()
                target_gt_columns = target_gt.columns.tolist()
                exit_code = None
                try:
                    result = subprocess.run(
                        [self.run_time_executive, self.run_time_file], capture_output=True, text=True, timeout=10)
                    exit_code = result.returncode
                    output = result.stdout.strip()
                    error = result.stderr.strip()
                except Exception as e:
                    print("-----TEST-----")
                    print(test_id)
                    print(e)
                finally:
                    pass
                    

                if exit_code != 0:
                    # print(f"{self.pl} execution error: {error}")
                    # target_pred_res = self.executionError
                    error_msg += self.executionError + "\n"
                else:
                    try:
                        assert os.path.exists("output.csv")
                        target_pred_res = pd.read_csv("output.csv", index_col=False).fillna('nan')
                        target_pred_res = target_pred_res.astype({col: 'float' for col in target_pred_res.select_dtypes(include='number').columns})
                        shutil.copy("output.csv", "run_output.csv")
                        target_pred_res_path = os.path.abspath("run_output.csv")
                        target_pred_res_list = target_pred_res.to_numpy().tolist()
                        target_pred_res_columns = target_pred_res.columns.tolist()
                    except AssertionError:
                        # target_pred_res = "ResultFileNotFound"
                        error_msg += "ResultFileNotFound\n"
                        target_pred_res_path = None
                    
                    
            except Exception as e:
                print("Unexpected error:", e)
            finally:
                os.chdir(cur_dir)
            
        flag_test = False
        flag_test_round10 = False
        columns_match = target_pred_res_columns == target_gt_columns
        if y_pred != self.codeBlockNotFound and type(target_pred_res) == pd.DataFrame and columns_match:
            try:
                target_pred_res.sort_values(by=target_pred_res.columns.tolist(), inplace=True)
                target_gt.sort_values(by=target_gt.columns.tolist(), inplace=True)
                flag_test = target_pred_res.equals(target_gt)
                flag_test_round10 = target_pred_res.round(10).equals(target_gt.round(10))
            except Exception as e:
                print(f"Error in case {test_id}: {e}")
                pass

        res = {
            "correct": 1 if flag_test_round10 else 0,
            "correct_exact": 1 if flag_test else 0,
            "columns_match": columns_match,
            "num_rows_match": target_pred_res.shape[0] == target_gt.shape[0],
            "exec_dir": cur_exec_dir,
            "target_gt": target_gt_list,
            "target_pred": target_pred_res_list,
            "target_pred_res": target_pred_res,
            "error_msg": error_msg,
        }
        return res
    
    def _compute_metric(self, res):
        acc = res["correct"].values.mean()
        metric = {
            "acc": acc,
        }
        return metric

    def _get_pred(self, completion):
        pattern = re.compile(f"```{self.pl}(.*?)```", re.DOTALL)
        matches = re.findall(pattern, completion)
        if len(matches) == 0:
            return self.codeBlockNotFound
        return matches[0].strip()
        
    # def _get_gt(self, label):
        # js = json.loads(label)
        # return js[self.answer_key]
        # gt = self.extract_json_answer(label, self.answer_key)
        # if gt == "JSONParsingError":
        #     raise Exception("Parsing Error on ground truth")
        # return gt
    
    def parse_raw(self, row, exec_dir):
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
        src_files = [x["data"] for x in row_res["test"]]
        # evaluate each row
        row_eval = self._evaluate_row(row_res["y_pred"], row_res["case_path"], src_files, exec_dir)
        for k, v in row_eval.items():
            row_res[k] = v

        return row_res
    
    def parse_raw_result(self, raw_result, n_jobs=1):
        result = []
        print("n_jobs", n_jobs)
        
        # prepare for runtime
        exec_root = "/datadrive/junjie/tmp_runtime"
        os.makedirs(exec_root, exist_ok=True)
        exec_dir = os.path.join(exec_root, f"timestamp_{time.time_ns()}")
        os.mkdir(exec_dir)

        if n_jobs == 1:
            for _, row in raw_result.iterrows():
                row_res = self.parse_raw(row, exec_dir)
                result.append(row_res)
        else:
            rows = []
            for _, row in raw_result.iterrows():
                rows.append((row, exec_dir))
            with Pool(n_jobs) as pool:
                result = pool.starmap(self.parse_raw, rows)
        result = pd.DataFrame(result)
        return result
    