from utils.table_serializer import MarkdownSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """Please fill in the missing value in the input table. The missing value is denoted by '[MISSING]'. Please only return the value filled in. Do not return the whole table.

No explanation, return the value filled in JSON format: {"value": "filled_value"}. 

***EXAMPLE:***

{{{fewshots}}}

***END OF EXAMPLE.***

Input Table:
{{{input_table}}}

Output:

"""

fewshots_template = """Input Table:
{{{input_table}}}

Output:
{{{output}}}

"""


dataset_config = {
    "task": "Data-Imputation",
    "version": "1.0_sample200_markdown_3shot",
    "tag": ["1.0_sample200_markdown_3shot"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Data-Imputation/sample200-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": MarkdownSerializer
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
                    "reader": "pandas",
                    "serializer": MarkdownSerializer
                },
                "output": {
                    "type": "text",
                    "name": "output"
                },
            }
        }
    }
}
