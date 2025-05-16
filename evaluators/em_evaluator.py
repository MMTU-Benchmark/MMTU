from .base_evaluator import BaseEvaluator

class EMEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        self.answer_key = "label"
        
    def _evaluate_one(self, y_true, y_pred):
        if y_true == 1 and y_pred == "match":
            correct = 1
        elif y_true == 0 and y_pred == "non-match":
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