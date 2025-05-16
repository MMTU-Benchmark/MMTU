from utils.table_serializer import MarkdownSerializer, MarkdownNoHeaderSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are given two input tables. Your task is to semantically join the entries from Table 1 with the most appropriate corresponding entries from Table 2, based on general world knowledge. Return the result as a JSON object with the key "output", where the value is a list of lists. Each inner list should contain one entry from Table 1 and its semantically matched entry from Table 2.

Input Table 1:
{{{input_1}}}

Input Table 2:
{{{input_2}}}

Joined Table:

"""


dataset_config = {
    "task": "semantic-join",
    "version": "0.1_sample1000_markdown",
    "tag": "0.1_sample1000_markdown",
    # "note": "NL2SQL datasets multi-table. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/semantic-join/sample1000",
    "info": "info.json",
    "fields": {
        "input_1": {
          "type": "table.csv", 
          "path": "input_1.csv",
          "reader": "pandas.no_header",
          "serializer": MarkdownNoHeaderSerializer,
        },
        "input_2": {
            "type": "table.csv", 
            "path": "input_2.csv",
            "reader": "pandas.no_header",
            "serializer": MarkdownNoHeaderSerializer,
        },
    }
}
