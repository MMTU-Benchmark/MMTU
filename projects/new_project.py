#!/usr/bin/env python3
"""Scaffold a new MMTU experiment project.

Usage:
    python projects/new_project.py my-experiment
    python projects/new_project.py my-experiment --model "gpt-4o" --backend azure_openai
    python projects/new_project.py my-experiment --model "Qwen/Qwen2.5-72B-Instruct" --backend vllm
"""

import argparse
import re
import sys
from pathlib import Path
from string import Template


def derive_model_alias(model: str) -> str:
    """Derive a filename-safe alias from a model name.

    Strips org prefix, replaces dots/slashes/hyphens with underscores.
    evaluate.py line 114: model_name = os.path.basename(jsonl_file).split(".")[-3]
    """
    # Strip org prefix (e.g. "Qwen/Qwen2.5-7B-Instruct" -> "Qwen2.5-7B-Instruct")
    name = model.split("/")[-1]
    # Replace dots with underscores (periods are filename delimiters in evaluate.py)
    name = name.replace(".", "_")
    return name


# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------

CLAUDE_MD = Template("""\
# $project_name

## Goal
$description

## Status
- [ ] Phase 1: Smoke test (5 Entity-Matching questions)
- [ ] Phase 2: Baseline (99 questions, 11 tasks x 9)

## Key Decisions
- **Model**: `$model`
- **Backend**: $backend
- **Temperature**: $temperature
""")

EXPERIMENTS_MD = Template("""\
# Experiments

<!-- Log each experiment as a dated section. Template:

## YYYY-MM-DD — Short description

**Goal:** What you were trying to achieve or test

**Setup:**
- Model: <model name>
- Config: <config file or parameters>
- Other relevant settings

**Results:**
- Key metrics (accuracy, F1, etc.)
- Notable observations

**Takeaways:**
- What was learned
- Next steps or follow-ups
-->
""")

# --- config.py templates (one per backend) ---

CONFIG_OPENAI = Template('''\
"""Configuration constants for $project_name project."""

# Server settings
BASE_URL = "$base_url"
API_KEY = "$api_key"
MODEL = "$model"

# Model alias for filenames (no dots or slashes)
# evaluate.py line 114: model_name = os.path.basename(jsonl_file).split(".")[-3]
MODEL_ALIAS = "$model_alias"

# Inference settings
TEMPERATURE = $temperature

# HuggingFace dataset
HF_DATASET = "MMTU-benchmark/MMTU"
HF_SPLIT = "train"

# Phase 1: smoke test
SMOKE_TEST_TASKS = ["Entity-Matching"]
SMOKE_TEST_N_PER_TASK = 5

# Phase 2: baseline — 11 tasks, 9 per task = 99 total
BASELINE_TASKS = [
    "Entity-Matching",
    "Schema-Matching",
    "Data-Imputation",
    "semantic-transform",
    "List-to-table",
    "Table-Locate-by-Row-Col",
    "Arithmetic-Relationship",
    "Functional-Dependency",
    "String-Relationship",
    "equi-join-detect",
    "semantic-join",
]
BASELINE_N_PER_TASK = 9

# Random seed for reproducible sampling
RANDOM_SEED = 42
''')

CONFIG_AZURE_OPENAI = Template('''\
"""Configuration constants for $project_name project."""

# Azure OpenAI settings
ENDPOINT = "https://<DEPLOYMENT>.openai.azure.com"
API_KEY = "<your-api-key>"
API_VERSION = "2024-08-01-preview"
MODEL = "$model"

# Model alias for filenames (no dots or slashes)
# evaluate.py line 114: model_name = os.path.basename(jsonl_file).split(".")[-3]
MODEL_ALIAS = "$model_alias"

# Inference settings
TEMPERATURE = $temperature

# HuggingFace dataset
HF_DATASET = "MMTU-benchmark/MMTU"
HF_SPLIT = "train"

# Phase 1: smoke test
SMOKE_TEST_TASKS = ["Entity-Matching"]
SMOKE_TEST_N_PER_TASK = 5

# Phase 2: baseline — 11 tasks, 9 per task = 99 total
BASELINE_TASKS = [
    "Entity-Matching",
    "Schema-Matching",
    "Data-Imputation",
    "semantic-transform",
    "List-to-table",
    "Table-Locate-by-Row-Col",
    "Arithmetic-Relationship",
    "Functional-Dependency",
    "String-Relationship",
    "equi-join-detect",
    "semantic-join",
]
BASELINE_N_PER_TASK = 9

# Random seed for reproducible sampling
RANDOM_SEED = 42
''')

