from utils.table_serializer import CSVSerializer

prompt_template = """Task: 
You are given a column of data from a table. Your job is to examine each value in the column, and identify if there is any clear data error in the column. An data error in the context of the column, can be values that are misspelled (typos), values that are formatted incorrectly, or values that are semantically incompatible with the rest of the column, etc., such that we can determine without ambiguity that such values are errors in the column. 

Since real-world data can vary widely in meaning and format, if you are uncertain whether a value is an error, please do not mark it as one. Only flag a value if you are confident that it is clearly a data error.

No explanation and return the final answer as a JSON object, {"obvious_error": "<CELL>"}. If you detect no error in the data, return {"obvious_error": null}.

***EXAMPLE:***

{{{fewshots}}}

***END OF EXAMPLE.***

**INPUT:**
Column:
{{{table}}}

**OUTPUT:**

"""

few_shots_template = """**INPUT:**
Column:
{{{table}}}

**OUTPUT:**
{{{output}}}
"""


dataset_config = {
    "task": "Error-Detect",
    "version": "0.3_sample200_csv_3shot",
    "tag": ["0.3_sample200_csv_3shot"],
    "note": "Error-Detect. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Error-Detect/benchmark/sample200-3shots",
    "info": "info.json",
    "fields": {
        "table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": CSVSerializer,
            "name": "table"
        },
        "fewshots": {
            "type": "fewshot",
            "path": "3shots",
            "info": "info.json",
            "template": few_shots_template,
            "fields": {
                "table": {
                    "type": "table.csv",
                    "path": "data.csv",
                    "reader": "pandas",
                    "serializer": CSVSerializer,
                    "name": "table"
                },
                "output": {
                    "type": "text",
                    "name": "output"
                }
            }
        }
    }
}