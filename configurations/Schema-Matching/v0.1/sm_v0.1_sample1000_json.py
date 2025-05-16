from utils.table_serializer import JsonSerializer
from utils.table_processor import FirstNRowsProcessor

prompt_template = """Task: 
Please identify the matching columns between Table A and Table B. For each column in Table A, specify the corresponding column in Table B. If a column in A has no corresponding column in Table B, you can map it to None. Represent each column mapping using a pair of column headers in a list, i.e., [Table A Column, Table B column or None]. Provide the mapping for each column in Table A and return all mappings in a list.

Return the matching columns in a structured JSON format: {"column_mappings": <a list of column pairs>}.

TableA:
{{{tableA}}}

TableB:
{{{tableB}}}

"""


dataset_config = {
    "task": "Schema-Matching",
    "version": "0.1_sample1000_json",
    "tag": ["0.1_sample1000_json"],
    "note": "Schema-Matching. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Schema-Matching/benchmark/sample1000",
    "info": "info.json",
    "fields": {
        "tableA": {
            "type": "table.csv",
            "path": "source.csv",
            "reader": "pandas",
            "serializer": JsonSerializer,
            "processors": [FirstNRowsProcessor(n=200)],
            "name": "tableA"
        },
        "tableB": {
            "type": "table.csv",
            "path": "target.csv",
            "reader": "pandas",
            "serializer": JsonSerializer,
            "processors": [FirstNRowsProcessor(n=200)],
            "name": "tableB"
        }
    }
}

