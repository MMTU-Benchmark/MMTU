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
from datetime import datetime

class DTPBEBaseEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        self.answer_key = "output_value"

        self.run_time_executive = "<CMD>"
        self.run_time_file = "<FILE>"
        self.pl = "<PL>"
        self.codeBlockNotFound = f"{self.pl}CodeBlockNotFound"
        self.executionError = f"{self.pl}ExecutionError"
        
    def _evaluate_row(self, y_pred, case_path, exec_dir):        
        example_pred_res = None
        example_gt_res = pd.DataFrame()
        test_pred_res = None
        test_gt_res = pd.DataFrame()
        
        example_pred_res_list = None
        example_gt_res_list = None
        test_pred_res_list = None
        test_gt_res_list = None
        
        example_pred_res_path = None
        test_pred_res_path = None
        
        case_path = os.path.expandvars(case_path)
        assert os.path.exists(case_path), f"Case path {case_path} does not exist. Please make sure that you have downloaded the MMTU data. See README for more details."
        test_id = case_path.split("/")[-1]
        
        cur_exec_dir = f"{exec_dir}/{test_id}"
        if y_pred == self.codeBlockNotFound:
            y_pred_res = None
        else:
            cur_dir = os.getcwd()
            try:
                os.mkdir(cur_exec_dir)
                os.chdir(cur_exec_dir)

                # Run two test on examples and holdout
                assert os.path.exists(os.path.join(case_path, "example_input.csv"))
                assert os.path.exists(os.path.join(case_path, "example_output.csv"))
                assert os.path.exists(os.path.join(case_path, "test_input.csv"))
                assert os.path.exists(os.path.join(case_path, "test_output.csv"))
                
                shutil.copy(os.path.join(case_path, "example_input.csv"), "example_input.csv")
                shutil.copy(os.path.join(case_path, "example_output.csv"), "example_output.csv")
                shutil.copy(os.path.join(case_path, "test_input.csv"), "test_input.csv")
                shutil.copy(os.path.join(case_path, "test_output.csv"), "test_output.csv")

                with open(self.run_time_file, "w") as f:
                    f.write(y_pred)

                # run the python code for examples
                shutil.copy("example_input.csv", "input.csv")
                example_gt_res = pd.read_csv("example_output.csv", index_col=False, dtype=str).fillna('nan')
                example_gt_res_list = example_gt_res.to_numpy().tolist()
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
                    os.remove("input.csv")
                    

                if exit_code != 0:
                    # print(f"{self.pl} execution error: {error}")
                    example_pred_res = self.executionError
                else:
                    try:
                        assert os.path.exists("output.csv")
                        example_pred_res = pd.read_csv("output.csv", index_col=False, dtype=str).fillna('nan')
                        shutil.copy("output.csv", "run_example_output.csv")
                        example_pred_res_path = os.path.abspath("run_example_output.csv")
                        example_pred_res_list = example_pred_res.to_numpy().tolist()
                    except AssertionError:
                        example_pred_res = "ResultFileNotFound_Example"
                        example_pred_res_path = None
                    
                    
                # run the python code for test
                shutil.copy("test_input.csv", "input.csv")
                test_gt_res = pd.read_csv("test_output.csv", index_col=False, dtype=str).fillna('nan')
                test_gt_res_list = test_gt_res.to_numpy().tolist()
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
                    os.remove("input.csv")
                    

                if exit_code != 0:
                    # print(f"{self.pl} execution error: {error}")
                    test_pred_res = self.executionError
                else:
                    try:
                        assert os.path.exists("output.csv")
                        test_pred_res = pd.read_csv("output.csv", index_col=False, dtype=str).fillna('nan')
                        shutil.copy("output.csv", "run_test_output.csv")
                        test_pred_res_path = os.path.abspath("run_test_output.csv")
                        test_pred_res_list = test_pred_res.to_numpy().tolist()
                    except AssertionError:
                        test_pred_res = "ResultFileNotFound_Test"
                        test_pred_res_path = None
                    
            except Exception as e:
                print("Unexpected error:", e)
            finally:
                os.chdir(cur_dir)

        flag_example = False
        if y_pred != self.codeBlockNotFound and type(example_pred_res) == pd.DataFrame:
            try:
                flag_example = example_pred_res.equals(example_gt_res)
            except Exception as e:
                pass
            
        flag_test = False
        if y_pred != self.codeBlockNotFound and type(test_pred_res) == pd.DataFrame:
            try:
                flag_test = test_pred_res.equals(test_gt_res)
            except Exception as e:
                pass

        res = {
            "correct": 1 if flag_test else 0,
            "correct_example": 1 if flag_example else 0,
            "exec_dir": cur_exec_dir,
            "test_gt_res_list": test_gt_res_list,
            "test_pred_res_list": test_pred_res_list,
            "test_pred_res_path": test_pred_res_path,
            "example_gt_res_list": example_gt_res_list,
            "example_pred_res_list": example_pred_res_list,
            "example_pred_res_path": example_pred_res_path
        }
        return res
    
    def _compute_metric(self, res):
        acc = res["correct"].values.mean()
        acc_example = res["correct_example"].values.mean()
        metric = {
            "acc": acc,
            "acc_example": acc_example
        }
        return metric

    def _get_pred(self, completion):
        if type(completion) != str:
            return self.codeBlockNotFound
        pattern = re.compile(f"```{self.pl}(.*?)```", re.DOTALL)
        matches = re.findall(pattern, completion)
        if len(matches) == 0:
            return self.codeBlockNotFound
        return matches[0].strip()
    
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
        # row_res["method"] = row_res["sampleMethod"] + row_res["numSamples"]
        # row_res["prompt_completion"] = row_res["prompt"] + "\n" + row_res["completion"]
        row_res["prompt_tokens"] = row.prompt_tokens if "prompt_tokens" in row else None
        row_res["completion_tokens"] = row.completion_tokens if "completion_tokens" in row else None
        row_res["model_name"] = row.model_name if "model_name" in row else None
        row_res["time_taken"] = row.time_taken if "time_taken" in row else None
        row_res["y_pred"] = self._get_pred(row_res["completion"])
        
        # evaluate each row
        row_eval = self._evaluate_row(row_res["y_pred"], row_res["case_path"], exec_dir)
        for k, v in row_eval.items():
            row_res[k] = v

        return row_res
    
    def parse_raw_result(self, raw_result, n_jobs=1):
        result = []
        print("n_jobs", n_jobs)
        
        # prepare for runtime
        mmtu_home = os.environ['MMTU_HOME']
        exec_root = os.path.join(mmtu_home, "tmp_exec")
        os.makedirs(exec_root, exist_ok=True)
        now = datetime.now()
        timestamp_str = now.strftime("%Y-%m-%d_%H-%M-%S")
        exec_dir = os.path.join(exec_root, f"timestamp_{timestamp_str}")
        print(f"exec_dir: {exec_dir}")
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
    