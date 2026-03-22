#!/usr/bin/env python3
"""
Qwen2.5-7B-Instruct baseline runner for MMTU benchmark.

Usage:
    python projects/qwen-base-line/run.py smoke      # Phase 1: 5 questions
    python projects/qwen-base-line/run.py baseline    # Phase 2: 99 questions
    python projects/qwen-base-line/run.py evaluate <result_file>
"""

import argparse
import json
import random
import subprocess
import sys
from pathlib import Path

from datasets import load_dataset
from openai import OpenAI


def _get_mmtu_root() -> Path:
    """Return the MMTU repo root (two levels up from this file)."""
    return Path(__file__).resolve().parent.parent.parent


def _get_output_dir() -> Path:
    """Return the project output directory, creating it if needed."""
    out = Path(__file__).resolve().parent / "output"
    out.mkdir(exist_ok=True)
    return out


def load_mmtu_dataset(hf_dataset: str, hf_split: str) -> list[dict]:
    """Load the full MMTU dataset from HuggingFace.

    Uses the datasets library's built-in caching (~/.cache/huggingface/datasets).
    First call downloads; subsequent calls load from disk.
    """
    print(f"Loading MMTU dataset from {hf_dataset} (split={hf_split})...")
    ds = load_dataset(hf_dataset, split=hf_split)
    records = [{"prompt": row["prompt"], "metadata": row["metadata"]} for row in ds]
    print(f"  Loaded {len(records)} total records.")
    return records


def sample_records_filtered(
    records: list[dict],
    tasks: list[str],
    n_per_task: int,
    seed: int,
    max_input_tokens: int,
) -> list[dict]:
    """Sample n_per_task records per task, excluding prompts that exceed max_input_tokens.

    Filters the full dataset by task membership and token count first,
    then randomly samples from qualifying records per task.
    Tasks with zero qualifying samples are reported and skipped.
    """
    from utils.count_token import count_tokens_mp

    task_set = set(tasks)

    # 1. Collect task-relevant records
    task_records: list[tuple[str, dict]] = []  # (task, record)
    for rec in records:
        meta = json.loads(rec["metadata"])
        task = meta["task"]
        if task in task_set:
            task_records.append((task, rec))

    # 2. Batch token count
    prompts = [rec["prompt"] for _, rec in task_records]
    token_counts = count_tokens_mp(prompts)

    # 3. Filter by token limit and bucket by task
    by_task: dict[str, list[dict]] = {t: [] for t in tasks}
    skipped_counts: dict[str, int] = {t: 0 for t in tasks}

    for (task, rec), tc in zip(task_records, token_counts):
        if tc > max_input_tokens:
            skipped_counts[task] += 1
        else:
            by_task[task].append(rec)

    # 4. Sample
    rng = random.Random(seed)
    sampled = []
    for task in sorted(tasks):
        pool = by_task[task]
        total = len(pool) + skipped_counts[task]
        if len(pool) == 0:
            print(f"  {task}: 0/{total} fit ≤{max_input_tokens} tokens — SKIPPED")
            continue
        n = min(n_per_task, len(pool))
        chosen = rng.sample(pool, n)
        sampled.extend(chosen)
        print(f"  {task}: sampled {n}/{len(pool)} qualifying"
              f" ({skipped_counts[task]}/{total} exceeded token limit)")

    print(f"  Total sampled: {len(sampled)}")
    return sampled


def check_vllm_health(base_url: str) -> bool:
    """Check if the vLLM server is reachable by listing models."""
    try:
        client = OpenAI(base_url=base_url, api_key="EMPTY")
        models = client.models.list()
        model_ids = [m.id for m in models.data]
        print(f"  vLLM models available: {model_ids}")
        return True
    except Exception as e:
        print(f"  ERROR: Cannot reach vLLM at {base_url}: {e}")
        return False


def run_inference(input_file: Path, output_file: Path,
                  base_url: str, model: str, api_key: str,
                  model_alias: str, temperature: float) -> Path:
    """Run inference using inference.py's pipeline.

    Imports create_query_funtion_openai and query_chat_endpoint from
    the MMTU inference module to reuse its multi-threading, resumption,
    and error handling.
    """
    mmtu_root = _get_mmtu_root()
    if str(mmtu_root) not in sys.path:
        sys.path.insert(0, str(mmtu_root))

    from inference import create_query_funtion_openai, query_chat_endpoint

    query_func = create_query_funtion_openai(base_url, model, api_key)
    query_chat_endpoint(
        str(input_file), str(output_file),
        [query_func], temperature,
        n_parallel_call_per_key=1, model_name=model_alias
    )
    return output_file


