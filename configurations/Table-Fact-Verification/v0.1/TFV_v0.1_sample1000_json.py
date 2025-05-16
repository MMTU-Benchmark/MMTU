from utils.table_serializer import MarkdownSerializer, JsonSerializer

prompt_template = """Task: 
You are given a table that contains structured data, along with a caption describing the table. Additionally, you will be provided with a statement. Your task is to verify whether the statement is entailed by the information in the table or refuted by it. You need to return your final answer in JSON format, {"label" : <label>}, with the label "ENTAILED" if the statement is supported by the table, or "REFUTED" if it contradicts the table. 

Table Caption:
{{{table_caption}}}

Table:
{{{table}}}

Statement:
{{{statement}}}
"""


dataset_config = {
    "task": "Table-Fact-Verification",
    "version": "0.1_sample1000_json",
    "tag": ["0.1_sample1000_json", "0.1_sample1000_json_gpt35"],
    "note": "Table-Fact-Verification. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Table-Fact-Verification/benchmark/sample1000",
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

