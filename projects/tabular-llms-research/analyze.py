#!/usr/bin/env python3
"""
Post-run analysis for tabular-llms-research experiments.

Produces per-question metadata, per-task score summaries,
and token distribution statistics.

Usage:
    python projects/tabular-llms-research/analyze.py <result_file>.jsonl
"""

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

try:
    import tiktoken
    _encoder = tiktoken.encoding_for_model("gpt-4o")
    def count_tokens(text: str) -> int:
        return len(_encoder.encode(text))
except Exception:
    def count_tokens(text: str) -> int:
        return max(1, int(len(text.split()) * 1.3))


def get_mmtu_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def load_evaluators():
    """Import MMTU evaluators via the main evaluation module."""
    mmtu_root = get_mmtu_root()
    if str(mmtu_root) not in sys.path:
        sys.path.insert(0, str(mmtu_root))

    from evaluate import evaluator_dict
    return evaluator_dict


F1_TASKS = {
    "Error-Detect", "Schema-Matching", "semantic-join",
    "Arithmetic-Relationship", "Functional-Dependency", "String-Relationship",
    "equi-join-detect",
}


def find_eom(response: str) -> str:
    """Return response up to end-of-message marker (or full response)."""
    for marker in ("<|im_end|>", "<|endoftext|>", "<|eom|>"):
        idx = response.find(marker)
        if idx != -1:
            return response[:idx]
    return response


def evaluate_per_row(result_df: pd.DataFrame, evaluators: dict) -> pd.DataFrame:
    """Run MMTU evaluators to get per-row scores."""
    all_results = []

    for task, group in result_df.groupby("task"):
        evaluator = evaluators.get(task)
        if evaluator is None:
            for _, row in group.iterrows():
                meta = json.loads(row["metadata"])
                all_results.append({
                    "task": task,
                    "test_case": meta.get("test_case", ""),
                    "score": -1.0,
                    "metric_type": "unknown",
                })
            continue

        try:
            parsed = evaluator.parse_raw_result(group)
        except Exception as e:
            print(f"  Warning: could not evaluate {task}: {e}")
            for _, row in group.iterrows():
                meta = json.loads(row["metadata"])
                all_results.append({
                    "task": task,
                    "test_case": meta.get("test_case", ""),
                    "score": -1.0,
                    "metric_type": "error",
                })
            continue

        is_f1 = task in F1_TASKS
        for _, prow in parsed.iterrows():
            test_case = prow.get("test_case", "")
            if is_f1:
                prec = float(prow.get("precision") or 0)
                rec = float(prow.get("recall") or 0)
                if prec + rec > 0:
                    score = 2 * prec * rec / (prec + rec)
                else:
                    score = 0.0
                metric_type = "f1"
            else:
                score = float(prow.get("correct", 0) or 0)
                metric_type = "acc"

            all_results.append({
                "task": task,
                "test_case": str(test_case),
                "score": score,
                "metric_type": metric_type,
            })

    return pd.DataFrame(all_results)


