from utils.table_serializer import HTMLSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """Please fill in the missing value in the input table. The missing value is denoted by '[MISSING]'. Please only return the value filled in. Do not return the whole table.

No explanation, return the value filled in JSON format: {"value": "filled_value"}. 

Input Table:
{{{input_table}}}

"""


dataset_config = {
    "task": "Data-Imputation",
    "version": "1.0_sample1000_html",
    "tag": ["1.0_sample1000_html"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Data-Imputation/sample1000-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": HTMLSerializer
        }
    }
}