def run_evaluation(result_file: Path, mmtu_root: Path,
                   n_jobs: int = -1) -> int:
    """Run evaluate.py via subprocess.

    Subprocess is needed because evaluate.py uses module-level args globals
    (args.debug, args.viz, args.n_jobs) set in __main__.
    """
    cmd = [
        sys.executable, str(mmtu_root / "evaluate.py"),
        str(result_file),
        "--n_jobs", str(n_jobs),
    ]
    print(f"  Running: {' '.join(cmd)}")
    proc = subprocess.run(cmd, cwd=str(mmtu_root))
    return proc.returncode


def _run_phase(phase_name: str, tasks: list[str], n_per_task: int,
               eval_n_jobs: int = -1):
    """Shared logic for smoke and baseline phases."""
    from config import (
        VLLM_BASE_URL, VLLM_API_KEY, VLLM_MODEL, MODEL_ALIAS,
        TEMPERATURE, HF_DATASET, HF_SPLIT, RANDOM_SEED,
        MAX_INPUT_TOKENS,
    )

    mmtu_root = _get_mmtu_root()
    output_dir = _get_output_dir()

    print("=" * 60)
    print(f"PHASE: {phase_name.upper()}")
    print(f"Tasks: {len(tasks)}, samples/task: {n_per_task}")
    print("=" * 60)

    # 1. Health check
    print("\n[1/3] Checking vLLM server...")
    if not check_vllm_health(VLLM_BASE_URL):
        print("FATAL: vLLM server not available. Is it running?")
        sys.exit(1)

    # 2. Load, filter by token limit, and sample
    print("\n[2/3] Loading and sampling dataset...")
    records = load_mmtu_dataset(HF_DATASET, HF_SPLIT)

    mmtu_root_str = str(mmtu_root)
    if mmtu_root_str not in sys.path:
        sys.path.insert(0, mmtu_root_str)

    sampled = sample_records_filtered(
        records, tasks, n_per_task, RANDOM_SEED, MAX_INPUT_TOKENS
    )

    # 3. Write input JSONL and run inference
    print("\n[3/3] Running inference & evaluation...")
    input_file = output_dir / f"{phase_name}.input.jsonl"
    with open(input_file, "w") as f:
        for rec in sampled:
            f.write(json.dumps(rec) + "\n")

    output_file = output_dir / f"{phase_name}.{MODEL_ALIAS}.result.jsonl"
    run_inference(input_file, output_file,
                  VLLM_BASE_URL, VLLM_MODEL, VLLM_API_KEY,
                  MODEL_ALIAS, TEMPERATURE)

    # Evaluate
    rc = run_evaluation(output_file, mmtu_root, n_jobs=eval_n_jobs)
    if rc != 0:
        print(f"Evaluation exited with code {rc}")
        sys.exit(rc)

    print(f"\n{phase_name.capitalize()} complete! Check results/ directory.")


def cmd_smoke(args):
    """Phase 1: Smoke test with 5 Entity-Matching questions."""
    from config import SMOKE_TEST_TASKS, SMOKE_TEST_N_PER_TASK
    _run_phase("smoke", SMOKE_TEST_TASKS, SMOKE_TEST_N_PER_TASK, eval_n_jobs=1)


def cmd_baseline(args):
    """Phase 2: Baseline with 99 questions across 11 tasks."""
    from config import BASELINE_TASKS, BASELINE_N_PER_TASK
    _run_phase("baseline", BASELINE_TASKS, BASELINE_N_PER_TASK)


def cmd_evaluate(args):
    """Standalone evaluation of a result file."""
    mmtu_root = _get_mmtu_root()
    result_file = Path(args.result_file).resolve()
    if not result_file.exists():
        print(f"Error: {result_file} does not exist")
        sys.exit(1)
    rc = run_evaluation(result_file, mmtu_root, n_jobs=args.n_jobs)
    sys.exit(rc)


def main():
    # Ensure config.py is importable
    project_dir = Path(__file__).resolve().parent
    if str(project_dir) not in sys.path:
        sys.path.insert(0, str(project_dir))

    parser = argparse.ArgumentParser(
        description="Qwen2.5-7B-Instruct baseline for MMTU"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("smoke", help="Phase 1: smoke test (5 questions)")
    subparsers.add_parser("baseline", help="Phase 2: baseline (99 questions)")

    sub_eval = subparsers.add_parser("evaluate", help="Evaluate a result file")
    sub_eval.add_argument("result_file", type=str)
    sub_eval.add_argument("--n_jobs", type=int, default=-1)

    args = parser.parse_args()

    commands = {"smoke": cmd_smoke, "baseline": cmd_baseline, "evaluate": cmd_evaluate}
    commands[args.command](args)


if __name__ == "__main__":
    main()
