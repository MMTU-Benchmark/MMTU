from utils.table_serializer import MarkdownSerializer, JsonSerializer

prompt_template = """Your task is to extract and return the value located at a specified row index and column name.

Input format:
- row_idx: An integer representing the row index (0-based).
- column name: A string representing the column name.
- Table: A table in Markdown format.

Output Format:
Return the value from the specified cell in JSON format: {"cell": <value>}

Input:

row_idx: {{{needle_row_idx}}}

column name: "{{{needle_col_name}}}"

Table:
{{{table}}}

"""


dataset_config = {
    "task": "Table-Locate-by-Row-Col",
    "version": "0.1_markdown",
    "tag": "0.1_table_locate_markdown",
    "note": "",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Table-needle-in-a-haystack/benchmark4",
    "info": "info.json",
    "fields": {
        "table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": MarkdownSerializer,
            "name": "table"
        },
        "needle_row_idx": {
            "type": "text",
            "name": "needle_row_idx"
        },
        "needle_col_name": {
            "type": "text",
            "name": "needle_col_name"
        },
    }
}

