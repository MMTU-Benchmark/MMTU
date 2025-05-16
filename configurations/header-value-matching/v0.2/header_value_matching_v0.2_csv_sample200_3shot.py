from utils.table_serializer import CSVSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """Given the input table data and the list of candidate headers, please determine the most suitable column header for each column in the table. Please only choose column headers from the candidate list. Please only return the most suitable column header for each column. Return the chosen column headers in a list. Do not return the entire table. No explanation and return your answer in JSON format: {"column_headers": "<a list of headers for each column chosen from the candidate list>"}.

***EXAMPLE:***

{{{fewshots}}}

***END OF EXAMPLE.***

**INPUT:**
Table Data:
{{{table_data}}}

Candidate column headers:
{{{candidate_headers}}}

**OUTPUT:**

"""

fewshots_template = """**INPUT:**
Table Data:
{{{table_data}}}

Candidate column headers:
{{{candidate_headers}}}

**OUTPUT:**
{{{output}}}

"""


dataset_config = {
    "task": "header-value-matching",
    "version": "0.2_sample200_csv_3shot",
    "tag": "0.2_sample200_csv_3shot",
    # "note": "NL2SQL datasets multi-table. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/header-value-matching/sample200-3shots",
    "info": "info.json",
    "fields": {
        "table_data": {
          "type": "table.csv", 
          "path": "data.csv",
          "reader": "pandas",
          "serializer": CSVSerializer,
        },
        "candidate_headers": {
            "type": "text", 
            "name": "headers"
        },
        "fewshots": {
            "type": "fewshot",
            "path": "3shots",
            "info": "info.json",
            "template": fewshots_template,
            "fields": {
                "table_data": {
                "type": "table.csv", 
                "path": "data.csv",
                "reader": "pandas",
                "serializer": CSVSerializer,
                },
                "candidate_headers": {
                    "type": "text", 
                    "name": "headers"
                },
                "output": {
                    "type": "text",
                    "name": "output"
                },
            }
        }
    }
}
