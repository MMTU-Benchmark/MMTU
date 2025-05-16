from utils.table_serializer import HTMLSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are a data analysis assistant. Given a relational table represented in CSV format, your task is to determine the functional dependencies present in the data. A functional dependency is a relationship where the value of one attribute (or a set of attributes) uniquely determines the value of another attribute.

Instructions:
Analyze the provided table.
Identify all functional dependencies that are evident from the data.
No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
{{{input_table}}}

"""


dataset_config = {
    "task": "Functional-Dependency",
    "version": "0.2_sample1000_html",
    "tag": ["0.2_sample1000_html"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Functional-Dependency/sample1000-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": HTMLSerializer,
            "processors": [ShuffleRowsProcessor(), FirstNRowsProcessor(50)],
        }
    }
}
