from utils.table_serializer import HTMLSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

***EXAMPLE:***

{{{fewshots}}}

***END OF EXAMPLE.***

**INPUT:**
Eample Input Column:

{{{example_input}}}

Eample Output Column:
{{{example_output}}}

Test Input Column:
{{{test_input}}}

**OUTPUT:**

"""

fewshots_template = """**INPUT:**
Eample Input Column:

{{{example_input}}}

Eample Output Column:
{{{example_output}}}

Test Input Column:
{{{test_input}}}

**OUTPUT:**
{{{output}}}

"""


dataset_config = {
    "task": "semantic-transform",
    "version": "0.3_sample1000_html_3shot",
    "tag": "0.3_sample1000_html_3shot",
    # "note": "NL2SQL datasets multi-table. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/semantic-transform/sample1000-3shots",
    "info": "info.json",
    "fields": {
        "example_input": {
          "type": "table.csv", 
          "path": "example_input.txt",
          "reader": "pandas",
          "serializer": HTMLSerializer,
        },
        "example_output": {
            "type": "table.csv", 
            "path": "example_groundtruth.txt",
            "reader": "pandas",
            "serializer": HTMLSerializer,
        },
        "test_input": {
            "type": "table.csv",
            "path": "test_input.txt",
            "reader": "pandas",
            "serializer": HTMLSerializer,
        },
        "fewshots": {
            "type": "fewshot",
            "path": "3shots",
            "info": "info.json",
            "template": fewshots_template,
            "fields": {
                "example_input": {
                "type": "table.csv", 
                "path": "example_input.txt",
                "reader": "pandas",
                "serializer": HTMLSerializer,
                },
                "example_output": {
                    "type": "table.csv", 
                    "path": "example_groundtruth.txt",
                    "reader": "pandas",
                    "serializer": HTMLSerializer,
                },
                "test_input": {
                    "type": "table.csv",
                    "path": "test_input.txt",
                    "reader": "pandas",
                    "serializer": HTMLSerializer,
                },
                "output": {
                    "type": "text",
                    "name": "output"
                },
            }
        }
    }
}
