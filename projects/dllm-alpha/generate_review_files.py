"""
Generate three review files from MMTU result JSONL:
1. questions.md       — full input prompts with IDs
2. results.csv        — per-question: id, task, expected, actual, score
3. summary.csv        — per-task aggregate metrics (using official aggregation)
"""

import json
import csv
import re
import ast
import sys
from collections import defaultdict
from pathlib import Path

def _safe_csv(val):
    """Wrap values that start with =, +, -, @ in backticks so Google Sheets won't interpret them as formulas."""
    s = str(val)
    if s and s[0] in ('=', '+', '-', '@'):
        return f'`{s}`'
    # Also check inside JSON arrays/objects for leading =
    if s.startswith('[') or s.startswith('{'):
        if '= ' in s or '"=' in s:
            return f'`{s}`'
    return s

if len(sys.argv) < 2:
    print("Usage: python generate_review_files.py <result_file.jsonl>")
    sys.exit(1)

RESULT_FILE = Path(sys.argv[1]).resolve()
if not RESULT_FILE.exists():
    print(f"Error: {RESULT_FILE} not found")
    sys.exit(1)

OUT_DIR = RESULT_FILE.parent / "review"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ── Load data ──────────────────────────────────────────────────────────────
with open(RESULT_FILE) as f:
    records = [json.loads(line) for line in f]

# ── Helpers: mirror official evaluators exactly ────────────────────────────

def _get_pred_json(text, key):
    """Extract value for `key` from JSON in model response (mirrors BaseEvaluator._get_pred)."""
    # Strip markdown code fences
    text = text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        text = "\n".join(lines[1:])
        if text.endswith("```"):
            text = text[:-3]
    # Try full parse
    try:
        obj = json.loads(text.strip())
        if isinstance(obj, dict) and key in obj:
            return obj[key]
    except Exception:
        pass
    # Regex for key: value
    pattern = rf'"{key}"\s*:\s*(\[[\s\S]*?\]|\{{[\s\S]*?\}})'
    match = re.search(pattern, text)
    if match:
        try:
            return json.loads(match.group(1))
        except Exception:
            pass
    return "JSONParsingError"


def _extract_reshape_json(text):
    """Extract list of JSON objects for data-transform-reshape."""
    pattern = r'\{[^}]*\}'
    matches = re.findall(pattern, text)
    rst = []
    for m in matches:
        try:
            rst.append(json.loads(m))
        except Exception:
            try:
                rst.append(ast.literal_eval(m))
            except Exception:
                continue
    return rst if rst else "JSONParsingError"


# ── Task scorers ──────────────────────────────────────────────────────────

def score_formula_context(y_true, response):
    """Exact match on formula string."""
    try:
        obj = json.loads(response.strip().lstrip("`").strip().rstrip("`").strip())
        if isinstance(obj, dict) and "formula" in obj:
            y_pred = obj["formula"]
        else:
            y_pred = str(obj)
    except Exception:
        y_pred = response.strip()
    y_true_clean = str(y_true).replace("$", "").strip()
    y_pred_clean = str(y_pred).replace("$", "").strip()
    score = 1.0 if y_true_clean == y_pred_clean else 0.0
    return {"score": score, "actual": y_pred}


def score_data_transform_reshape(y_true_label, y_true_alt, response):
    """Exact match on list of operation dicts."""
    y_pred = _extract_reshape_json(response)
    if y_pred == "JSONParsingError":
        return {"score": 0.0, "actual": "JSONParsingError"}

    if isinstance(y_pred, dict):
        y_pred = [y_pred]

    y_pred_eval = []
    for op in (y_pred if isinstance(y_pred, list) else [y_pred]):
        if isinstance(op, dict):
            op2 = dict(op)
            if "transformation" in op2:
                op2["operator"] = op2.pop("transformation")
            y_pred_eval.append(op2)

    if isinstance(y_true_label, dict):
        y_true_label = [y_true_label]

    correct = 0
    if isinstance(y_true_label, list) and len(y_pred_eval) == len(y_true_label):
        if all(a == b for a, b in zip(y_pred_eval, y_true_label)):
            correct = 1

    if not correct and y_true_alt:
        alt = [y_true_alt] if isinstance(y_true_alt, dict) else y_true_alt
        if isinstance(alt, list) and len(y_pred_eval) == len(alt):
            if all(a == b for a, b in zip(y_pred_eval, alt)):
                correct = 1

    return {"score": float(correct), "actual": json.dumps(y_pred_eval)}


