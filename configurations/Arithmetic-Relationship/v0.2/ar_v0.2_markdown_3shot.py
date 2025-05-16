from utils.table_serializer import MarkdownSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are given a table with numerical values across multiple columns. Your task is to analyze the data and identify any underlying arithmetic relationships between the columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

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
    "task": "Arithmetic-Relationship",
    "version": "0.2_sample1000_markdown_3shot",
    "tag": ["0.2_sample1000_markdown_3shot"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Arithmetic-Relationship/sample1000-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": MarkdownSerializer,
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
                    "serializer": MarkdownSerializer
                },
                "output": {
                    "type": "text",
                    "name": "output"
                },
            }
        }
    }
}
