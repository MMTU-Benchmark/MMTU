from utils.table_serializer import HTMLSerializer

prompt_template = """You are given two input tables below. Your task is to identify the most likely semantic relationships between values of these two columns, and then output pairs of values from Table 1 and Table 2, that can be joined/linked based on the inferred semantic relationships. 

No explanation is needed, only return your answer in JSON format: {"output": <answer>}, where the <answer> is a list of lists. Each inner list should contain exactly one value from Table 1, and its semantically matching value from Table 2. If a value from Table 1 does not have corresponding value from Table 2, you can omit it in the answer. But be careful, not to miss any values from Table 1 that do have corresponding matching values in Table 2.

Input Table 1:
{{{input_1}}}

Input Table 2:
{{{input_2}}}

Joined Table:

"""


dataset_config = {
    "task": "semantic-join",
    "version": "1.0_sample1000_html",
    "tag": "1.0_sample1000_html",
    # "note": "NL2SQL datasets multi-table. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/semantic-join/sample1000-3shots",
    "info": "info.json",
    "fields": {
        "input_1": {
          "type": "table.csv", 
          "path": "input_1.csv",
          "reader": "pandas",
          "serializer": HTMLSerializer,
        },
        "input_2": {
            "type": "table.csv", 
            "path": "input_2.csv",
            "reader": "pandas",
            "serializer": HTMLSerializer,
        },
    }
}
