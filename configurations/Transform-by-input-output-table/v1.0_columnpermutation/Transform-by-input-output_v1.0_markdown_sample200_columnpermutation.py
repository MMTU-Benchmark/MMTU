from utils.table_serializer import MarkdownSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor
from utils.table_processor import ShuffleRowsProcessor, ShuffleColumnsKeepFirstThreeProcessor

prompt_template = """Your task is to create a data transformation pipeline in Python using pandas libraries.

Given input table(s) and a corresponding output table below, please write Python pandas code that can transform the input table into the given output table. Your code should save the resulting DataFrame to a CSV file named 'output.csv'. Ensure that the code is executable and can be run directly as is, in a Python environment with pandas installed.

Input Table:

{{{inputs}}}

Output Table:
{{{output_table}}}

Return only the final code in markdown codeblock format, without any additional text or explanation. 

"""

table_template = """
Table #{{{idx}}}
Filename: {{{filename}}}
Sample Rows in Markdown:
{{{data}}}
"""


dataset_config = {
    "task": "Transform-by-input-output-table",
    "version": "1.0_sample200_markdown_columnpermutation",
    "tag": "1.0_sample200_markdown_columnpermutation",
    # "note": "NL2SQL datasets multi-table. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Transform-by-input-output-table/sample200-3shots",
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
                    "processors": [FirstNRowsProcessor(n=10), ShuffleColumnsKeepFirstThreeProcessor()],
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
            "serializer": MarkdownSerializer,
            "processors": [FirstNRowsProcessor(n=10), ShuffleColumnsKeepFirstThreeProcessor()],
        },
    }
}
