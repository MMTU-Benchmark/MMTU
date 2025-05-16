from utils.table_serializer import MarkdownSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """Your task is to perform semantic data transformation on the given input column. You will be given a pair of example input/output columns. Then you will be given the input column for test, no explanation, no code and return your answer in JSON : {"output": [<output column>]}.


Eample Input Column:

{{{example_input}}}

Eample Output Column:
{{{example_output}}}

Test Input Column:
{{{test_input}}}

"""


dataset_config = {
    "task": "semantic-transform",
    "version": "0.2_sample200_markdown",
    "tag": "0.2_sample200_markdown",
    # "note": "NL2SQL datasets multi-table. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/semantic-transform/sample200-3shots",
    "info": "info.json",
    "fields": {
        "example_input": {
          "type": "table.csv", 
          "path": "example_input.txt",
          "reader": "pandas",
          "serializer": MarkdownSerializer,
        },
        "example_output": {
            "type": "table.csv", 
            "path": "example_groundtruth.txt",
            "reader": "pandas",
            "serializer": MarkdownSerializer,
        },
        "test_input": {
            "type": "table.csv",
            "path": "test_input.txt",
            "reader": "pandas",
            "serializer": MarkdownSerializer,
        }
    }
}
