"""Parse and permute markdown tables embedded in MMTU prompts.

Finds standard markdown pipe tables (produced by pandas to_markdown()),
parses them into rows/columns, applies column and/or row permutations,
and re-serializes back into the prompt.
"""

import random
import re


# Regex to match a contiguous block of markdown table lines.
# Each line starts with optional whitespace then a pipe character.
_TABLE_LINE_RE = re.compile(r"^\s*\|.*\|\s*$")

# Separator line: contains only pipes, dashes, colons, and whitespace.
_SEPARATOR_RE = re.compile(r"^\s*\|[\s\-:|]+\|\s*$")


def _find_table_blocks(text: str) -> list[tuple[int, int]]:
    """Return (start_line, end_line) indices for each markdown table block.

    A table block is a contiguous run of lines matching the pipe-table pattern,
    containing at least a header, separator, and one data row.
    """
    lines = text.split("\n")
    blocks = []
    i = 0
    while i < len(lines):
        if _TABLE_LINE_RE.match(lines[i]):
            start = i
            while i < len(lines) and _TABLE_LINE_RE.match(lines[i]):
                i += 1
            end = i  # exclusive
            # Must have at least 3 lines (header + separator + 1 data row)
            if end - start >= 3:
                # Verify there's a separator line
                has_sep = any(_SEPARATOR_RE.match(lines[j]) for j in range(start, end))
                if has_sep:
                    blocks.append((start, end))
        else:
            i += 1
    return blocks


def _parse_row(line: str) -> list[str]:
    """Parse a pipe-delimited row into cell values (stripped)."""
    # Strip leading/trailing pipe and split
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [cell.strip() for cell in stripped.split("|")]


def _format_row(cells: list[str], widths: list[int]) -> str:
    """Format a list of cells into a pipe-delimited row with aligned widths."""
    parts = []
    for cell, w in zip(cells, widths):
        parts.append(f" {cell:<{w}} ")
    return "|" + "|".join(parts) + "|"


def _format_separator(widths: list[int], alignments: list[str]) -> str:
    """Format a separator row with proper alignment markers."""
    parts = []
    for w, align in zip(widths, alignments):
        dashes = "-" * (w + 2)  # +2 for padding spaces
        if align == "right":
            dashes = dashes[:-1] + ":"
        elif align == "center":
            dashes = ":" + dashes[1:-1] + ":"
        elif align == "left":
            dashes = ":" + dashes[1:]
        parts.append(dashes)
    return "|" + "|".join(parts) + "|"


def _parse_alignment(sep_cell: str) -> str:
    """Parse alignment from a separator cell (e.g., ':---:', '---:', ':---')."""
    s = sep_cell.strip()
    left = s.startswith(":")
    right = s.endswith(":")
    if left and right:
        return "center"
    if right:
        return "right"
    if left:
        return "left"
    return "none"


def _permute_table_block(
    lines: list[str],
    start: int,
    end: int,
    shuffle_columns: bool = False,
    shuffle_rows: bool = False,
    rng: random.Random | None = None,
) -> list[str]:
    """Permute a single markdown table block in-place.

    Returns the modified list of lines for the block.
    """
    if rng is None:
        rng = random.Random(42)

    block_lines = lines[start:end]

    # Find separator line index (relative to block)
    sep_idx = None
    for i, line in enumerate(block_lines):
        if _SEPARATOR_RE.match(line):
            sep_idx = i
            break

    if sep_idx is None:
        return block_lines  # Can't parse, return unchanged

    # Parse header (lines before separator), separator, and data rows
    header_cells = _parse_row(block_lines[sep_idx - 1])
    sep_cells = _parse_row(block_lines[sep_idx])
    alignments = [_parse_alignment(c) for c in sep_cells]

    data_rows_with_indices = []
    for i in range(sep_idx + 1, len(block_lines)):
        data_rows_with_indices.append((_parse_row(block_lines[i]), i - (sep_idx + 1)))

    n_cols = len(header_cells)

    # Build column permutation
    if shuffle_columns:
        col_order = list(range(n_cols))
        rng.shuffle(col_order)
    else:
        col_order = list(range(n_cols))

    # Apply column permutation
    header_cells = [header_cells[i] for i in col_order]
    alignments = [alignments[i] for i in col_order]
    data_rows_with_indices = [
        ([row[i] for i in col_order] if len(row) == n_cols else row, orig_idx)
        for row, orig_idx in data_rows_with_indices
    ]

    # Apply row permutation
    if shuffle_rows:
        rng.shuffle(data_rows_with_indices)

    # Compute column widths for alignment
    all_rows = [header_cells] + [row for row, _ in data_rows_with_indices]
    widths = []
    for col_idx in range(n_cols):
        max_w = max(len(row[col_idx]) for row in all_rows if col_idx < len(row))
        widths.append(max_w)

    # Rebuild block
    result = []
    # Any lines before header (usually none for standard tables)
    for i in range(sep_idx - 1):
        result.append(block_lines[i])
    result.append(_format_row(header_cells, widths))
    result.append(_format_separator(widths, alignments))
    for row, orig_idx in data_rows_with_indices:
        if len(row) == n_cols:
            result.append(_format_row(row, widths))
        else:
            # Malformed row, keep as-is using the tracked original index
            result.append(block_lines[sep_idx + 1 + orig_idx])

    return result


def permute_tables_in_prompt(
    prompt: str,
    shuffle_columns: bool = False,
    shuffle_rows: bool = False,
    seed: int = 42,
) -> str:
    """Find all markdown tables in a prompt and apply permutations.

    Args:
        prompt: The full prompt text containing markdown tables.
        shuffle_columns: If True, randomly permute column order.
        shuffle_rows: If True, randomly permute data row order.
        seed: Random seed for reproducibility.

    Returns:
        The prompt with permuted tables.
    """
    if not shuffle_columns and not shuffle_rows:
        return prompt

    lines = prompt.split("\n")
    blocks = _find_table_blocks(prompt)

    if not blocks:
        return prompt

    # Process blocks in reverse order so line indices remain valid
    rng = random.Random(seed)
    for start, end in reversed(blocks):
        new_block = _permute_table_block(
            lines, start, end,
            shuffle_columns=shuffle_columns,
            shuffle_rows=shuffle_rows,
            rng=rng,
        )
        lines[start:end] = new_block

    return "\n".join(lines)
