from utils.table_serializer import MarkdownSerializerFloatTenDecimalPlaces

prompt_template = """Within the following table, there is a specific value that is unique: "{{{needle_value}}}". 

Your task is to identify its exact position in the table. Please provide both the row index and column name where this value appears. Return the answer in JSON format: {"row": <row-index>, "column": "<column-name>"}

Table:
{{{table}}}

"""


dataset_config = {
    "task": "Table-needle-in-a-haystack",
    "version": "1.0_sample1000_markdown",
    "tag": "1.0_sample1000_markdown",
    "note": "use the Table-Locate v0.4 data. 50*50 unique values table.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Table-needle-in-a-haystack/sample1000/benchmark8",
    "info": "info.json",
    "fields": {
        "table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas.str",
            "serializer": MarkdownSerializerFloatTenDecimalPlaces,
            "name": "table"
        },
        "needle_value": {
            "type": "text",
            "name": "needle_value"
        },
    }
}

