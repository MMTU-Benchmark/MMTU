from utils.table_serializer import MarkdownSerializer, MarkdownNoHeaderSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are given a input table where each row represents an input data point, and an output table that can be produced by applying data transformation on the input table. Your task is to transform the data according to the pattern demonstrated in the provided input-output examples. The transformation should be applied systematically across all rows to ensure consistency.

Requirements:
1. Identify the transformation logic based on the given input-output mappings.
2. Apply the same transformation to all similar inputs.
3. Ensure that the output structure matches the expected format, including column names and data types.

Implementation Details:
1. Generate Python code using the Pandas library to perform the transformation.
2. The code should read the input table from "input.csv".
3. Apply the transformation based on the observed pattern.
4. Save the transformed output to "output.csv".

Your task is to ensure that the Python script is correctly formatted, efficient, and ready for execution on any dataset following the same transformation pattern.

Return the Python code in a markdown code block: ```python\n<PYTHON-CODE>\n```.

Input Table:
{{{input_table}}}

Output Table:
{{{output_table}}}

"""


dataset_config = {
    "task": "Data-transform-pbe",
    "version": "0.1_sample1000_markdown",
    "tag": ["0.1_sample1000_markdown", "0.1_sample1000_markdown_gpt35"],
    # "note": "NL2SQL datasets multi-table. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Data-transform-pbe/sample1000",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "example_input.csv",
            "reader": "pandas",
            "serializer": MarkdownSerializer
        },
        "output_table": {
            "type": "table.csv",
            "path": "example_output.csv",
            "reader": "pandas",
            "serializer": MarkdownSerializer
        },
    },
    "foofah_fields": {
        "input_table": {
            "type": "table.csv",
            "path": "example_input.csv",
            "reader": "pandas.no_header",
            "serializer": MarkdownNoHeaderSerializer
        },
        "output_table": {
            "type": "table.csv",
            "path": "example_output.csv",
            "reader": "pandas.no_header",
            "serializer": MarkdownNoHeaderSerializer
        },
    }
}
