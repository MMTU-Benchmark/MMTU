from utils.table_serializer import MarkdownSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor
from utils.table_processor import ShuffleRowsProcessor, ShuffleColumnsKeepFirstThreeProcessor

prompt_template = """Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
{{{input_table}}}

"""


dataset_config = {
    "task": "Functional-Dependency",
    "version": "1.0_sample200_markdown_table_permutation",
    "tag": ["1.0_sample200_markdown_table_permutation"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Functional-Dependency/sample200-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": MarkdownSerializer,
            "processors": [ShuffleRowsProcessor(), FirstNRowsProcessor(50), ShuffleColumnsKeepFirstThreeProcessor(), ShuffleRowsProcessor(seed=1)],
        }
    }
}
