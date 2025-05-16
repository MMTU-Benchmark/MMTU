from utils.table_serializer import HTMLSerializer

prompt_template = """Task: 
You are given a table that contains structured data, along with a caption describing the table. Additionally, you will be provided with a statement. Your task is to verify whether the statement is entailed by the information in the table or refuted by it. You need to return your final answer in JSON format, {"label" : <label>}, with the label "ENTAILED" if the statement is supported by the table, or "REFUTED" if it contradicts the table. No explanation is needed.

***EXAMPLE:***

{{{fewshots}}}

***END OF EXAMPLE.***

**INPUT:**

Table Caption:
{{{table_caption}}}

Table:
{{{table}}}

Statement:
{{{statement}}}

**OUTPUT:**

"""

fewshots_template = """**INPUT:**

Table Caption:
{{{table_caption}}}

Table:
{{{table}}}

Statement:
{{{statement}}}

**OUTPUT:**
{{{output}}}

"""


dataset_config = {
    "task": "Table-Fact-Verification",
    "version": "0.2_sample200_html_3shot",
    "tag": ["0.2_sample200_html_3shot"],
    "note": "Table-Fact-Verification. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Table-Fact-Verification/benchmark/sample200-3shots",
    "info": "info.json",
    "fields": {
        "table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": HTMLSerializer,
            "name": "table"
        },
        "statement": {
            "type": "text",
            "name": "statement"
        },
        "table_caption": {
            "type": "text",
            "name": "table_caption"
        },
        "fewshots": {
            "type": "fewshot",
            "path": "3shots",
            "info": "info.json",
            "template": fewshots_template,
            "fields": {
                "table": {
                    "type": "table.csv",
                    "path": "data.csv",
                    "reader": "pandas",
                    "serializer": HTMLSerializer,
                    "name": "table"
                },
                "statement": {
                    "type": "text",
                    "name": "statement"
                },
                "table_caption": {
                    "type": "text",
                    "name": "table_caption"
                },
                "output": {
                    "type": "text",
                    "name": "output"
                },
            }
        }
    }
}

