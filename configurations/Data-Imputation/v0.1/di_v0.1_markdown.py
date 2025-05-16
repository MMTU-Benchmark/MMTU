from utils.table_serializer import MarkdownSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """Please fill in the missing value in the input table. The missing value is denoted by '[MISSING]'. Please only return the value filled in. Do not return the whole table.

Please return the value filled in JSON format: {"value": "filled_value"}. 


Input Table:
{{{input_table}}}

"""


dataset_config = {
    "task": "Data-Imputation",
    "version": "0.1_sample1000_markdown",
    "tag": ["0.1_sample1000_markdown", "0.1_sample1000_markdown_gpt35"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Data-Imputation/sample1000",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": MarkdownSerializer
        }
    }
}
