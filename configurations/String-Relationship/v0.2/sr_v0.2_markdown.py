from utils.table_serializer import MarkdownSerializer
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


Input Table:
{{{input_table}}}

"""


dataset_config = {
    "task": "String-Relationship",
    "version": "0.2_sample1000_markdown",
    "tag": ["0.2_sample1000_markdown"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/String-Relationship/sample1000-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": MarkdownSerializer,
            "processors": [FirstNRowsProcessor(50)],
        }
    }
}
