from utils.table_serializer import JsonSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are given two data records from two datasets that may refer to the same real-world entity. Each record consists of multiple attributes, such as name, address, and other identifying details. Your goal is to determine whether pairs of records refer to the same entity (match) or different entities (non-match).

No explanation and return the final answer as a JSON object, {"label": "<LABEL>"}, where "<LABEL>" is either "match" or "non-match".

***EXAMPLE:***

{{{fewshots}}}

***END OF EXAMPLE.***

**INPUT:**
Entity A:
{{{entityA}}}

Entity B:
{{{entityB}}}

**OUTPUT:**

"""

fewshots_template = """**INPUT:**
Entity A:
{{{entityA}}}

Entity B:
{{{entityB}}}

**OUTPUT:**
{{{output}}}

"""


dataset_config = {
    "task": "Entity-Matching",
    "version": "1.0_sample1000_json_3shot",
    "tag": ["1.0_sample1000_json_3shot"],
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Entity-Matching/sample1000-3shots",
    "info": "info.json",
    "fields": {
        "entityA": {
            "type": "table.csv",
            "path": "entityA.csv",
            "reader": "pandas",
            "serializer": JsonSerializer
        },
        "entityB": {
            "type": "table.csv",
            "path": "entityB.csv",
            "reader": "pandas",
            "serializer": JsonSerializer
        },
        "fewshots": {
            "type": "fewshot",
            "path": "3shots",
            "info": "info.json",
            "template": fewshots_template,
            "fields": {
                "entityA": {
                    "type": "table.csv",
                    "path": "entityA.csv",
                    "reader": "pandas",
                    "serializer": JsonSerializer
                },
                "entityB": {
                    "type": "table.csv",
                    "path": "entityB.csv",
                    "reader": "pandas",
                    "serializer": JsonSerializer
                },
                "output": {
                    "type": "text",
                    "name": "output"
                },
            }
        }
    },
}
