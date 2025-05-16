from utils.table_serializer import CSVSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are a data engineer tasked with creating a data transformation pipeline in Python using the pandas library.

Given input table(s) and a corresponding output table. Please write code that transforms the input table into the output table.

Return only the final code in markdown codeblock format, without any additional text or explanation. Finally, save the resulting DataFrame to a CSV file named 'output.csv'.

The code should be well-structured and easy to understand. Ensure that the code is executable and can be run in a Python environment with pandas installed.

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
Sample Rows in CSV:
{{{data}}}
"""


dataset_config = {
    "task": "Transform-by-input-output-table",
    "version": "0.2_sample1000_csv_3shot",
    "tag": "0.2_sample1000_csv_3shot",
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
                    "serializer": CSVSerializer,
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
            "serializer": CSVSerializer,
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
                            "serializer": CSVSerializer,
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
                    "serializer": CSVSerializer,
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
