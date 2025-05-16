from utils.table_serializer import MarkdownSerializer, MarkdownNoHeaderSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """Your task is to perform semantic data transformation on the given input column. You will be given a pair of example input/output columns. Then you will be given the input column for test, return the output table in JSON : {"output": [<output column>]}.

Eample Input Column:

{{{example_input}}}

Eample Output Column:
{{{example_output}}}

Test Input Column:
{{{test_input}}}

Return the output column in JSON : {"output": [<output column>]}.

Test Output Column:

"""


dataset_config = {
    "task": "semantic-transform",
    "version": "0.1_sample1000_markdown",
    "tag": "0.1_sample1000_markdown",
    # "note": "NL2SQL datasets multi-table. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/semantic-transform/sample1000",
    "info": "info.json",
    "fields": {
        "example_input": {
          "type": "table.csv", 
          "path": "example_input.txt",
          "reader": "pandas.no_header",
          "serializer": MarkdownNoHeaderSerializer,
        },
        "example_output": {
            "type": "table.csv", 
            "path": "example_groundtruth.txt",
            "reader": "pandas.no_header",
            "serializer": MarkdownNoHeaderSerializer,
        },
        "test_input": {
            "type": "table.csv",
            "path": "test_input.txt",
            "reader": "pandas.no_header",
            "serializer": MarkdownNoHeaderSerializer,
        }
    }
}
