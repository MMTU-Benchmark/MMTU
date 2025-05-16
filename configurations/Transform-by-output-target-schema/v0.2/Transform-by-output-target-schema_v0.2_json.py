from utils.table_serializer import JsonSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are a data engineer tasked with creating a data transformation pipeline in Python using the pandas library.

Given the following:

Source Tables:

{{{train}}}

Target Schema:
{{{target}}}

Task:
Write a Python function or script using pandas that transforms the given input table(s) into the desired target table structure. Use operations such as merge, groupby, pivot, apply, or any appropriate pandas functions. Include comments explaining each step. 

Read all source tables with option `index_col=0`.

Return only the final code in markdown codeblock format, without any additional text or explanation. Finally, save the resulting DataFrame to a CSV file named 'output.csv'.

The code should be well-structured and easy to understand. Ensure that the code is executable and can be run in a Python environment with pandas installed.

"""

table_template = """
Table #{{{idx}}}
Filename: {{{filename}}}
Sample Rows in JSON:
{{{data}}}
"""


dataset_config = {
    "task": "Transform-by-output-target-schema",
    "version": "0.2_sample1000_json",
    "tag": "0.2_sample1000_json",
    # "note": "NL2SQL datasets multi-table. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Transform-by-output-target-schema/sample1000-3shots",
    "info": "info.json",
    "fields": {
        "train": {
            "type": "list",
            "template": table_template,
            "fields": {
                "idx": {
                    "type": "text",
                    "name": "idx"
                },
                "data": {
                    "type": "table.csv.path",
                    "reader": "pandas.w_idx",
                    "serializer": JsonSerializer,
                    "processors": [FirstNRowsProcessor(n=10)],
                    "name": "data"
                },
                "filename": {
                    "type": "text",
                    "name": "data"
                }
            }
        },
        "target": {
            "type": "table.csv.path",
            "reader": "pandas.w_idx",
            "serializer": JsonSerializer,
            "processors": [FirstNRowsProcessor(n=10)],
            "name": "target"
        }
    }
}
