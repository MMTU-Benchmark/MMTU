from utils.table_serializer import CSVSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are given a table below, where some of the columns may be derived from other columns using string-based transformations (e.g., string split, concatenation, formatting, substring extraction, and pattern matching, etc.). 

Your task is to identify string transformation relationships between the columns, by determining if any column, henceforce referred to as a TargetColumn, can be derived from other columns, referred to as SourceColumns, using the string-based transformations. Please only return relationships that are semantically meaningful and truly hold, and do not return any relationships that are spurious. 

No explanation is needed, return all the detected relationships in the following JSON format: 
{
  "String-Relationship": [
    [["SourceColumn1", "SourceColumn2", ...], "TargetColumn"],
    ...
  ]
}

***EXAMPLE:***

{{{fewshots}}}

***END OF EXAMPLE.***

**INPUT:**
Input Table:
{{{input_table}}}

**OUTPUT:**

"""

fewshots_template = """**INPUT:**
Input Table:
{{{input_table}}}

**OUTPUT:**
{{{output}}}

"""


dataset_config = {
    "task": "String-Relationship",
    "version": "1.0_sample1000_csv_3shot",
    "tag": ["1.0_sample1000_csv_3shot"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/String-Relationship/sample1000-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": CSVSerializer,
            "processors": [FirstNRowsProcessor(50)],
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
                    "serializer": CSVSerializer,
                    "processors": [FirstNRowsProcessor(50)],
                },
                "output": {
                    "type": "text",
                    "name": "output"
                },
            }
        }
    }
}
