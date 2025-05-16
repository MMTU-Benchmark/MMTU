from utils.table_serializer import JsonSerializer
from utils.table_processor import FirstNRowsProcessor

prompt_template = """Task: 
Please identify the matching columns between Table A and Table B. For each column in Table A, specify the corresponding column in Table B. If a column in A has no corresponding column in Table B, you can map it to null. Represent each column mapping using a pair of column headers in a list, i.e., [Table A Column, Table B column or null]. Provide the mapping for each column in Table A and return all mappings in a list.

No explanation and return the matching columns in a structured JSON format: {"column_mappings": <a list of column pairs>}.

***EXAMPLE:***

{{{fewshots}}}

***END OF EXAMPLE.***

**INPUT:**
TableA:
{{{tableA}}}

TableB:
{{{tableB}}}

**OUTPUT:**

"""

fewshots_template = """**INPUT:**
TableA:
{{{tableA}}}

TableB:
{{{tableB}}}

**OUTPUT:**
{{{output}}}

"""


dataset_config = {
    "task": "Schema-Matching",
    "version": "1.0_sample200_json_3shot",
    "tag": ["1.0_sample200_json_3shot"],
    # "note": "Schema-Matching. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Schema-Matching/benchmark/sample200-3shots",
    "info": "info.json",
    "fields": {
        "tableA": {
            "type": "table.csv",
            "path": "source.csv",
            "reader": "pandas",
            "serializer": JsonSerializer,
            "processors": [FirstNRowsProcessor(n=10)],
            "name": "tableA"
        },
        "tableB": {
            "type": "table.csv",
            "path": "target.csv",
            "reader": "pandas",
            "serializer": JsonSerializer,
            "processors": [FirstNRowsProcessor(n=10)],
            "name": "tableB"
        },
        "fewshots": {
            "type": "fewshot",
            "path": "3shots",
            "info": "info.json",
            "template": fewshots_template,
            "fields": {
                "tableA": {
                "type": "table.csv",
                "path": "source.csv",
                "reader": "pandas",
                "serializer": JsonSerializer,
                "processors": [FirstNRowsProcessor(n=10)],
                "name": "tableA"
            },
            "tableB": {
                "type": "table.csv",
                "path": "target.csv",
                "reader": "pandas",
                "serializer": JsonSerializer,
                "processors": [FirstNRowsProcessor(n=10)],
                "name": "tableB"
            },
                "output": {
                    "type": "text",
                    "name": "output"
                },
            }
        }
    }
}

