from utils.table_serializer import MarkdownSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """Your task is to create a data transformation pipeline in Python using pandas libraries.

Given input table(s) and a corresponding output table below, please write Python pandas code that can transform the input table into the given output table. Your code should save the resulting DataFrame to a CSV file named 'output.csv'. Ensure that the code is executable and can be run directly as is, in a Python environment with pandas installed.

Return only the final code in markdown codeblock format, without any additional text or explanation. 

***EXAMPLE:***

{{{fewshots}}}

***END OF EXAMPLE.***

**INPUT:**
Input Table:

{{{inputs}}}

Output Table:
{{{output_table}}}

**OUTPUT:**
"""

fewshots_template = """**INPUT:**
Input Table:

{{{inputs}}}

Output Table:
{{{output_table}}}

**OUTPUT:**
{{{gt_output}}}

"""

table_template = """
Table #{{{idx}}}
Filename: {{{filename}}}
Sample Rows in Markdown:
{{{data}}}
"""


dataset_config = {
    "task": "Transform-by-input-output-table",
    "version": "0.3_sample1000_markdown_3shot",
    "tag": "0.3_sample1000_markdown_3shot",
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
        "output_table": {
            "type": "table.csv",
            "reader": "pandas",
            "path": "output.csv",
            "serializer": MarkdownSerializer,
            "processors": [FirstNRowsProcessor(n=10)],
        },
        "fewshots": {
            "type": "fewshot",
            "path": "3shots",
            "info": "info.json",
            "template": fewshots_template,
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
                "output_table": {
                    "type": "table.csv",
                    "reader": "pandas",
                    "path": "output.csv",
                    "serializer": MarkdownSerializer,
                    "processors": [FirstNRowsProcessor(n=10)],
                },
                "gt_output": {
                    "type": "text",
                    "name": "output"
                },
            }
        }
    }
}
