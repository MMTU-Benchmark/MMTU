"""
Generate per-task markdown files showing all questions from the baseline run.

Reads the input and result JSONL files, groups questions by task, and writes
one markdown file per task to projects/qwen-base-line/output/tasks/.
"""

import json
import os
import textwrap

INPUT_FILE = "projects/qwen-base-line/output/baseline.input.fix.jsonl"
RESULT_FILE = "projects/qwen-base-line/output/baseline.Qwen2_5-7B-Instruct.result.fix.jsonl"
OUTPUT_DIR = "projects/qwen-base-line/output/tasks"


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def get_correct_answer(meta):
    """Extract the correct/expected answer from metadata."""
    task = meta["task"]

    # Table-Locate-by-Row-Col has special fields instead of label/output
    if task == "Table-Locate-by-Row-Col":
        val = meta.get("needle_value", "(unknown)")
        row = meta.get("needle_row_idx", "?")
        col_name = meta.get("needle_col_name", "?")
        return json.dumps({"cell": val}, indent=2) + f"\n\n(Row {row}, Column \"{col_name}\")"

    # Entity-Matching: label is 0/1, map to human-readable
    if task == "Entity-Matching" and "label" in meta:
        label = meta["label"]
        if label == 1:
            return '{"label": "match"}  (label=1)'
        elif label == 0:
            return '{"label": "non-match"}  (label=0)'

    # Data-Imputation: prefer 'output' field which has JSON format, fall back to 'label'
    if task == "Data-Imputation":
        if "output" in meta and meta["output"] not in (None, "N/A"):
            out = meta["output"]
            if isinstance(out, str):
                try:
                    parsed = json.loads(out)
                    return json.dumps(parsed, indent=2)
                except (json.JSONDecodeError, TypeError):
                    return str(out)
        if "label" in meta:
            return json.dumps({"value": str(meta["label"])}, indent=2)

    # Tasks that store answer in 'output' field as JSON string
    if "output" in meta and meta["output"] not in (None, "N/A"):
        out = meta["output"]
        if isinstance(out, str):
            try:
                return json.dumps(json.loads(out), indent=2)
            except (json.JSONDecodeError, TypeError):
                return str(out)
        return json.dumps(out, indent=2)

    # Tasks that store answer in 'label' field
    if "label" in meta:
        label = meta["label"]
        if isinstance(label, list):
            return json.dumps(label, indent=2)
        return str(label)

    return "(no ground truth found)"


def format_prompt_as_markdown(prompt, task):
    """Format the prompt for display - truncate very long tables but keep readable."""
    lines = prompt.split("\n")
    if len(lines) > 80:
        # Show first 40 and last 20 lines with truncation notice
        header = lines[:40]
        footer = lines[-20:]
        omitted = len(lines) - 60
        return "\n".join(header) + f"\n\n... ({omitted} rows omitted) ...\n\n" + "\n".join(footer)
    return prompt


def format_response(response):
    """Clean up model response for display."""
    if not response:
        return "(no response)"
    # Truncate very long responses
    if len(response) > 2000:
        return response[:2000] + "\n\n... (truncated) ..."
    return response


def generate_task_markdown(task_name, entries):
    """Generate markdown content for a single task."""
    lines = []
    lines.append(f"# {task_name}: All Questions ({len(entries)} total)\n")
    lines.append(f"**Model:** Qwen2.5-7B-Instruct\n")

    for i, entry in enumerate(entries, 1):
        meta = json.loads(entry["metadata"])
        dataset = meta.get("dataset", "unknown")
        test_case = meta.get("test_case", "unknown")
        prompt = entry["prompt"]
        response = entry.get("response", "(no response)")
        correct = get_correct_answer(meta)

        lines.append(f"---\n")
        lines.append(f"## Question {i}: {test_case} ({dataset})\n")

        # Metadata
        lines.append(f"**Dataset:** {dataset}  ")
        lines.append(f"**Test case:** {test_case}  ")
        version = meta.get("version", "")
        if version:
            lines.append(f"**Version:** {version}  ")
        lines.append("")

        # Prompt
        lines.append("### Prompt\n")
        formatted_prompt = format_prompt_as_markdown(prompt, task_name)
        lines.append("````")
        lines.append(formatted_prompt)
        lines.append("````\n")

        # Model response
        lines.append("### Model Response\n")
        lines.append("```")
        lines.append(format_response(response))
        lines.append("```\n")

        # Correct answer
        lines.append("### Correct Answer\n")
        lines.append("```")
        lines.append(correct)
        lines.append("```\n")

        # Quick verdict
        resp_str = str(response).strip().lower() if response else ""
        correct_str = str(correct).strip().lower()
        # Simple heuristic - exact match check isn't reliable for all tasks
        # Just show both and let the reader compare
        lines.append("")

    return "\n".join(lines)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load both input (has full metadata) and result (has response) files
    inputs = load_jsonl(INPUT_FILE)
    results = load_jsonl(RESULT_FILE)

    # Build lookup from result file by (task, test_case)
    result_lookup = {}
    for r in results:
        meta = json.loads(r["metadata"])
        key = (meta["task"], meta["test_case"])
        result_lookup[key] = r

    # Group inputs by task
    tasks = {}
    for inp in inputs:
        meta = json.loads(inp["metadata"])
        task = meta["task"]
        test_case = meta["test_case"]

        # Merge with result if available
        key = (task, test_case)
        if key in result_lookup:
            entry = result_lookup[key]
        else:
            # Use input, add empty response
            entry = dict(inp)
            entry["response"] = "(no result available)"

        if task not in tasks:
            tasks[task] = []
        tasks[task].append(entry)

    # Generate markdown for each task
    for task_name in sorted(tasks.keys()):
        entries = tasks[task_name]
        md_content = generate_task_markdown(task_name, entries)

        # Sanitize filename
        filename = task_name.replace(" ", "-") + "_examples.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, "w") as f:
            f.write(md_content)
        print(f"  Wrote {filepath} ({len(entries)} questions)")

    print(f"\nDone! Generated {len(tasks)} task files in {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
