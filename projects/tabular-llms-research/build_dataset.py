#!/usr/bin/env python3
"""
Build a deterministic dataset artifact for tabular-llms-research.

Reads a dataset config YAML, pulls from HuggingFace, filters by token length,
samples evenly across tasks, optionally applies table permutations, and
saves a static JSONL artifact for models to evaluate against.

Usage:
    python projects/tabular-llms-research/build_dataset.py configs/dataset_full.yaml
"""

import argparse
import json
import random
import sys
from pathlib import Path

import yaml
from datasets import load_dataset


def _get_mmtu_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent

def _get_project_dir() -> Path:
    return Path(__file__).resolve().parent

def load_config(config_path: str) -> dict:
    path = Path(config_path)
    if not path.is_absolute():
        path = _get_project_dir() / path
    if not path.exists():
        print(f"Error: config file not found: {path}")
        sys.exit(1)
    with open(path) as f:
        return yaml.safe_load(f)

def build_dataset(config: dict, output_path: str):
    dataset_cfg = config["dataset"]
    seed = dataset_cfg.get("seed", 42)
    max_tokens = dataset_cfg.get("max_input_tokens", 3566)
    tasks = dataset_cfg["tasks"]
    n_per_task = dataset_cfg.get("samples_per_task")
    n_total = dataset_cfg.get("total_samples")

    perm_cfg = config.get("permutation", {})
    shuffle_cols = perm_cfg.get("shuffle_columns", False)
    shuffle_rows = perm_cfg.get("shuffle_rows", False)
    perm_seed = perm_cfg.get("seed", seed)

    print(f"Loading MMTU from {dataset_cfg['name']} (split={dataset_cfg['split']})...")
    ds = load_dataset(dataset_cfg["name"], split=dataset_cfg["split"])
    records = [{"prompt": row["prompt"], "metadata": row["metadata"]} for row in ds]

    mmtu_root = _get_mmtu_root()
    if str(mmtu_root) not in sys.path:
        sys.path.insert(0, str(mmtu_root))
    from utils.count_token import count_tokens_mp

    # Filter to requested tasks and markdown only
    task_set = set(tasks)
    task_records = []
    for rec in records:
        meta = json.loads(rec["metadata"])
        if meta["task"] in task_set and "markdown" in meta.get("version", "").lower():
            task_records.append((meta["task"], rec))

    print(f"Filtered to {len(task_records)} markdown records across {len(tasks)} tasks.")

    # Token count
    prompts = [r["prompt"] for _, r in task_records]
    token_counts = count_tokens_mp(prompts)

    by_task = {t: [] for t in tasks}
    for (task, rec), tc in zip(task_records, token_counts):
        if tc <= max_tokens:
            by_task[task].append(rec)

    # Sample
    rng = random.Random(seed)
    sampled = []
    if n_total is not None:
        all_qualifying = []
        for t in tasks:
            all_qualifying.extend(by_task[t])
        sampled = rng.sample(all_qualifying, min(n_total, len(all_qualifying)))
    else:
        for t in tasks:
            pool = by_task[t]
            if pool:
                sampled.extend(rng.sample(pool, min(n_per_task, len(pool))))

    print(f"Sampled {len(sampled)} records.")

    # Permute
    if shuffle_cols or shuffle_rows:
        print(f"Applying permutations (cols={shuffle_cols}, rows={shuffle_rows}, seed={perm_seed})...")
        from table_permuter import permute_tables_in_prompt
        for rec in sampled:
            rec["prompt"] = permute_tables_in_prompt(
                rec["prompt"], shuffle_columns=shuffle_cols, shuffle_rows=shuffle_rows, seed=perm_seed
            )

    # Save artifact
    out_file = Path(output_path)
    if not out_file.is_absolute():
        out_file = _get_project_dir() / out_file
    out_file.parent.mkdir(parents=True, exist_ok=True)

    with open(out_file, "w") as f:
        for rec in sampled:
            f.write(json.dumps(rec) + "\n")

    print(f"\nSuccessfully built dataset artifact:")
    print(f"-> {out_file.relative_to(_get_project_dir())}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=str)
    args = parser.parse_args()
    cfg = load_config(args.config)

    if "output" not in cfg or "artifact_path" not in cfg["output"]:
        print("Error: Config must specify output.artifact_path")
        sys.exit(1)

    build_dataset(cfg, cfg["output"]["artifact_path"])
