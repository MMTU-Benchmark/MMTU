from utils.table_serializer import CSVSerializer

prompt_template = """Task: 
You are given a table containing structured data and a natural language question referring to the table. Your goal is to analyze the table and provide an accurate and concise answer based on the given data.

Instructions:
1. Understand the Table: Examine the structure, headers, and data in the table. Identify relevant columns and rows related to the question.
2. Interpret the Question: Determine whether the question requires direct retrieval, aggregation, comparison, sorting, filtering, or inference.
3. Extract the Answer: Use logical reasoning and numerical operations (if necessary) to derive the correct response from the table.
4. Format the Answer: No explanation, return the answer in a structured JSON format: {"answer": <answer>}. If the question cannot be answered due to missing or ambiguous data, return a JSON response with {"answer": null}.

***EXAMPLE:***

{{{fewshots}}}

***END OF EXAMPLE.***

**INPUT:**
Table:
{{{table}}}

Question:
{{{question}}}

**OUTPUT:**
"""

fewshots_template = """**INPUT:**
Table:
{{{table}}}

Question:
{{{question}}}

**OUTPUT:**
{{{output}}}

"""


dataset_config = {
    "task": "Table-QA",
    "version": "0.2_sample1000_csv_3shot",
    "tag": ["0.2_sample1000_csv_3shot"],
    # "note": "TableQA. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Table-QA/benchmark/sample1000-3shots",
    "info": "info.json",
    "fields": {
        "table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": CSVSerializer,
            "name": "table"
        },
        "question": {
            "type": "text",
            "name": "question"
        },
        "fewshots": {
            "type": "fewshot",
            "path": "3shots",
            "info": "info.json",
            "template": fewshots_template,
            "fields": {
                "table": {
                    "type": "table.csv",
                    "path": "data.csv",
                    "reader": "pandas",
                    "serializer": CSVSerializer,
                    "name": "table"
                },
                "question": {
                    "type": "text",
                    "name": "question"
                },
                "output": {
                    "type": "text",
                    "name": "output"
                },
            }
        }
    }
}

