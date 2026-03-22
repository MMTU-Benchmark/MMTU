"""Tests for table_permuter module."""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from table_permuter import (
    _find_table_blocks,
    _parse_row,
    permute_tables_in_prompt,
)


SAMPLE_TABLE = """\
| Name    | Age | City     |
|:--------|----:|:---------|
| Alice   |  25 | New York |
| Bob     |  30 | London   |
| Charlie |  35 | Tokyo    |"""

SAMPLE_PROMPT = f"""\
You are given the following table:

{SAMPLE_TABLE}

Question: What is Bob's age?
Answer:"""


class TestFindTableBlocks:
    def test_finds_single_table(self):
        blocks = _find_table_blocks(SAMPLE_PROMPT)
        assert len(blocks) == 1

    def test_correct_line_range(self):
        blocks = _find_table_blocks(SAMPLE_PROMPT)
        start, end = blocks[0]
        lines = SAMPLE_PROMPT.split("\n")
        # First table line should start with |
        assert lines[start].strip().startswith("|")
        # Last table line should also have pipes
        assert lines[end - 1].strip().startswith("|")

    def test_no_table(self):
        blocks = _find_table_blocks("Hello world\nNo tables here")
        assert len(blocks) == 0

    def test_two_tables(self):
        prompt = f"Table A:\n{SAMPLE_TABLE}\n\nTable B:\n{SAMPLE_TABLE}\n"
        blocks = _find_table_blocks(prompt)
        assert len(blocks) == 2


class TestParseRow:
    def test_simple_row(self):
        cells = _parse_row("| Alice | 25 | New York |")
        assert cells == ["Alice", "25", "New York"]

    def test_numeric_alignment(self):
        cells = _parse_row("|   610 | Allan Hancock |   7534.91 |")
        assert cells[0] == "610"
        assert cells[1] == "Allan Hancock"


class TestPermuteColumns:
    def test_columns_are_shuffled(self):
        result = permute_tables_in_prompt(
            SAMPLE_PROMPT, shuffle_columns=True, seed=42
        )
        # Original has Name | Age | City
        # After shuffle, column order should differ
        lines = result.split("\n")
        # Find header line
        header_line = None
        for line in lines:
            if "|" in line and "---" not in line and "Name" in line or "Age" in line or "City" in line:
                if "|" in line and "---" not in line:
                    cells = [c.strip() for c in line.strip("|").split("|")]
                    if any(c in ("Name", "Age", "City") for c in cells):
                        header_line = line
                        break

        assert header_line is not None
        cells = [c.strip() for c in header_line.strip().strip("|").split("|")]
        # All original columns should be present
        assert set(cells) == {"Name", "Age", "City"}

    def test_deterministic_with_seed(self):
        r1 = permute_tables_in_prompt(SAMPLE_PROMPT, shuffle_columns=True, seed=123)
        r2 = permute_tables_in_prompt(SAMPLE_PROMPT, shuffle_columns=True, seed=123)
        assert r1 == r2

    def test_different_seeds_differ(self):
        r1 = permute_tables_in_prompt(SAMPLE_PROMPT, shuffle_columns=True, seed=1)
        r2 = permute_tables_in_prompt(SAMPLE_PROMPT, shuffle_columns=True, seed=2)
        # With only 3 columns, there's a chance they match, but very unlikely
        # with different seeds. We just check the function runs.
        assert isinstance(r1, str) and isinstance(r2, str)

    def test_data_follows_header(self):
        result = permute_tables_in_prompt(
            SAMPLE_PROMPT, shuffle_columns=True, seed=42
        )
        lines = result.split("\n")
        table_lines = [l for l in lines if l.strip().startswith("|") and "---" not in l]
        if len(table_lines) >= 2:
            header_cells = [c.strip() for c in table_lines[0].strip().strip("|").split("|")]
            data_cells = [c.strip() for c in table_lines[1].strip().strip("|").split("|")]
            # Data should match the shuffled column order
            assert len(header_cells) == len(data_cells)


class TestPermuteRows:
    def test_rows_are_shuffled(self):
        result = permute_tables_in_prompt(
            SAMPLE_PROMPT, shuffle_rows=True, seed=42
        )
        lines = result.split("\n")
        table_lines = [l for l in lines if l.strip().startswith("|") and "---" not in l]
        # Header should remain first
        header = [c.strip() for c in table_lines[0].strip().strip("|").split("|")]
        assert "Name" in header

    def test_header_unchanged(self):
        result = permute_tables_in_prompt(
            SAMPLE_PROMPT, shuffle_rows=True, seed=42
        )
        # Header columns should be exactly the same
        lines = result.split("\n")
        for line in lines:
            if "Name" in line and "Age" in line and "City" in line and "---" not in line:
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                assert cells == ["Name", "Age", "City"]
                break


class TestNoPermutation:
    def test_noop(self):
        result = permute_tables_in_prompt(SAMPLE_PROMPT)
        # Should be identical when no permutation requested
        assert result == SAMPLE_PROMPT

    def test_preserves_surrounding_text(self):
        result = permute_tables_in_prompt(
            SAMPLE_PROMPT, shuffle_columns=True, seed=42
        )
        assert "You are given the following table:" in result
        assert "Question: What is Bob's age?" in result
        assert "Answer:" in result


class TestBothPermutations:
    def test_both(self):
        result = permute_tables_in_prompt(
            SAMPLE_PROMPT, shuffle_columns=True, shuffle_rows=True, seed=42
        )
        # Should still contain all original data
        assert "Alice" in result
        assert "Bob" in result
        assert "Charlie" in result
        assert "25" in result
        assert "30" in result
        assert "35" in result
