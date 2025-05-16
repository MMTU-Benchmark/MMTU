from .base_evaluator import BaseEvaluator

class ListToTableEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        self.answer_key = "table"
        
    def _evaluate_one(self, y_true, y_pred):
        y_pred_rows = y_pred.split("\n")
        y_pred_rows = ["||".join([item.strip() for item in row.split("||")]) for row in y_pred_rows]
        y_pred = "\n".join(y_pred_rows)
        if y_true == y_pred:
            correct = 1
        else:
            correct = 0
        res = {
            "correct": correct
        }
        return res
    
    def _compute_metric(self, res):
        acc = res["correct"].values.mean()
        metric = {
            "acc": acc
        }
        return metric