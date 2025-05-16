from .base_evaluator import BaseEvaluator
import json
import pandas as pd

class SMEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        self.answer_key = "column_mappings"
        self.default_result = {"precision": None, "recall": None}
        
    def parse_matching(self, label):
        gt = {}
        if type(label) != list:
            return gt
        for x in label:
            try:
                if not x or len(x) != 2:
                    # print(x)
                    continue
            except Exception as e:
                # print(x)
                continue
            source, target = x
            if target is None:
                target = "None"
            if source is None:
                source = "None"
            source = str(source).strip()
            target = str(target).strip()
            if source == "nan":
                source = "None"
            if target == "nan":
                target = "None"
            if len(target) == 0:
                continue
            if source == "None" or target == "None":
                continue
            gt[source] = target
        return gt
        
    def _evaluate_row(self, y_true, y_pred):
        y_true = self.parse_matching(y_true)
        y_pred = self.parse_matching(y_pred)
        # no rand
        count = 0
        for k in y_pred.keys():
            if k in y_true and y_pred[k] == y_true[k]:
                count += 1
        if len(y_true) == 0:
            recall = None
        else:
            recall = count / len(y_true)
        if len(y_pred) == 0:
            precision = None
        else:
            precision = count / len(y_pred)
        res = {
            "recall": recall,
            "precision": precision
        }
        return res
    
    def _compute_metric(self, res):
        acc = res["recall"].mean()
        prec = res["precision"].mean()
        if not acc == 0 and not prec == 0:
            f1 = 2 * acc * prec / (acc + prec)
        else:
            f1 = 0
        # f1 = 2 * acc * prec / (acc + prec)
        metric = {
            "recall": acc,
            "prec": prec,
            "f1": f1
        }
        return metric
    
    def parse_raw_result(self, raw_result, n_jobs=1):
        result = []
        for _, row in raw_result.iterrows():
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
            row_res["y_gt"] = row_res["column_mappings"]
            row_res["y_pred_eval"] = self.parse_matching(row_res["y_pred"])
            row_res["y_gt_eval"] = row_res["column_mappings"]
            
            # evaluate each row
            try:
                row_eval = self._evaluate_row(row_res["y_gt"], row_res["y_pred"])
            except Exception as e:
                print(f"Error in evaluating row: {e}")
                row_eval = self.default_result
            for k, v in row_eval.items():
                row_res[k] = v
                
            result.append(row_res)
        result = pd.DataFrame(result)
        return result