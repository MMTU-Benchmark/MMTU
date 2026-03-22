#!/usr/bin/env python3
"""
Compare output directories side-by-side.

Usage:
    python projects/tabular-llms-research/compare.py \
      projects/tabular-llms-research/output/encoder_vs_decoder_baseline/Qwen2.5-14B-Instruct \
      projects/tabular-llms-research/output/encoder_vs_decoder_baseline/t5gemma-9b-ul2-it
"""

import argparse
import json
import sys
from pathlib import Path
import pandas as pd

def parse_json(file_path: Path):
    with open(file_path) as f:
        data = json.load(f)

    tasks = {k: v["score"] for k, v in data.get("tasks", {}).items()}
    overall = data.get("overall_score", 0.0)

    return tasks, overall

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir1", type=str)
    parser.add_argument("dir2", type=str)
    args = parser.parse_args()

    d1 = Path(args.dir1)
    d2 = Path(args.dir2)

    if not d1.exists() or not d2.exists():
        print("Both directories must exist.")
        sys.exit(1)

    json1 = list(d1.glob("*.analysis.json"))
    json2 = list(d2.glob("*.analysis.json"))

    if not json1 or not json2:
        print("Both directories must contain an analysis.json file (run analyze.py again).")
        sys.exit(1)

    t1, o1 = parse_json(json1[0])
    t2, o2 = parse_json(json2[0])

    print("=" * 60)
    print(f"{'Task':<30} | {d1.name[:12]:<12} | {d2.name[:12]:<12} | Delta (d1 - d2)")
    print("-" * 60)

    all_tasks = sorted(set(list(t1.keys()) + list(t2.keys())))
    for task in all_tasks:
        s1 = t1.get(task, 0.0)
        s2 = t2.get(task, 0.0)
        delta = s1 - s2

        delta_str = f"+{delta:.3f}" if delta > 0 else f"{delta:.3f}"
        if delta == 0: delta_str = " 0.000"

        print(f"{task[:28]:<30} | {s1:<12.3f} | {s2:<12.3f} | {delta_str}")

    print("-" * 60)
    o1 = o1 or 0.0
    o2 = o2 or 0.0
    od = o1 - o2
    od_str = f"+{od:.3f}" if od > 0 else f"{od:.3f}"
    print(f"{'OVERALL MEAN SCORE':<30} | {o1:<12.3f} | {o2:<12.3f} | {od_str}")

if __name__ == "__main__":
    main()
