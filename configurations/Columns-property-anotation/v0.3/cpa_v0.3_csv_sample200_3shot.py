from utils.table_serializer import CSVSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You will be given a table, along with a head column and a tail column from the table. Your task is to annotate the semantic relationship between this pair of columns in the table, using a valid property name from the DBPedia Ontology, which always starts with the prefix of http://dbpedia.org/ontology/.
 
No explanation, return the ontology property in JSON format: {"DBpedia property": "<DBpedia property>"}. The annotation property should come with the prefix of http://dbpedia.org/ontology/.

***EXAMPLE:***

{{{fewshots}}}

***END OF EXAMPLE.***

**INPUT:**
Input table:
{{{input_table}}}

Head column: {{{head_col_name}}}

Tail column: {{{tail_col_name}}}

**OUTPUT:**
"""

fewshots_template = """**INPUT:**
Input table:
{{{input_table}}}

Head column: {{{head_col_name}}}

Tail column: {{{tail_col_name}}}

**OUTPUT:**
{{{output}}}

"""


dataset_config = {
    "task": "Columns-property-anotation",
    "version": "0.3_sample200_csv_3shot",
    "tag": ["0.3_sample200_csv_3shot"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Columns-property-anotation/sample200-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": CSVSerializer
        },
        "head_col_name": {
            "type": "text",
            "name": "col_a_name"
        },
        "tail_col_name": {
            "type": "text",
            "name": "col_b_name"
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
                    "serializer": CSVSerializer
                },
                "head_col_name": {
                    "type": "text",
                    "name": "col_a_name"
                },
                "tail_col_name": {
                    "type": "text",
                    "name": "col_b_name"
                },  
                "output": {
                    "type": "text",
                    "name": "output"
                },
            }
        }
    }
}
