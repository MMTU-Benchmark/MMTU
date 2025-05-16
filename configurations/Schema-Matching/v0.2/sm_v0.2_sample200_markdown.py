from utils.table_serializer import MarkdownSerializer
from utils.table_processor import FirstNRowsProcessor

prompt_template = """Task: 
Please identify the matching columns between Table A and Table B. For each column in Table A, specify the corresponding column in Table B. If a column in A has no corresponding column in Table B, you can map it to null. Represent each column mapping using a pair of column headers in a list, i.e., [Table A Column, Table B column or null]. Provide the mapping for each column in Table A and return all mappings in a list.

No explanation and return the matching columns in a structured JSON format: {"column_mappings": <a list of column pairs>}.

TableA:
{{{tableA}}}

TableB:
{{{tableB}}}

"""


dataset_config = {
    "task": "Schema-Matching",
    "version": "0.2_sample200_markdown",
    "tag": ["0.2_sample200_markdown"],
    # "note": "Schema-Matching. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Schema-Matching/benchmark/sample200-3shots",
    "info": "info.json",
    "fields": {
        "tableA": {
            "type": "table.csv",
            "path": "source.csv",
            "reader": "pandas",
            "serializer": MarkdownSerializer,
            "processors": [FirstNRowsProcessor(n=10)],
            "name": "tableA"
        },
        "tableB": {
            "type": "table.csv",
            "path": "target.csv",
            "reader": "pandas",
            "serializer": MarkdownSerializer,
            "processors": [FirstNRowsProcessor(n=10)],
            "name": "tableB"
        }
    }
}

