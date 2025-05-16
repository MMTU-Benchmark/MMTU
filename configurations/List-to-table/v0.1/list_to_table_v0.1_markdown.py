from utils.table_serializer import MarkdownSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are given a table where each row contains multiple fields. The number and type of fields may vary. Your task is to process each row and convert it into a single string with all fields separated by "||", while preserving the order and structure of the original row. Return the processed table string in JSON format: {"table": "<processed table string>"}

Input:
{{{TEGRA_TABLE_TEXT}}}

"""


dataset_config = {
    "task": "List-to-table",
    "version": "0.1_sample1000_markdown",
    "tag": ["0.1_sample1000_markdown", "0.1_sample1000_markdown_gpt35"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/List-to-table/sample1000",
    "info": "info.json",
    "fields": {
        "TEGRA_TABLE_TEXT": {
            "type": "text",
            "name": "TEGRA_TABLE_TEXT"
        }
    }
}