def score_semantic_transform(y_true, response):
    """Element-wise accuracy."""
    try:
        text = response.strip()
        if text.startswith("```"):
            lines = text.split("\n")
            text = "\n".join(lines[1:])
            if text.endswith("```"):
                text = text[:-3]
        obj = json.loads(text.strip())
        if isinstance(obj, dict) and "output" in obj:
            y_pred = obj["output"]
        elif isinstance(obj, list):
            y_pred = obj
        else:
            y_pred = text
    except Exception:
        y_pred = response.strip()

    if not isinstance(y_pred, list) or not isinstance(y_true, list):
        return {"score": 0.0, "actual": str(y_pred)[:300]}

    if len(y_true) != len(y_pred):
        return {"score": 0.0, "actual": json.dumps(y_pred)}

    correct = sum(1 for a, b in zip(y_true, y_pred) if str(a) == str(b))
    return {"score": correct / len(y_true), "actual": json.dumps(y_pred)}


def _set_prf(y_true_set, y_pred_set):
    """Compute precision, recall, F1 from two sets. Returns dict with None for undefined."""
    if len(y_true_set) == 0 and len(y_pred_set) == 0:
        return {"precision": None, "recall": None, "f1": None}
    if len(y_true_set) == 0:
        return {"precision": 0.0 if y_pred_set else None, "recall": None, "f1": None}
    if len(y_pred_set) == 0:
        return {"precision": None, "recall": 0.0, "f1": 0.0}
    tp = y_true_set & y_pred_set
    p = len(tp) / len(y_pred_set)
    r = len(tp) / len(y_true_set)
    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
    return {"precision": p, "recall": r, "f1": f1}


def score_ar(y_true, response, labeled_formulas):
    """Arithmetic-Relationship: set-based P/R/F1 (mirrors AREvaluator)."""
    y_pred_raw = _get_pred_json(response, "Arithmetic-Relationship")
    y_true_set = set(y_true) if isinstance(y_true, list) else {y_true}

    if y_pred_raw == "JSONParsingError" or y_pred_raw is None:
        y_pred_list = []
    elif isinstance(y_pred_raw, str):
        y_pred_list = [y_pred_raw]
    elif isinstance(y_pred_raw, list):
        y_pred_list = [str(x) for x in y_pred_raw]
    else:
        y_pred_list = []

    # Strip whitespace like official evaluator
    y_pred_list = [re.sub(r"\s+", "", x) for x in y_pred_list]
    # Filter to valid formulas
    y_pred_set = set(x for x in y_pred_list if x in labeled_formulas)

    res = _set_prf(y_true_set, y_pred_set)
    res["actual"] = json.dumps(sorted(y_pred_set))
    return res


def score_fd(y_true, response, labeled_fds):
    """Functional-Dependency: set-based P/R/F1 (mirrors FDEvaluator)."""
    y_pred_raw = _get_pred_json(response, "Functional-Dependency")
    y_true_set = set(tuple(x) for x in y_true)

    y_pred_set = set()
    if y_pred_raw != "JSONParsingError" and isinstance(y_pred_raw, list):
        for item in y_pred_raw:
            if isinstance(item, list):
                t = tuple(item)
                if list(t) in labeled_fds:
                    y_pred_set.add(t)

    res = _set_prf(y_true_set, y_pred_set)
    res["actual"] = json.dumps([list(x) for x in sorted(y_pred_set)])
    return res


def score_sr(y_true, response, labeled_data):
    """String-Relationship: set-based P/R/F1 (mirrors SREvaluator)."""
    y_pred_raw = _get_pred_json(response, "String-Relationship")
    y_true_set = set()
    if isinstance(y_true, list):
        for item in y_true:
            y_true_set.add((tuple(item[0]), item[1]))

    y_pred_set = set()
    if y_pred_raw != "JSONParsingError" and isinstance(y_pred_raw, list):
        for item in y_pred_raw:
            if isinstance(item, list) and len(item) == 2:
                try:
                    t = (tuple(item[0]) if isinstance(item[0], list) else (item[0],), item[1])
                    y_pred_set.add(t)
                except Exception:
                    pass

    res = _set_prf(y_true_set, y_pred_set)
    res["actual"] = json.dumps([[list(x[0]) if isinstance(x[0], tuple) else x[0], x[1]] for x in sorted(y_pred_set, key=str)])
    return res


# ── Process all records ───────────────────────────────────────────────────

rows = []         # for results.csv
md_sections = []  # for questions.md
# For summary: per-task lists of {precision, recall, score, metric}
task_data = defaultdict(list)

