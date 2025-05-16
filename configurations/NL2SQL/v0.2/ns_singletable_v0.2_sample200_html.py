from utils.table_serializer import HTMLSerializer

prompt_template = """Natural language to SQL, also known as NL2SQL, is the problem of generating a SQL query that can be executed on a input table, for a given natural language question.

You will be given an input table called "table" in the HTML format, as well as a question. Your task is to generate an SQL query that can be executed on the input table to answer the question.

Please ensure that the generated SQL only return relevant columns being specifically asked in the question (e.g., in SQL please don't return more than one columns in SELECT if only one column is needed to answer the given question, and similarly please refrain from using SELECT * unless the entire row is needed to answer the question).
 
When generating SQL code, please use the SQLite syntax to ensure that your SQL is executable on SQLite3. Use only columns that are present in the table, always use quotes around your column and table names (some column names have punctuation or special characters), and refer to the columns using the column-names exactly as they appear in the table, do not add or remove punctuation (underscore, slash, etc.)

No explanation, return the code only with the following markdown codeblock format : ```sql<SQL CODE>```. For example, ```sql\nSELECT * FROM "table"\n``` is a valid format.

Table:
{{{table}}}

Question: {{{question}}}"""


dataset_config = {
    "task": "NL2SQL",
    "version": "0.2_sample200_html_singletable",
    "tag": ["0.2_sample200_html"],
    # "note": "This is the first version of the NL2SQL dataset. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/NL2SQL/benchmark/sample200-3shots/singletable",
    "info": "info.json",
    "fields": {
        "table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": HTMLSerializer,
            "name": "table"
        },
        "question": {
            "type": "text",
            "name": "question"
        },
    }
}

