from utils.table_serializer import MarkdownSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

prompt_template = """You are given a table below, where each row corresponds to a record, with multiple columns/attributes. However, the column delimiters separating cell values belonging to different columns within the same row, are missing. 

Your task is to inspect the data below, identify column separators, and mark them clearly using "||" in each row. Please ensure that after your column separators "||" are inserted, each row should have the same number of columns. Also make sure that the output table preserves the order of the input rows, with each output row separated by a new line just like the input rows. 

No explanation and return the processed table string in JSON format: {"table": "<processed table string>"}

Input:
{{{TEGRA_TABLE_TEXT}}}

"""


dataset_config = {
    "task": "List-to-table",
    "version": "1.0_sample200_markdown_4k",
    "tag": ["1.0_sample200_markdown_4k"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/List-to-table/sample200-3shots",
    "info": "info.json",
    "fields": {
        "TEGRA_TABLE_TEXT": {
            "type": "text",
            "name": "TEGRA_TABLE_TEXT"
        }
    }
}
