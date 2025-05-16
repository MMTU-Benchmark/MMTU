from utils.table_serializer import MarkdownSerializer
from utils.table_processor import ShuffleRowsProcessor, ShuffleColumnsKeepFirstThreeProcessor

prompt_template = """Your task is to annotate a cell in a table, using the DBpedia resource URI that best describes the entity referenced in the cell.
 
No explanation, return the DBpedia entity in JSON format: {"DBpedia entity": "<DBpedia entity>"}. Please note that DBpedia entity URIs are in the format of "http://dbpedia.org/resource/<entity>".

Input Table:
{{{input_table}}}

Target cell located at row {{{row}}} and column {{{col_name}}}:
{{{cell}}}

"""


dataset_config = {
    "task": "Cell-entity-annotation",
    "version": "1.0_sample1000_markdown_table_permutation",
    "tag": ["1.0_sample1000_markdown_table_permutation"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Cell-entity-annotation/sample1000-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": MarkdownSerializer,
            "processors": [ShuffleColumnsKeepFirstThreeProcessor(), ShuffleRowsProcessor()],
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
        }
    }
}