CONFIG_AI_FOUNDRY = Template('''\
"""Configuration constants for $project_name project."""

# Azure AI Foundry settings
ENDPOINT = "https://<resource>.services.ai.azure.com/models"
API_KEY = "<your-api-key>"
MODEL = "$model"

# Model alias for filenames (no dots or slashes)
# evaluate.py line 114: model_name = os.path.basename(jsonl_file).split(".")[-3]
MODEL_ALIAS = "$model_alias"

# Inference settings
TEMPERATURE = $temperature

# HuggingFace dataset
HF_DATASET = "MMTU-benchmark/MMTU"
HF_SPLIT = "train"

# Phase 1: smoke test
SMOKE_TEST_TASKS = ["Entity-Matching"]
SMOKE_TEST_N_PER_TASK = 5

# Phase 2: baseline — 11 tasks, 9 per task = 99 total
BASELINE_TASKS = [
    "Entity-Matching",
    "Schema-Matching",
    "Data-Imputation",
    "semantic-transform",
    "List-to-table",
    "Table-Locate-by-Row-Col",
    "Arithmetic-Relationship",
    "Functional-Dependency",
    "String-Relationship",
    "equi-join-detect",
    "semantic-join",
]
BASELINE_N_PER_TASK = 9

# Random seed for reproducible sampling
RANDOM_SEED = 42
''')

# --- run.py templates ---

RUN_PY_OPENAI = Template('''\
#!/usr/bin/env python3
"""
$project_name runner for MMTU benchmark.

Usage:
    python projects/$project_name/run.py smoke
    python projects/$project_name/run.py baseline
    python projects/$project_name/run.py evaluate <result_file>
"""

import argparse
import json
import random
import subprocess
import sys
from pathlib import Path

from datasets import load_dataset


def _get_mmtu_root() -> Path:
    """Return the MMTU repo root (two levels up from this file)."""
    return Path(__file__).resolve().parent.parent.parent


def _get_output_dir() -> Path:
    """Return the project output directory, creating it if needed."""
    out = Path(__file__).resolve().parent / "output"
    out.mkdir(exist_ok=True)
    return out


def load_mmtu_dataset(hf_dataset: str, hf_split: str) -> list[dict]:
    """Load the full MMTU dataset from HuggingFace."""
    print(f"Loading MMTU dataset from {hf_dataset} (split={hf_split})...")
    ds = load_dataset(hf_dataset, split=hf_split)
    records = [{"prompt": row["prompt"], "metadata": row["metadata"]} for row in ds]
    print(f"  Loaded {len(records)} total records.")
    return records


def sample_records(records: list[dict], tasks: list[str],
                   n_per_task: int, seed: int) -> list[dict]:
    """Sample n_per_task records for each task from the full dataset."""
    by_task: dict[str, list[dict]] = {}
    for rec in records:
        meta = json.loads(rec["metadata"])
        task = meta["task"]
        if task in tasks:
            by_task.setdefault(task, []).append(rec)

    missing = set(tasks) - set(by_task.keys())
    if missing:
        print(f"  WARNING: Tasks not found in dataset: {missing}")

    rng = random.Random(seed)
    sampled = []
    for task in sorted(tasks):
        pool = by_task.get(task, [])
        n = min(n_per_task, len(pool))
        if n == 0:
            print(f"  WARNING: No records for task '{task}'")
            continue
        chosen = rng.sample(pool, n)
        sampled.extend(chosen)
        print(f"  {task}: sampled {n}/{len(pool)}")

    print(f"  Total sampled: {len(sampled)}")
    return sampled


def run_inference(input_file: Path, output_file: Path,
                  base_url: str, model: str, api_key: str,
                  model_alias: str, temperature: float) -> Path:
    """Run inference using inference.py's pipeline."""
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
    """Run evaluate.py via subprocess."""
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
        BASE_URL, API_KEY, MODEL, MODEL_ALIAS,
        TEMPERATURE, HF_DATASET, HF_SPLIT, RANDOM_SEED,
    )

    mmtu_root = _get_mmtu_root()
    output_dir = _get_output_dir()

    print("=" * 60)
    print(f"PHASE: {phase_name.upper()}")
    print(f"Tasks: {len(tasks)}, samples/task: {n_per_task}")
    print("=" * 60)

    # 1. Load & sample
    print("\\n[1/3] Loading and sampling dataset...")
    records = load_mmtu_dataset(HF_DATASET, HF_SPLIT)
    sampled = sample_records(records, tasks, n_per_task, RANDOM_SEED)

    # 2. Write input JSONL and run inference
    print("\\n[2/3] Running inference...")
    input_file = output_dir / f"{phase_name}.input.jsonl"
    with open(input_file, "w") as f:
        for rec in sampled:
            f.write(json.dumps(rec) + "\\n")

    output_file = output_dir / f"{phase_name}.{MODEL_ALIAS}.result.jsonl"
    run_inference(input_file, output_file,
                  BASE_URL, MODEL, API_KEY,
                  MODEL_ALIAS, TEMPERATURE)

    # 3. Evaluate
    print("\\n[3/3] Running evaluation...")
    rc = run_evaluation(output_file, mmtu_root, n_jobs=eval_n_jobs)
    if rc != 0:
        print(f"Evaluation exited with code {rc}")
        sys.exit(rc)

    print(f"\\n{phase_name.capitalize()} complete! Check results/ directory.")


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
    project_dir = Path(__file__).resolve().parent
    if str(project_dir) not in sys.path:
        sys.path.insert(0, str(project_dir))

    parser = argparse.ArgumentParser(
        description="$project_name — MMTU experiment runner"
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
''')

