from utils.table_serializer import MarkdownSerializer, JsonSerializer

prompt_template = """Within the following table, there is a specific value that is unique: "<T-NEEDLE>". 

Your task is to identify its exact position in the table. Please provide both the row index and column name where this value appears. Return the answer in JSON format: {"row": <row-index>, "column": "<column-name>"}

Table:
{{{table}}}

"""


dataset_config = {
    "task": "Table-needle-in-a-haystack",
    "version": "0.2_markdown",
    "tag": "0.2_tniah_markdown",
    "note": "",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Table-needle-in-a-haystack/benchmark2",
    "info": "info.json",
    "fields": {
        "table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": MarkdownSerializer,
            "name": "table"
        }
    }
}

