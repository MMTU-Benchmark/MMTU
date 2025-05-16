from utils.table_serializer import CSVSerializer

prompt_template = """Within the following table, there is a specific value that is unique: "{{{needle_value}}}". 

Your task is to identify its exact position in the table. Please provide both the row index and column name where this value appears. Return the answer in JSON format: {"row": <row-index>, "column": "<column-name>"}

Table:
{{{table}}}

"""


dataset_config = {
    "task": "Table-needle-in-a-haystack",
    "version": "0.7_csv",
    "tag": "0.7_tniah_csv",
    "note": "use the Table-Locate v0.4 data. 50*50 unique values table.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Table-needle-in-a-haystack/benchmark8",
    "info": "info.json",
    "fields": {
        "table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas.str",
            "serializer": CSVSerializer,
            "name": "table"
        },
        "needle_value": {
            "type": "text",
            "name": "needle_value"
        },
    }
}