def main():
    parser = argparse.ArgumentParser(description="Post-run analysis of MMTU results")
    parser.add_argument("result_file", type=str, help="Path to .result.jsonl")
    parser.add_argument("--output", "-o", type=str, default=None,
                        help="Output markdown file (default: alongside result file)")
    args = parser.parse_args()

    result_path = Path(args.result_file).resolve()
    if not result_path.exists():
        print(f"Error: {result_path} not found")
        sys.exit(1)

    output_path = Path(args.output) if args.output else result_path.with_suffix(".analysis.md")

    rows = []
    with open(result_path) as f:
        for line in f:
            rows.append(json.loads(line))

    if not rows:
        print("No results found.")
        sys.exit(1)

    print(f"Loaded {len(rows)} results from {result_path.name}")

    result_df = pd.read_json(result_path, lines=True)
    if "task" not in result_df.columns:
        result_df["task"] = result_df["metadata"].apply(lambda x: json.loads(x)["task"])

    evaluators = load_evaluators()
    eval_df = evaluate_per_row(result_df, evaluators)

    # Token counts
    token_data = []
    for row in rows:
        response_raw = row.get("response", "")
        response = find_eom(response_raw)
        metadata = json.loads(row["metadata"])
        token_data.append({
            "task": metadata["task"],
            "test_case": metadata.get("test_case", ""),
            "input_tokens": count_tokens(row["prompt"]),
            "output_tokens": count_tokens(response),
        })
    token_df = pd.DataFrame(token_data)

    df = token_df.merge(eval_df, on=["task", "test_case"], how="left")
    df["score"] = df["score"].fillna(-1)
    df["metric_type"] = df["metric_type"].fillna("unknown")

    # Build markdown report
    md = []
    exp_name = rows[0].get("experiment", result_path.stem)
    md.append(f"# Analysis: {exp_name}\n")
    md.append(f"**Result file:** `{result_path.name}`  ")
    md.append(f"**Samples:** {len(df)}\n")

    # Per-question table
    md.append("## Per-Question Metadata\n")
    md.append("| # | Task | Test Case | Input Tok | Output Tok | Metric | Score |")
    md.append("|---|---|---|---|---|---|---|")
    for i, r in df.iterrows():
        score = r["score"]
        mtype = r["metric_type"]
        if score < 0:
            score_str = "N/A"
        elif mtype == "acc":
            score_str = "1.00" if score >= 0.5 else "0.00"
        else:
            score_str = f"{score:.3f}"
        md.append(f"| {i+1} | {r['task']} | {r['test_case']} | {r['input_tokens']} | "
                  f"{r['output_tokens']} | {mtype} | {score_str} |")
    md.append("")

    # Score summary by task
    evaluated = df[df["score"] >= 0]
    md.append("## Score Summary by Task\n")
    if len(evaluated) > 0:
        md.append("| Task | Metric | N | Mean Score | Perfect (=1.0) | Zero (=0.0) |")
        md.append("|---|---|---|---|---|---|")
        for task, grp in evaluated.groupby("task"):
            mtype = grp["metric_type"].iloc[0]
            n = len(grp)
            mean_score = grp["score"].mean()
            perfect = int((grp["score"] >= 1.0 - 1e-9).sum())
            zero = int((grp["score"] <= 1e-9).sum())
            md.append(f"| {task} | {mtype} | {n} | {mean_score:.3f} | {perfect}/{n} | {zero}/{n} |")

        overall_mean = evaluated["score"].mean()
        md.append(f"\n**Overall mean score:** {overall_mean:.3f}\n")
    else:
        md.append("_No evaluatable tasks found._\n")

    # Per-task token statistics
    md.append("## Per-Task Token Statistics\n")
    md.append("| Task | N | Input Mean | Input Med | Output Mean | Output Med |")
    md.append("|---|---|---|---|---|---|")
    for task, grp in df.groupby("task"):
        n = len(grp)
        im = grp["input_tokens"].mean()
        imed = grp["input_tokens"].median()
        om = grp["output_tokens"].mean()
        omed = grp["output_tokens"].median()
        md.append(f"| {task} | {n} | {im:.0f} | {imed:.0f} | {om:.0f} | {omed:.0f} |")
    md.append("")

    report = "\n".join(md)

    with open(output_path, "w") as f:
        f.write(report)

    # Export a machine-readable JSON summary alongside the markdown report
    summary_data = {
        "experiment": exp_name,
        "result_file": result_path.name,
        "samples": len(df),
        "overall_score": float(overall_mean) if len(evaluated) > 0 else 0.0,
        "tasks": {}
    }

    if len(evaluated) > 0:
        for task, grp in evaluated.groupby("task"):
            summary_data["tasks"][task] = {
                "metric": grp["metric_type"].iloc[0],
                "samples": len(grp),
                "score": float(grp["score"].mean()),
                "perfect": int((grp["score"] >= 1.0 - 1e-9).sum()),
                "zero": int((grp["score"] <= 1e-9).sum())
            }

    json_path = output_path.with_suffix(".json")
    with open(json_path, "w") as f:
        json.dump(summary_data, f, indent=2)

    print(f"\nAnalysis written to: {output_path}")
    print(f"JSON summary written to: {json_path}")
    print(f"\n{'='*60}")
    print(report)


if __name__ == "__main__":
    main()
