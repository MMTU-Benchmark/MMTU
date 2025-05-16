from utils.table_serializer import HTMLSerializer

prompt_template = """Task: 
You are given a column of data from a table. Your job is to examine each value in the column and detect if there is any obvious error in the data. An error can be anything that seems out of place, such as formatting issues, inconsistent values, or data that doesn't align with the expected type or pattern.

If you detect an obvious error, return a JSON object, {"obvious_error": "<CELL>"}, with the key "obvious_error" and the value being the problematic cell. If you detect no error in the data, return {"obvious_error": null}.

Column:
{{{table}}}
"""


dataset_config = {
    "task": "Error-Detect",
    "version": "0.1_sample1000_html",
    "tag": ["0.1_sample1000_html", "0.1_sample1000_html_gpt35"],
    "note": "Error-Detect. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Error-Detect/benchmark/sample1000",
    "info": "info.json",
    "fields": {
        "table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": HTMLSerializer,
            "name": "table"
        }
    }
}

