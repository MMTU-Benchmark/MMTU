from utils.table_serializer import MarkdownSerializer
from utils.table_processor import ShuffleRowsProcessor, ShuffleColumnsKeepFirstThreeProcessor

prompt_template = """Please fill in the missing value in the input table. The missing value is denoted by '[MISSING]'. Please only return the value filled in. Do not return the whole table.

No explanation, return the value filled in JSON format: {"value": "filled_value"}. 

Input Table:
{{{input_table}}}

"""


dataset_config = {
    "task": "Data-Imputation",
    "version": "1.0_sample200_markdown_table_permutation",
    "tag": ["1.0_sample200_markdown_table_permutation"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Data-Imputation/sample200-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": MarkdownSerializer,
            "processors": [ShuffleColumnsKeepFirstThreeProcessor(), ShuffleRowsProcessor()],
        }
    }
}
