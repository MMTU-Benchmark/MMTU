from utils.table_serializer import JsonWithIndexSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are given an Excel worksheet snippet consisting of a Target Cell (labeled as "[Target Cell]") and its surrounding values — up to 10 rows above/below and 10 columns left/right. Analyze the surrounding cells and determine the most likely Microsoft Excel formula that should go in the Target Cell.

1. Use standard Excel syntax, e.g. a formula always begins with an equal sign (=).
2. Base the formula on visible patterns, references to nearby cells, aggregations, or common Excel logic.
3. Assume the Target Cell originally contained a formula, and your goal is to reconstruct it as accurately as possible.
4. If multiple formulas are possible, choose the most reasonable or commonly used based on context.
5. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

***EXAMPLE:***

{{{fewshots}}}

***END OF EXAMPLE.***

**INPUT:**
Input Excel Snippet in JSON format:
{{{input_table}}}

**OUTPUT:**

"""

fewshots_template = """**INPUT:**
Input Excel Snippet in JSON format:
{{{input_table}}}

**OUTPUT:**
{{{output}}}

"""


dataset_config = {
    "task": "Formula-prediction-context",
    "version": "0.2_sample1000_json_3shot",
    "tag": ["0.2_sample1000_json_3shot"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Formula-prediction-context/sample1000-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas.w_idx",
            "serializer": JsonWithIndexSerializer
        },
        "fewshots": {
            "type": "fewshot",
            "path": "3shots",
            "info": "info.json",
            "template": fewshots_template,
            "fields": {
                "input_table": {
                "type": "table.csv",
                "path": "data.csv",
                "reader": "pandas.w_idx",
                "serializer": JsonWithIndexSerializer
            },
                "output": {
                    "type": "text",
                    "name": "output"
                },
            }
        }
    }
}
