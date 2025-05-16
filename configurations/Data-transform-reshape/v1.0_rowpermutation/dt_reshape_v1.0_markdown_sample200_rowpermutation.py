from utils.table_serializer import MarkdownSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor
from utils.table_processor import ShuffleRowsProcessor, ShuffleColumnsKeepFirstThreeProcessor

prompt_template = """Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
{{{input_table}}}

## Output:
"""


dataset_config = {
    "task": "Data-transform-reshape",
    "version": "1.0_sample200_markdown_rowpermutation",
    "tag": ["1.0_sample200_markdown_rowpermutation"],
    # "note": "NL2SQL datasets multi-table. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Data-transform-reshape/sample200-3shots",
    "info": "info.json",
    "fields": {
        "input_table": {
            "type": "table.csv",
            "path": "data.csv",
            "reader": "pandas",
            "serializer": MarkdownSerializer,
            "processors": [FirstNRowsProcessor(n=100), ShuffleRowsProcessor()],
        }
    }
}
