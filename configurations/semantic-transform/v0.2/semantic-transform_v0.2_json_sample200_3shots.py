from utils.table_serializer import JsonSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """Your task is to perform semantic data transformation on the given input column. You will be given a pair of example input/output columns. Then you will be given the input column for test, no explanation, no code and return your answer in JSON : {"output": [<output column>]}.

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
    "version": "0.2_sample200_json_3shot",
    "tag": "0.2_sample200_json_3shot",
    # "note": "NL2SQL datasets multi-table. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/semantic-transform/sample200-3shots",
    "info": "info.json",
    "fields": {
        "example_input": {
          "type": "table.csv", 
          "path": "example_input.txt",
          "reader": "pandas",
          "serializer": JsonSerializer,
        },
        "example_output": {
            "type": "table.csv", 
            "path": "example_groundtruth.txt",
            "reader": "pandas",
            "serializer": JsonSerializer,
        },
        "test_input": {
            "type": "table.csv",
            "path": "test_input.txt",
            "reader": "pandas",
            "serializer": JsonSerializer,
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
                "serializer": JsonSerializer,
                },
                "example_output": {
                    "type": "table.csv", 
                    "path": "example_groundtruth.txt",
                    "reader": "pandas",
                    "serializer": JsonSerializer,
                },
                "test_input": {
                    "type": "table.csv",
                    "path": "test_input.txt",
                    "reader": "pandas",
                    "serializer": JsonSerializer,
                },
                "output": {
                    "type": "text",
                    "name": "output"
                },
            }
        }
    }
}