RUN_PY_VLLM = Template('''\
#!/usr/bin/env python3
"""
$project_name runner for MMTU benchmark.

Usage:
    python projects/$project_name/run.py smoke
    python projects/$project_name/run.py baseline
    python projects/$project_name/run.py evaluate <result_file>
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
    """Load the full MMTU dataset from HuggingFace."""
    print(f"Loading MMTU dataset from {hf_dataset} (split={hf_split})...")
    ds = load_dataset(hf_dataset, split=hf_split)
    records = [{"prompt": row["prompt"], "metadata": row["metadata"]} for row in ds]
    print(f"  Loaded {len(records)} total records.")
    return records


def sample_records(records: list[dict], tasks: list[str],
                   n_per_task: int, seed: int) -> list[dict]:
    """Sample n_per_task records for each task from the full dataset."""
    by_task: dict[str, list[dict]] = {}
    for rec in records:
        meta = json.loads(rec["metadata"])
        task = meta["task"]
        if task in tasks:
            by_task.setdefault(task, []).append(rec)

    missing = set(tasks) - set(by_task.keys())
    if missing:
        print(f"  WARNING: Tasks not found in dataset: {missing}")

    rng = random.Random(seed)
    sampled = []
    for task in sorted(tasks):
        pool = by_task.get(task, [])
        n = min(n_per_task, len(pool))
        if n == 0:
            print(f"  WARNING: No records for task '{task}'")
            continue
        chosen = rng.sample(pool, n)
        sampled.extend(chosen)
        print(f"  {task}: sampled {n}/{len(pool)}")

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
    """Run inference using inference.py's pipeline."""
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
    """Run evaluate.py via subprocess."""
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
    )

    mmtu_root = _get_mmtu_root()
    output_dir = _get_output_dir()

    print("=" * 60)
    print(f"PHASE: {phase_name.upper()}")
    print(f"Tasks: {len(tasks)}, samples/task: {n_per_task}")
    print("=" * 60)

    # 1. Health check
    print("\\n[1/4] Checking vLLM server...")
    if not check_vllm_health(VLLM_BASE_URL):
        print("FATAL: vLLM server not available. Is it running?")
        sys.exit(1)

    # 2. Load & sample
    print("\\n[2/4] Loading and sampling dataset...")
    records = load_mmtu_dataset(HF_DATASET, HF_SPLIT)
    sampled = sample_records(records, tasks, n_per_task, RANDOM_SEED)

    # 3. Write input JSONL and run inference
    print("\\n[3/4] Running inference...")
    input_file = output_dir / f"{phase_name}.input.jsonl"
    with open(input_file, "w") as f:
        for rec in sampled:
            f.write(json.dumps(rec) + "\\n")

    output_file = output_dir / f"{phase_name}.{MODEL_ALIAS}.result.jsonl"
    run_inference(input_file, output_file,
                  VLLM_BASE_URL, VLLM_MODEL, VLLM_API_KEY,
                  MODEL_ALIAS, TEMPERATURE)

    # 4. Evaluate
    print("\\n[4/4] Running evaluation...")
    rc = run_evaluation(output_file, mmtu_root, n_jobs=eval_n_jobs)
    if rc != 0:
        print(f"Evaluation exited with code {rc}")
        sys.exit(rc)

    print(f"\\n{phase_name.capitalize()} complete! Check results/ directory.")


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
    project_dir = Path(__file__).resolve().parent
    if str(project_dir) not in sys.path:
        sys.path.insert(0, str(project_dir))

    parser = argparse.ArgumentParser(
        description="$project_name — MMTU experiment runner"
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
''')

