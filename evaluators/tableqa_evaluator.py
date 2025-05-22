from .base_evaluator import BaseEvaluator

class TQAEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()
        self.answer_key = "answer"
        
    def _evaluate_one(self, y_true, y_pred):
        # print("--------------------")
        # print(y_true, y_pred)
        # print(f"str(y_true).lower(): {str(y_true).lower()}")
        # print(f"str(y_pred).lower(): {str(y_pred).lower()}")
        # print(f"str(y_true).lower() == str(y_pred).lower() == {str(y_true).lower() == str(y_pred).lower()}")
        correct = 0
        if str(y_true).lower() == str(y_pred).lower():
            return {"correct": 1}
        else:
            if type(y_pred) == str:
                if "%" in y_pred:
                    y_pred = y_pred.replace("%", "")
                    if round(float(y_true), 2) == round(float(y_pred), 2):
                        return {"correct": 1}
                    
                    y_pred = float(y_pred) / 100
                    if round(float(y_true), 2) == round(float(y_pred), 2):
                        return {"correct": 1}
                elif "$" in y_pred:
                    y_pred = y_pred.replace("$", "").replace(",", "")
                    if round(float(y_true), 2) == round(float(y_pred), 2):
                        return {"correct": 1}
            else:
                try:
                    if round(float(y_true), 2) == round(float(y_pred), 2):
                        correct = 1
                    else:
                        correct = 0
                except:
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
        