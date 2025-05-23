import os
import re
import json
import ast
from multiprocessing import Pool

import numpy as np
import pandas as pd
from tqdm import tqdm

def makedir(dir_list, file=None):
    save_dir = os.path.join(*dir_list)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    if file is not None:
        save_dir = os.path.join(save_dir, file)
    return save_dir

class BaseEvaluator(object):
    def __init__(self):
        self.group_keys = ["dataset", "tag", "note"]
        self.merge_keys = ["dataset", "tag", "note"]
        self.err_merge_keys = ["dataset", "tag", "note"]
        self.answer_key = None
        self.gt_key = "label"
        self.default_result = {"correct": 0}
    
    def _compute_metric(self, res) -> dict:
        # return a dict of evaluation metrics
        raise NotImplementedError

    def _evaluate_one(self, y_true, y_pred) -> dict:
        # return a dict of evaluation results
        raise NotImplementedError
    
    def extract_json_answer(self, text, answer_key):
        assert answer_key is not None
        if text.startswith("<think>"):
            match = re.match(r"<think>(.*?)</think>(.*)", text, re.DOTALL)
            text = match.group(2) if match else text

        pattern = r'{[^}]*}'  # Regex pattern to match strings inside curly braces while keeping the braces
        matches = re.findall(pattern, text)
        for match in matches:
            try:
                result = json.loads(match)
                if answer_key in result:
                    return result[answer_key]
            except:
                try:
                    result = ast.literal_eval(match)
                    if answer_key in result:
                        return result[answer_key]
                except:
                    continue
                continue
        return "JSONParsingError"

    def _get_pred(self, completion):
        # return the predicted answer
        return self.extract_json_answer(completion, self.answer_key)
    
    def _get_gt(self, metadata):
        # return the GT answer
        return metadata[self.gt_key]

    def parse_raw_result(self, raw_result, n_jobs=1):
        # return a DataFrame of parsed results
        result = []
        for _, row in tqdm(raw_result.iterrows(), total=len(raw_result), ncols=80, desc="Parsing results"):
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
            if row_res["completion"] is None:
                row_res["completion"] = ""
            # row_res["label"] = self._get_gt(row_res)
            row_res["prompt_completion"] = row_res["prompt"] + "\n" + row_res["completion"]
            row_res["prompt_tokens"] = row.prompt_tokens if "prompt_tokens" in row else None
            row_res["completion_tokens"] = row.completion_tokens if "completion_tokens" in row else None
            row_res["model_name"] = row.model_name if "model_name" in row else None
            row_res["time_taken"] = row.time_taken if "time_taken" in row else None
            row_res["y_pred"] = self._get_pred(row_res["completion"])
            row_res["y_gt"] = self._get_gt(row_res)
            
            # evaluate each row
            try:
                row_eval = self._evaluate_one(row_res["y_gt"], row_res["y_pred"])
            except Exception as e:
                print(f"Error in evaluating row {row_res['metadata']}: {e}")
                row_eval = self.default_result
            for k, v in row_eval.items():
                row_res[k] = v
                
            result.append(row_res)
        result = pd.DataFrame(result)
        return result
    
    def save_debug(self, result, debug_dir):
        model_name = debug_dir.split("/")[-1]
        for (dataset, version, _), group_df in result.groupby(["dataset", "tag", "note"]):
            group_df.to_csv(makedir([debug_dir], f"{dataset}_{version}_{model_name}.csv"), index=False)
            group_df.to_excel(makedir([debug_dir], f"{dataset}_{version}_{model_name}.xlsx"), index=False)
            
    def save_viz(self, result, viz_dir):
        raise NotImplementedError
    
    def evaluate_one_case(self, case):
        group_key, group_df = case
        metric_group = self._compute_metric(group_df)
        return group_key, metric_group

    def evaluate_by_group(self, result, group_keys, n_jobs=1):
        groups = list(result.groupby(group_keys))
        # evaluate result for each group
        if n_jobs == 1:
            eval_results = [self.evaluate_one_case(case) for case in groups]
        else:
            with Pool(n_jobs) as pool:
                eval_results = list(tqdm(pool.imap(self.evaluate_one_case, groups), total=len(groups), ncols=80, desc="Evaluating groups"))
        
        group_keys = pd.DataFrame([key for key, _ in eval_results], columns=group_keys)
        group_metric = pd.DataFrame([metric for _, metric in eval_results])
        eval_results = pd.concat([group_keys, group_metric], axis=1)
        return eval_results
    
    def evaluate(self, raw_result, debug_dir=None, viz_dir=None, n_jobs=1):
        result = self.parse_raw_result(raw_result, n_jobs)
        # Define a custom function
        def get_error(completion, y_pred):
            if completion is None:
                return 'None'
            if type(completion) != str:
                return 'CompletionNotString'
            if completion == 'Error: content filter':
                return 'content_filter'
            elif completion.startswith('API Timeout'):
                return 'timeout'
            elif completion == "":
                return 'empty'
            else:
                if y_pred == "JSONParsingError":
                    return 'JSONParsingError'
                return 'normal'

        # Use map with the custom function
        result['error'] = result.apply(lambda row: get_error(row['completion'], row['y_pred']), axis=1)

        # result['error'] = result[['completion', "y_true"]].map(get_error)
        eval_results = self.evaluate_by_group(result, self.group_keys, n_jobs=n_jobs)
        merge_results = result.groupby(self.merge_keys, as_index=False).agg(lambda x: list(x))
        avg_results = eval_results.groupby(self.merge_keys, as_index=False).mean(numeric_only=True).sort_values(by=self.merge_keys)
            
        error_cnt = None
        if "error" in result:
            error_cnt = result.groupby(self.err_merge_keys+["error"]).size().reset_index(name='count').pivot_table(index=self.err_merge_keys, columns="error", values='count', fill_value=0).reset_index()
        else:
            error_cnt = pd.DataFrame()
        
        if debug_dir is not None:
            print(f"Saving debug results to {debug_dir}")
            self.save_debug(result, debug_dir)
            
        if viz_dir is not None:
            self.save_viz(result, viz_dir)

        return avg_results, merge_results, error_cnt