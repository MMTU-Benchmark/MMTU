from utils.table_serializer import MarkdownSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

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
    "task": "Functional-Dependency",
    "version": "0.3_sample1000_markdown_3shot",
    "tag": ["0.3_sample1000_markdown_3shot"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Functional-Dependency/sample1000-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": MarkdownSerializer,
            "processors": [ShuffleRowsProcessor(), FirstNRowsProcessor(50)],
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
                    "serializer": MarkdownSerializer,
                    "processors": [ShuffleRowsProcessor(), FirstNRowsProcessor(50)],
                },
                "output": {
                    "type": "text",
                    "name": "output"
                },
            }
        }
    }
}
