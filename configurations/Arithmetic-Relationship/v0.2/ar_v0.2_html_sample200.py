from utils.table_serializer import HTMLSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are given a table with numerical values across multiple columns. Your task is to analyze the data and identify any underlying arithmetic relationships between the columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
{{{input_table}}}

"""


dataset_config = {
    "task": "Arithmetic-Relationship",
    "version": "0.2_sample200_html",
    "tag": ["0.2_sample200_html"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Arithmetic-Relationship/sample200-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": HTMLSerializer,
            # "processors": [FirstNRowsProcessor(50)],
        }
    }
}
