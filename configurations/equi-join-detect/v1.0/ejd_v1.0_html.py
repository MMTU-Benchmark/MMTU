from utils.table_serializer import HTMLSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """Your are given a database with related tables used for business intelligence analysis. Your task is to identify all key/foreign-key join relationships between the tables for this database. Recall that a join is a relationship between two tables, that allows rows from one table to be combined with rows from another, based on a set of common join columns.
 
 
No explanation needed. Please return all join relationships in the following JSON format:
{
  "joins": [
    {
      "from_table": "table-1",
      "from_column": "column-1",
      "to_table": "table-2",
      "to_column": "column-3"
    }, 
	...
  ]
}

Tables:
{{{tables}}}
 
"""

table_template = """
Table: {{{name}}}
{{{data}}}
"""


dataset_config = {
    "task": "equi-join-detect",
    "version": "1.0_sample1000_html",
    "tag": ["1.0_sample1000_html"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/equi-join-detect/sample1000-3shots",
    "info": "info.json",
    "fields": {
        "tables": {
            "type": "list",
            "template": table_template,
            "fields": {
                "name": {
                    "type": "text",
                    "name": "name"
                },
                "data": {
                    "type": "table.csv.path",
                    "reader": "pandas",
                    "serializer": HTMLSerializer,
                    "processors": [FirstNRowsProcessor(n=10)],
                    "name": "data"
                }
            }
        },
    }
}
