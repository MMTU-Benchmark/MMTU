from utils.table_serializer import JsonSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are given two input tables. Your task is to semantically join the entries from Table 1 with the most appropriate corresponding entries from Table 2, based on general world knowledge. No explanation and return your answer in JSON format: {"output": <answer>}, where the answer is a list of lists. Each inner list should contain one entry from Table 1 and its semantically matched entry from Table 2. No explanation is needed. 

***EXAMPLE:***

{{{fewshots}}}

***END OF EXAMPLE.***

**INPUT:**
Input Table 1:
{{{input_1}}}

Input Table 2:
{{{input_2}}}

***OUTPUT:**

"""

fewshots_template = """**INPUT:**
Input Table 1:
{{{input_1}}}

Input Table 2:
{{{input_2}}}

***OUTPUT:**
{{{output}}}

"""


dataset_config = {
    "task": "semantic-join",
    "version": "0.2_sample200_json_3shot",
    "tag": "0.2_sample200_json_3shot",
    # "note": "NL2SQL datasets multi-table. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/semantic-join/sample200-3shots",
    "info": "info.json",
    "fields": {
        "input_1": {
          "type": "table.csv", 
          "path": "input_1.csv",
          "reader": "pandas",
          "serializer": JsonSerializer,
        },
        "input_2": {
            "type": "table.csv", 
            "path": "input_2.csv",
            "reader": "pandas",
            "serializer": JsonSerializer,
        },
        "fewshots": {
            "type": "fewshot",
            "path": "3shots",
            "info": "info.json",
            "template": fewshots_template,
            "fields": {
                "input_1": {
                "type": "table.csv", 
                "path": "input_1.csv",
                "reader": "pandas",
                "serializer": JsonSerializer,
                },
                "input_2": {
                    "type": "table.csv", 
                    "path": "input_2.csv",
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
