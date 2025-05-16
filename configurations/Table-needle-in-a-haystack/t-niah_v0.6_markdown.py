from utils.table_serializer import MarkdownSerializer, JsonSerializer

prompt_template = """Within the following table, there is a specific value that is unique: "<T-NEEDLE>". 

Your task is to identify its exact position in the table. Please provide both the row index and column name where this value appears. Return the answer in JSON format: {"row": <row-index>, "column": "<column-name>"}

Table:
{{{table}}}

"""


dataset_config = {
    "task": "Table-needle-in-a-haystack",
    "version": "0.6_markdown",
    "tag": "0.6_tniah_markdown",
    "note": "random select a needle in upper-right 5*5 bin, then shift columns and rows of the table to put needle in a different position",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Table-needle-in-a-haystack/benchmark7",
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

