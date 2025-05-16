from utils.table_serializer import JsonSerializer

prompt_template = """Your task is to extract and return the cell located at a specified row index and column name.

Input format:
- row_idx: An integer representing the row index (0-based).
- column name: A string representing the column name.
- Table: A table in JSON format.

Output Format:
Return the exact cell value in JSON format: {"cell": <cell>}. For string values, return the string as it is. For numerical values, return the number as it is, do not round or format the number.
Do not explain, return the JSON object directly. 

Input:

row_idx: {{{needle_row_idx}}}

column name: "{{{needle_col_name}}}"

Table:
{{{table}}}

Output:
"""


dataset_config = {
    "task": "Table-Locate-by-Row-Col",
    "version": "0.4_json",
    "tag": "0.4_table_locate_json",
    "note": "",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Table-Locate-by-Row-Col/benchmark4",
    "info": "info.json",
    "fields": {
        "table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas.str",
            "serializer": JsonSerializer,
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

