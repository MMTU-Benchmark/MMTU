from utils.table_serializer import JsonSerializer

prompt_template = """Task: 
You are given a table that contains structured data, along with a caption describing the table. Additionally, you will be provided with a statement. Your task is to verify whether the statement is entailed by the information in the table or refuted by it. You need to return your final answer in JSON format, {"label" : <label>}, with the label "ENTAILED" if the statement is supported by the table, or "REFUTED" if it contradicts the table. No explanation is needed.

Table Caption:
{{{table_caption}}}

Table:
{{{table}}}

Statement:
{{{statement}}}
"""


dataset_config = {
    "task": "Table-Fact-Verification",
    "version": "1.0_sample200_json",
    "tag": ["1.0_sample200_json"],
    "note": "Table-Fact-Verification. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Table-Fact-Verification/benchmark/sample200-3shots",
    "info": "info.json",
    "fields": {
        "table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": JsonSerializer,
            "name": "table"
        },
        "statement": {
            "type": "text",
            "name": "statement"
        },
        "table_caption": {
            "type": "text",
            "name": "table_caption"
        }
    }
}

