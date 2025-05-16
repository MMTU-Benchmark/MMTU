from utils.table_serializer import CSVSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are given a input table where each row is an input record, and an output table that contains one additional column, called "Output", whose values in each row can be produced by transforming values of the same row in the input table. Your task is to write the corresponding code that can perform such transformations, based on the given input-output examples. Make sure that the transformations you write can generalize to additional input examples not shown in the input table.

Implementation Details:
1. Generate Python code using the Pandas library to perform the transformation.
2. The code should read the input table from "input.csv".
3. Apply the transformation based on the observed pattern.
4. Save the transformed output to "output.csv".
5. Ensure that the output structure matches the expected format, including column names and data types.

Your task is to ensure that the Python script is correctly formatted, efficient, and ready for execution on any dataset following the same transformation pattern.

No explanation and return the Python code in a markdown code block: ```python\n<PYTHON-CODE>\n```.

***EXAMPLE:***

{{{fewshots}}}

***END OF EXAMPLE.***

**INPUT:**
Input Table:
{{{input_table}}}

Output Table:
{{{output_table}}}

**OUTPUT:**

"""

fewshots_template = """**INPUT:**
Input Table:
{{{input_table}}}

Output Table:
{{{output_table}}}

**OUTPUT:**
{{{output}}}

"""


dataset_config = {
    "task": "Data-transform-pbe",
    "version": "1.0_sample200_csv_3shot",
    "tag": ["1.0_sample200_csv_3shot"],
    # "note": "NL2SQL datasets multi-table. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Data-transform-pbe/sample200-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "example_input.csv",
            "reader": "pandas",
            "serializer": CSVSerializer
        },
        "output_table": {
            "type": "table.csv",
            "path": "example_output.csv",
            "reader": "pandas",
            "serializer": CSVSerializer
        },
        "fewshots": {
            "type": "fewshot",
            "path": "3shots",
            "info": "info.json",
            "template": fewshots_template,
            "fields": {
                "input_table": {
                    "type": "table.csv",
                    "path": "example_input.csv",
                    "reader": "pandas",
                    "serializer": CSVSerializer
                },
                "output_table": {
                    "type": "table.csv",
                    "path": "example_output.csv",
                    "reader": "pandas",
                    "serializer": CSVSerializer
                },
                "output": {
                    "type": "text",
                    "name": "output"
                },
            }
        }
    }
}
