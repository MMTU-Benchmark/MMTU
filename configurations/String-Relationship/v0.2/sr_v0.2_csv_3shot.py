from utils.table_serializer import CSVSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are given a tabular dataset where each row represents a data instance, and each column contains either numerical, categorical, textual, or date/time values. Among these columns, there exists a set of columns that are derived or transformed from other columns via a string transformation relationship (e.g., concatenation, formatting, substring extraction, pattern mapping, etc.).

Task:
Identify and extract the string transformation relationships between columns. 

Specifically, determine if one or more columns are derived from others through some form of string-based operation. Focus on identifying patterns such as:

Concatenation of multiple columns
Substring extraction
Joining values with delimiters

No explanation, return all the detected relationships in the following JSON format: 
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
    "version": "0.2_sample1000_csv_3shot",
    "tag": ["0.2_sample1000_csv_3shot"],
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