RUN_PY_AZURE_OPENAI = Template('''\
#!/usr/bin/env python3
"""
$project_name runner for MMTU benchmark.

Usage:
    python projects/$project_name/run.py smoke
    python projects/$project_name/run.py baseline
    python projects/$project_name/run.py evaluate <result_file>
"""

import argparse
import json
import random
import subprocess
import sys
from pathlib import Path

from datasets import load_dataset


def _get_mmtu_root() -> Path:
    """Return the MMTU repo root (two levels up from this file)."""
    return Path(__file__).resolve().parent.parent.parent


def _get_output_dir() -> Path:
    """Return the project output directory, creating it if needed."""
    out = Path(__file__).resolve().parent / "output"
    out.mkdir(exist_ok=True)
    return out


def load_mmtu_dataset(hf_dataset: str, hf_split: str) -> list[dict]:
    """Load the full MMTU dataset from HuggingFace."""
    print(f"Loading MMTU dataset from {hf_dataset} (split={hf_split})...")
    ds = load_dataset(hf_dataset, split=hf_split)
    records = [{"prompt": row["prompt"], "metadata": row["metadata"]} for row in ds]
    print(f"  Loaded {len(records)} total records.")
    return records


def sample_records(records: list[dict], tasks: list[str],
                   n_per_task: int, seed: int) -> list[dict]:
    """Sample n_per_task records for each task from the full dataset."""
    by_task: dict[str, list[dict]] = {}
    for rec in records:
        meta = json.loads(rec["metadata"])
        task = meta["task"]
        if task in tasks:
            by_task.setdefault(task, []).append(rec)

    missing = set(tasks) - set(by_task.keys())
    if missing:
        print(f"  WARNING: Tasks not found in dataset: {missing}")

    rng = random.Random(seed)
    sampled = []
    for task in sorted(tasks):
        pool = by_task.get(task, [])
        n = min(n_per_task, len(pool))
        if n == 0:
            print(f"  WARNING: No records for task '{task}'")
            continue
        chosen = rng.sample(pool, n)
        sampled.extend(chosen)
        print(f"  {task}: sampled {n}/{len(pool)}")

    print(f"  Total sampled: {len(sampled)}")
    return sampled


def run_inference(input_file: Path, output_file: Path,
                  endpoint: str, model: str, api_key: str,
                  api_version: str, model_alias: str,
                  temperature: float) -> Path:
    """Run inference using inference.py's pipeline."""
    mmtu_root = _get_mmtu_root()
    if str(mmtu_root) not in sys.path:
        sys.path.insert(0, str(mmtu_root))

    from inference import create_query_funtion_azure_openai, query_chat_endpoint

    query_func = create_query_funtion_azure_openai(
        endpoint, model, api_key, api_version
    )
    query_chat_endpoint(
        str(input_file), str(output_file),
        [query_func], temperature,
        n_parallel_call_per_key=1, model_name=model_alias
    )
    return output_file


def run_evaluation(result_file: Path, mmtu_root: Path,
                   n_jobs: int = -1) -> int:
    """Run evaluate.py via subprocess."""
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
        ENDPOINT, API_KEY, API_VERSION, MODEL, MODEL_ALIAS,
        TEMPERATURE, HF_DATASET, HF_SPLIT, RANDOM_SEED,
    )

    mmtu_root = _get_mmtu_root()
    output_dir = _get_output_dir()

    print("=" * 60)
    print(f"PHASE: {phase_name.upper()}")
    print(f"Tasks: {len(tasks)}, samples/task: {n_per_task}")
    print("=" * 60)

    # 1. Load & sample
    print("\\n[1/3] Loading and sampling dataset...")
    records = load_mmtu_dataset(HF_DATASET, HF_SPLIT)
    sampled = sample_records(records, tasks, n_per_task, RANDOM_SEED)

    # 2. Write input JSONL and run inference
    print("\\n[2/3] Running inference...")
    input_file = output_dir / f"{phase_name}.input.jsonl"
    with open(input_file, "w") as f:
        for rec in sampled:
            f.write(json.dumps(rec) + "\\n")

    output_file = output_dir / f"{phase_name}.{MODEL_ALIAS}.result.jsonl"
    run_inference(input_file, output_file,
                  ENDPOINT, MODEL, API_KEY, API_VERSION,
                  MODEL_ALIAS, TEMPERATURE)

    # 3. Evaluate
    print("\\n[3/3] Running evaluation...")
    rc = run_evaluation(output_file, mmtu_root, n_jobs=eval_n_jobs)
    if rc != 0:
        print(f"Evaluation exited with code {rc}")
        sys.exit(rc)

    print(f"\\n{phase_name.capitalize()} complete! Check results/ directory.")


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
    project_dir = Path(__file__).resolve().parent
    if str(project_dir) not in sys.path:
        sys.path.insert(0, str(project_dir))

    parser = argparse.ArgumentParser(
        description="$project_name — MMTU experiment runner"
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
''')

