from utils.table_serializer import MarkdownWithIndexSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
{{{input_table}}}

"""


dataset_config = {
    "task": "Formula-prediction-context",
    "version": "1.0_sample1000_markdown_4k",
    "tag": ["1.0_sample1000_markdown_4k"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Formula-prediction-context/sample1000-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas.w_idx",
            "serializer": MarkdownWithIndexSerializer
        }
    }
}