for idx, rec in enumerate(records):
    meta = json.loads(rec["metadata"]) if isinstance(rec["metadata"], str) else rec["metadata"]
    task = meta["task"]
    test_case = meta.get("test_case", f"sample_{idx}")
    qid = f"{task}__{test_case}"
    prompt = rec["prompt"]
    response = rec["response"] or ""

    if task == "Formula-prediction-context":
        res = score_formula_context(meta["formula"], response)
        expected = meta["formula"]
        metric_name = "acc"
    elif task == "Data-transform-reshape":
        res = score_data_transform_reshape(meta["label"], meta.get("alternative_label"), response)
        expected = json.dumps(meta["label"])
        metric_name = "acc"
    elif task == "semantic-transform":
        res = score_semantic_transform(meta["label"], response)
        expected = json.dumps(meta["label"])
        metric_name = "acc"
    elif task == "Arithmetic-Relationship":
        res = score_ar(meta["label"], response, meta.get("labeled_formulas", []))
        expected = json.dumps(meta["label"])
        metric_name = "f1"
    elif task == "Functional-Dependency":
        res = score_fd(meta["label"], response, meta.get("labeled_fds", []))
        expected = json.dumps(meta["label"])
        metric_name = "f1"
    elif task == "String-Relationship":
        res = score_sr(meta["label"], response, meta.get("labeled_data", []))
        expected = json.dumps(meta["label"])
        metric_name = "f1"
    else:
        res = {"score": "", "actual": response[:200]}
        expected = ""
        metric_name = "unknown"

    # For F1 tasks, the "score" column shows the per-row F1
    score_val = res.get("f1", res.get("score", ""))

    rows.append({
        "question_id": qid,
        "task": task,
        "expected_answer": _safe_csv(expected),
        "actual_answer": _safe_csv(res["actual"]),
        "score": score_val if score_val is not None else "",
    })

    task_data[task].append({
        "metric": metric_name,
        "score": res.get("score", res.get("f1")),
        "precision": res.get("precision"),
        "recall": res.get("recall"),
        "f1": res.get("f1"),
    })

    # ── Markdown section ──
    md_sections.append(f"## {qid}\n\n"
                       f"**Task:** {task}\n\n"
                       f"**Input:**\n\n{prompt}\n\n---\n\n")


# ── Write questions.md ────────────────────────────────────────────────────
md_path = OUT_DIR / "questions.md"
with open(md_path, "w") as f:
    f.write("# MMTU Evaluation Questions\n\n")
    f.write(f"Total questions: {len(records)}\n\n---\n\n")
    for sec in md_sections:
        f.write(sec)
print(f"Wrote {md_path}  ({len(md_sections)} questions)")

# ── Write results.csv ─────────────────────────────────────────────────────
csv_path = OUT_DIR / "results.csv"
with open(csv_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["question_id", "task", "expected_answer", "actual_answer", "score"])
    writer.writeheader()
    writer.writerows(rows)
print(f"Wrote {csv_path}  ({len(rows)} rows)")

# ── Write summary.csv (official aggregation) ──────────────────────────────
summary_path = OUT_DIR / "summary.csv"
with open(summary_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "task", "metric", "num_samples", "mean_precision", "mean_recall", "mean_score"])
    writer.writeheader()
    for task in sorted(task_data.keys()):
        entries = task_data[task]
        n = len(entries)
        metric = entries[0]["metric"]

        if metric == "acc":
            scores = [float(e["score"]) for e in entries if e["score"] is not None and e["score"] != ""]
            writer.writerow({
                "task": task,
                "metric": "acc",
                "num_samples": n,
                "mean_precision": "",
                "mean_recall": "",
                "mean_score": f"{sum(scores)/len(scores):.4f}" if scores else "0",
            })
        else:
            # F1: official = mean(P), mean(R), then F1(mean_P, mean_R)
            precs = [e["precision"] for e in entries if e["precision"] is not None]
            recalls = [e["recall"] for e in entries if e["recall"] is not None]
            mean_p = sum(precs) / len(precs) if precs else 0
            mean_r = sum(recalls) / len(recalls) if recalls else 0
            f1 = 2 * mean_p * mean_r / (mean_p + mean_r) if (mean_p + mean_r) > 0 else 0
            writer.writerow({
                "task": task,
                "metric": "f1",
                "num_samples": n,
                "mean_precision": f"{mean_p:.4f}",
                "mean_recall": f"{mean_r:.4f}",
                "mean_score": f"{f1:.4f}",
            })
print(f"Wrote {summary_path}")
