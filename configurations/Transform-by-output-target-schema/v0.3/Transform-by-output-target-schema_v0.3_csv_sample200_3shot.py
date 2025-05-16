from utils.table_serializer import CSVSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """Your task is to create a data transformation pipeline in Python using pandas libraries.

Given Source Tables below, and a Target Schema provided by users that demonstrates how the desired output table should look like schematically, please write Python pandas code that can transform the Source Tables into an output table, that matches the schema/structure given by the Target Schema.  Please note that the data values in the Target Schema are intended to represent the format and layout of the output table, but may not exactly match the actual data generated from the Source Tables when the python code is run on the Source Tables.

Use operations such as merge, groupby, pivot, apply, or any appropriate python or pandas steps. Your code should save the resulting DataFrame to a CSV file named 'output.csv'. Ensure that the code is executable and can be run directly as is, in a Python environment with pandas installed.

Return only the final code in markdown codeblock format, without any additional text or explanation. 

***EXAMPLE:***

{{{fewshots}}}

***END OF EXAMPLE.***

**INPUT:**
Source Tables:

{{{train}}}

Target Schema:
{{{target}}}

**OUTPUT:**
"""

fewshots_template = """**INPUT:**
Source Tables:

{{{train}}}

Target Schema:
{{{target}}}

**OUTPUT:**
{{{output}}}

"""

table_template = """
Table #{{{idx}}}
Filename: {{{filename}}}
Sample Rows in CSV:
{{{data}}}
"""


dataset_config = {
    "task": "Transform-by-output-target-schema",
    "version": "0.3_sample200_csv_3shot",
    "tag": "0.3_sample200_csv_3shot",
    # "note": "NL2SQL datasets multi-table. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Transform-by-output-target-schema/sample200-3shots",
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
        "target": {
            "type": "table.csv.path",
            "reader": "pandas.w_idx",
            "serializer": CSVSerializer,
            "processors": [FirstNRowsProcessor(n=10)],
            "name": "target"
        },
        "fewshots": {
            "type": "fewshot",
            "path": "3shots",
            "info": "info.json",
            "template": fewshots_template,
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
                "target": {
                    "type": "table.csv.path",
                    "reader": "pandas.w_idx",
                    "serializer": CSVSerializer,
                    "processors": [FirstNRowsProcessor(n=10)],
                    "name": "target"
                },
                "output": {
                    "type": "text",
                    "name": "output"
                },
            }
        }
    }
}
