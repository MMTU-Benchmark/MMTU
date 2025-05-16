from utils.table_serializer import CSVSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are given two data records from two datasets that may refer to the same real-world entity. Each record consists of multiple attributes, such as name, address, and other identifying details. Your goal is to determine whether pairs of records refer to the same entity (match) or different entities (non-match).

Return the final answer as a JSON object, {"label": "<LABEL>"}, where "<LABEL>" is either "match" or "non-match".

Entity A:
{{{entityA}}}

Entity B:
{{{entityB}}}

"""


dataset_config = {
    "task": "Entity-Matching",
    "version": "0.1_sample1000_csv",
    "tag": ["0.1_sample1000_csv", "0.1_sample1000_csv_gpt35"],
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Entity-Matching/sample1000",
    "info": "info.json",
    "fields": {
        "entityA": {
            "type": "table.csv",
            "path": "entityA.csv",
            "reader": "pandas",
            "serializer": CSVSerializer
        },
        "entityB": {
            "type": "table.csv",
            "path": "entityB.csv",
            "reader": "pandas",
            "serializer": CSVSerializer
        },
    },
}