RUN_PY_AI_FOUNDRY = Template('''\
#!/usr/bin/env python3
"""
$project_name runner for MMTU benchmark.

Usage:
    python projects/$project_name/run.py smoke
    python projects/$project_name/run.py baseline
    python projects/$project_name/run.py evaluate <result_file>
"""

import argparse
import json
import random
import subprocess
import sys
from pathlib import Path

from datasets import load_dataset


def _get_mmtu_root() -> Path:
    """Return the MMTU repo root (two levels up from this file)."""
    return Path(__file__).resolve().parent.parent.parent


def _get_output_dir() -> Path:
    """Return the project output directory, creating it if needed."""
    out = Path(__file__).resolve().parent / "output"
    out.mkdir(exist_ok=True)
    return out


def load_mmtu_dataset(hf_dataset: str, hf_split: str) -> list[dict]:
    """Load the full MMTU dataset from HuggingFace."""
    print(f"Loading MMTU dataset from {hf_dataset} (split={hf_split})...")
    ds = load_dataset(hf_dataset, split=hf_split)
    records = [{"prompt": row["prompt"], "metadata": row["metadata"]} for row in ds]
    print(f"  Loaded {len(records)} total records.")
    return records


def sample_records(records: list[dict], tasks: list[str],
                   n_per_task: int, seed: int) -> list[dict]:
    """Sample n_per_task records for each task from the full dataset."""
    by_task: dict[str, list[dict]] = {}
    for rec in records:
        meta = json.loads(rec["metadata"])
        task = meta["task"]
        if task in tasks:
            by_task.setdefault(task, []).append(rec)

    missing = set(tasks) - set(by_task.keys())
    if missing:
        print(f"  WARNING: Tasks not found in dataset: {missing}")

    rng = random.Random(seed)
    sampled = []
    for task in sorted(tasks):
        pool = by_task.get(task, [])
        n = min(n_per_task, len(pool))
        if n == 0:
            print(f"  WARNING: No records for task '{task}'")
            continue
        chosen = rng.sample(pool, n)
        sampled.extend(chosen)
        print(f"  {task}: sampled {n}/{len(pool)}")

    print(f"  Total sampled: {len(sampled)}")
    return sampled


def run_inference(input_file: Path, output_file: Path,
                  endpoint: str, model: str, api_key: str,
                  model_alias: str, temperature: float) -> Path:
    """Run inference using inference.py's pipeline."""
    mmtu_root = _get_mmtu_root()
    if str(mmtu_root) not in sys.path:
        sys.path.insert(0, str(mmtu_root))

    from inference import create_query_function_ai_foundry, query_chat_endpoint

    query_func = create_query_function_ai_foundry(endpoint, model, api_key)
    query_chat_endpoint(
        str(input_file), str(output_file),
        [query_func], temperature,
        n_parallel_call_per_key=1, model_name=model_alias
    )
    return output_file


def run_evaluation(result_file: Path, mmtu_root: Path,
                   n_jobs: int = -1) -> int:
    """Run evaluate.py via subprocess."""
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
        ENDPOINT, API_KEY, MODEL, MODEL_ALIAS,
        TEMPERATURE, HF_DATASET, HF_SPLIT, RANDOM_SEED,
    )

    mmtu_root = _get_mmtu_root()
    output_dir = _get_output_dir()

    print("=" * 60)
    print(f"PHASE: {phase_name.upper()}")
    print(f"Tasks: {len(tasks)}, samples/task: {n_per_task}")
    print("=" * 60)

    # 1. Load & sample
    print("\\n[1/3] Loading and sampling dataset...")
    records = load_mmtu_dataset(HF_DATASET, HF_SPLIT)
    sampled = sample_records(records, tasks, n_per_task, RANDOM_SEED)

    # 2. Write input JSONL and run inference
    print("\\n[2/3] Running inference...")
    input_file = output_dir / f"{phase_name}.input.jsonl"
    with open(input_file, "w") as f:
        for rec in sampled:
            f.write(json.dumps(rec) + "\\n")

    output_file = output_dir / f"{phase_name}.{MODEL_ALIAS}.result.jsonl"
    run_inference(input_file, output_file,
                  ENDPOINT, MODEL, API_KEY,
                  MODEL_ALIAS, TEMPERATURE)

    # 3. Evaluate
    print("\\n[3/3] Running evaluation...")
    rc = run_evaluation(output_file, mmtu_root, n_jobs=eval_n_jobs)
    if rc != 0:
        print(f"Evaluation exited with code {rc}")
        sys.exit(rc)

    print(f"\\n{phase_name.capitalize()} complete! Check results/ directory.")


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
    project_dir = Path(__file__).resolve().parent
    if str(project_dir) not in sys.path:
        sys.path.insert(0, str(project_dir))

    parser = argparse.ArgumentParser(
        description="$project_name — MMTU experiment runner"
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
''')


