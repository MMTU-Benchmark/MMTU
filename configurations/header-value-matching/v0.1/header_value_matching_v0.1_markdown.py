from utils.table_serializer import MarkdownSerializer, MarkdownNoHeaderSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """Given the input table data and the list of candidate headers, please determine the most suitable column header for each column in the table. Please only choose column headers from the candidate list. Please only return the most suitable column header for each column. Return the chosen column headers in a list. Do not return the entire table. Return the final result as JSON in the format {"column_headers": "<a list of headers for each column chosen from the candidate list>"}.

Table Data:
{{{table_data}}}

Candidate column headers:
{{{candidate_headers}}}

"""


dataset_config = {
    "task": "header-value-matching",
    "version": "0.1_sample1000_markdown",
    "tag": "0.1_sample1000_markdown",
    # "note": "NL2SQL datasets multi-table. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/header-value-matching/sample1000",
    "info": "info.json",
    "fields": {
        "table_data": {
          "type": "table.csv", 
          "path": "data.csv",
          "reader": "pandas.no_header",
          "serializer": MarkdownNoHeaderSerializer,
        },
        "candidate_headers": {
            "type": "text", 
            "name": "headers"
        },
    }
}
