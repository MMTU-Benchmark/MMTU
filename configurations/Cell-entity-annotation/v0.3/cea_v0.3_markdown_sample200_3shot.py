from utils.table_serializer import MarkdownSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """Your task is to annotate a cell in a table, using the DBpedia resource URI that best describes the entity referenced in the cell.
 
No explanation, return the DBpedia entity in JSON format: {"DBpedia entity": "<DBpedia entity>"}. Please note that DBpedia entity URIs are in the format of "http://dbpedia.org/resource/<entity>".

***EXAMPLE:***

{{{fewshots}}}

***END OF EXAMPLE.***

**INPUT:**
Input Table:
{{{input_table}}}

Target cell located at row {{{row}}} and column {{{col_name}}}:
{{{cell}}}

**OUTPUT:**
"""

fewshots_template = """**INPUT:**
Input Table:
{{{input_table}}}

Target cell located at row {{{row}}} and column {{{col_name}}}:
{{{cell}}}

**OUTPUT:**
{{{output}}}

"""


dataset_config = {
    "task": "Cell-entity-annotation",
    "version": "0.3_sample200_markdown_3shot",
    "tag": ["0.3_sample200_markdown_3shot"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Cell-entity-annotation/sample200-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": MarkdownSerializer
        },
        "row": {
            "type": "text",
            "name": "row_id"
        },
        "col_name": {
            "type": "text",
            "name": "col_name"
        },
        "cell": {
            "type": "text",
            "name": "cell_value"
        },
        "fewshots": {
            "type": "fewshot",
            "path": "3shots",
            "info": "info.json",
            "template": fewshots_template,
            "fields": {
                "input_table": {
                    "type": "table.csv",
                    "path": "data.csv",
                    "reader": "pandas",
                    "serializer": MarkdownSerializer
                },
                "row": {
                    "type": "text",
                    "name": "row_id"
                },
                "col_name": {
                    "type": "text",
                    "name": "col_name"
                },
                "cell": {
                    "type": "text",
                    "name": "cell_value"
                },
                "output": {
                    "type": "text",
                    "name": "output"
                },
            }
        }
    }
}
