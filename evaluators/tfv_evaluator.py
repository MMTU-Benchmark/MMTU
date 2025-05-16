from .base_evaluator import BaseEvaluator

class TFVEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        self.answer_key = "label"
        
    def _evaluate_one(self, y_true, y_pred):
        if str(y_true).lower() == str(y_pred).lower():
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