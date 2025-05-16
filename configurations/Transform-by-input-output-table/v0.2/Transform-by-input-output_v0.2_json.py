from utils.table_serializer import JsonSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are a data engineer tasked with creating a data transformation pipeline in Python using the pandas library.

Given input table(s) and a corresponding output table. Please write code that transforms the input table into the output table.

Input Table:

{{{inputs}}}

Output Table:
{{{output_table}}}

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
    "task": "Transform-by-input-output-table",
    "version": "0.2_sample1000_json",
    "tag": "0.2_sample1000_json",
    # "note": "NL2SQL datasets multi-table. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Transform-by-input-output-table/sample1000-3shots",
    "info": "info.json",
    "fields": {
        "inputs": {
            "type": "list",
            "template": table_template,
            "fields": {
                "idx": {
                    "type": "text",
                    "name": "idx"
                },
                "data": {
                    "type": "table.csv.path",
                    "reader": "pandas",
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
        "output_table": {
            "type": "table.csv",
            "reader": "pandas",
            "path": "output.csv",
            "serializer": JsonSerializer,
            "processors": [FirstNRowsProcessor(n=10)],
        },
    }
}
