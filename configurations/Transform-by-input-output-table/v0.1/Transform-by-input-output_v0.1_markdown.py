from utils.table_serializer import MarkdownSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are a data engineer tasked with creating a data transformation pipeline in Python using the pandas library.

Given input table(s) and a corresponding output table. Please write code that transforms the input table into the output table.

Input Table:

{{{inputs}}}

Output Table:
{{{output}}}

Return only the final code in markdown format, without any additional text or explanation. Finally, save the resulting DataFrame to a CSV file named 'output.csv'.

The code should be well-structured and easy to understand. Ensure that the code is executable and can be run in a Python environment with pandas installed.

"""

table_template = """
Table #{{{idx}}}
Filename: {{{filename}}}
Sample Rows in Markdown:
{{{data}}}
"""


dataset_config = {
    "task": "Transform-by-input-output-table",
    "version": "0.1_sample1000_markdown",
    "tag": "0.1_sample1000_markdown",
    # "note": "NL2SQL datasets multi-table. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Transform-by-input-output-table/sample1000",
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
                    "serializer": MarkdownSerializer,
                    "processors": [FirstNRowsProcessor(n=10)],
                    "name": "data"
                },
                "filename": {
                    "type": "text",
                    "name": "data"
                }
            }
        },
        "output": {
            "type": "table.csv.path",
            "reader": "pandas",
            "serializer": MarkdownSerializer,
            "processors": [FirstNRowsProcessor(n=10)],
            "name": "output"
        }
    }
}
