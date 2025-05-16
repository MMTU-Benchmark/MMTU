from utils.table_serializer import JsonSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
{{{input_table}}}

"""


dataset_config = {
    "task": "Arithmetic-Relationship",
    "version": "1.0_sample200_json",
    "tag": ["1.0_sample200_json"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Arithmetic-Relationship/sample200-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": JsonSerializer,
            # "processors": [FirstNRowsProcessor(50)],
        }
    }
}
