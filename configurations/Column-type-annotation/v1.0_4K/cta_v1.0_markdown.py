from utils.table_serializer import MarkdownSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """Your task is to annotate the target entity column in the input table with the DBPedia ontology that can most accurately describe all entities in the column (i.e. use the most fine grained ontology class name that can describe all entities in the column).

No explanation, return the ontology class in JSON format: {"DBpedia ontology class": "<DBpedia ontology class>"}. Please note that DBpedia ontology classes are in the format of "http://dbpedia.org/ontology/<class_name>".

Input Table:
{{{input_table}}}

Target entity column: {{{target_entity_column}}}

"""


dataset_config = {
    "task": "Column-type-annotation",
    "version": "1.0_sample1000_markdown_4k",
    "tag": ["1.0_sample1000_markdown_4k"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Column-type-annotation/sample1000-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": MarkdownSerializer,
            "processors": [FirstNRowsProcessor(5)],
        },
        "target_entity_column": {
            "type": "text",
            "name": "col_name"
        }
    }
}