# ---------------------------------------------------------------------------
# Template dispatch
# ---------------------------------------------------------------------------

CONFIG_VLLM = Template('''\
"""Configuration constants for $project_name project."""

# vLLM server settings
VLLM_BASE_URL = "$base_url"
VLLM_API_KEY = "$api_key"  # vLLM default
VLLM_MODEL = "$model"  # HF name — what vLLM expects

# Model alias for filenames (no dots or slashes)
# evaluate.py line 114: model_name = os.path.basename(jsonl_file).split(".")[-3]
MODEL_ALIAS = "$model_alias"

# Inference settings
TEMPERATURE = $temperature

# HuggingFace dataset
HF_DATASET = "MMTU-benchmark/MMTU"
HF_SPLIT = "train"

# Phase 1: smoke test
SMOKE_TEST_TASKS = ["Entity-Matching"]
SMOKE_TEST_N_PER_TASK = 5

# Phase 2: baseline — 11 tasks, 9 per task = 99 total
BASELINE_TASKS = [
    "Entity-Matching",
    "Schema-Matching",
    "Data-Imputation",
    "semantic-transform",
    "List-to-table",
    "Table-Locate-by-Row-Col",
    "Arithmetic-Relationship",
    "Functional-Dependency",
    "String-Relationship",
    "equi-join-detect",
    "semantic-join",
]
BASELINE_N_PER_TASK = 9

# Random seed for reproducible sampling
RANDOM_SEED = 42
''')

