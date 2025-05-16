from .data_transform_pbe_evaluator import DTPBEBaseEvaluator

class DTPBEPythonEvaluator(DTPBEBaseEvaluator):
    def __init__(self):
        super().__init__()
        self.run_time_executive = "python3"
        self.run_time_file = "transform.py"
        self.pl = "python"

        self.codeBlockNotFound = f"{self.pl}CodeBlockNotFound"
        self.executionError = f"{self.pl}ExecutionError"