CONFIG_TEMPLATES: dict[str, Template] = {
    "openai": CONFIG_OPENAI,
    "vllm": CONFIG_VLLM,
    "azure_openai": CONFIG_AZURE_OPENAI,
    "azure_ai": CONFIG_AI_FOUNDRY,
}

RUN_TEMPLATES: dict[str, Template] = {
    "openai": RUN_PY_OPENAI,
    "vllm": RUN_PY_VLLM,
    "azure_openai": RUN_PY_AZURE_OPENAI,
    "azure_ai": RUN_PY_AI_FOUNDRY,
}

BACKEND_DEFAULTS: dict[str, dict[str, str]] = {
    "openai": {
        "base_url": "https://api.openai.com/v1",
        "api_key": "<your-api-key>",
    },
    "vllm": {
        "base_url": "http://localhost:8000/v1",
        "api_key": "EMPTY",
    },
    "azure_openai": {},  # uses its own template
    "azure_ai": {},      # uses its own template
}


def scaffold(name: str, model: str, description: str,
             backend: str, temperature: float) -> None:
    """Create a new experiment project directory with templated files."""
    projects_dir = Path(__file__).resolve().parent
    project_dir = projects_dir / name

    if project_dir.exists():
        print(f"Error: {project_dir} already exists. Choose a different name.")
        sys.exit(1)

    model_alias = derive_model_alias(model)

    # Common template variables
    variables = {
        "project_name": name,
        "model": model,
        "model_alias": model_alias,
        "description": description,
        "backend": backend,
        "temperature": str(temperature),
    }

    # Add backend-specific defaults
    defaults = BACKEND_DEFAULTS.get(backend, {})
    variables.update(defaults)

    # Create directory
    project_dir.mkdir(parents=True)

    # Write files
    files = {
        "CLAUDE.md": CLAUDE_MD.substitute(variables),
        "experiments.md": EXPERIMENTS_MD.substitute(variables),
        "config.py": CONFIG_TEMPLATES[backend].substitute(variables),
        "run.py": RUN_TEMPLATES[backend].substitute(variables),
    }

    for filename, content in files.items():
        (project_dir / filename).write_text(content)
        print(f"  Created {project_dir / filename}")

    print(f"\nProject '{name}' created at {project_dir}")
    print(f"\nNext steps:")
    print(f"  1. Edit projects/{name}/config.py — fill in API keys and endpoints")
    print(f"  2. python projects/{name}/run.py smoke")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scaffold a new MMTU experiment project"
    )
    parser.add_argument("name", help="Project directory name (e.g. my-experiment)")
    parser.add_argument("--model", default="Qwen/Qwen2.5-7B-Instruct",
                        help="Model name (default: Qwen/Qwen2.5-7B-Instruct)")
    parser.add_argument("--description", default="TODO: describe goal",
                        help="One-line goal for CLAUDE.md")
    parser.add_argument("--backend", default="openai",
                        choices=["openai", "vllm", "azure_openai", "azure_ai"],
                        help="Inference backend (default: openai)")
    parser.add_argument("--temperature", type=float, default=0.0,
                        help="Inference temperature (default: 0.0)")

    args = parser.parse_args()
    scaffold(args.name, args.model, args.description,
             args.backend, args.temperature)


if __name__ == "__main__":
    main()
