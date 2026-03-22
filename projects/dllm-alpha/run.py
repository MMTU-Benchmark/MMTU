#!/usr/bin/env python3
"""
dllm-alpha: Shared experiment runner for MMTU benchmark experiments.

Usage:
    python projects/dllm-alpha/run.py run configs/llada-8b-smoke.yaml
    python projects/dllm-alpha/run.py run configs/llada-8b-baseline.yaml
    python projects/dllm-alpha/run.py evaluate <result_file> [--n_jobs N]
    python projects/dllm-alpha/run.py list
"""

import argparse
import json
import random
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml
from datasets import load_dataset


def _get_mmtu_root() -> Path:
    """Return the MMTU repo root (three levels up from this file)."""
    return Path(__file__).resolve().parent.parent.parent


def _get_project_dir() -> Path:
    """Return the baselines project directory."""
    return Path(__file__).resolve().parent


def _make_run_key(tag: str | None = None) -> str:
    """Generate a timestamped run key, optionally with a tag suffix."""
    key = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    if tag:
        key = f"{key}_{tag}"
    return key


def _find_latest_run(experiment_name: str) -> Path | None:
    """Return the most recent run directory for an experiment, or None."""
    exp_root = _get_project_dir() / "output" / experiment_name
    if not exp_root.exists():
        return None
    latest_link = exp_root / "latest"
    if latest_link.is_symlink() and latest_link.resolve().is_dir():
        return latest_link.resolve()
    # Fallback: find newest timestamped directory
    run_dirs = sorted(
        [d for d in exp_root.iterdir() if d.is_dir() and not d.is_symlink()],
        key=lambda d: d.name,
    )
    return run_dirs[-1] if run_dirs else None


def _update_latest_symlink(run_dir: Path) -> None:
    """Point the 'latest' symlink at run_dir."""
    latest = run_dir.parent / "latest"
    if latest.is_symlink() or latest.exists():
        latest.unlink()
    latest.symlink_to(run_dir.name)


def _get_output_dir(experiment_name: str, run_key: str) -> Path:
    """Return and create the run output directory."""
    out = _get_project_dir() / "output" / experiment_name / run_key
    out.mkdir(parents=True, exist_ok=True)
    return out


def _git_sha() -> str:
    """Return the current short git SHA, or 'unknown'."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, cwd=str(_get_mmtu_root()),
        )
        return result.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def load_config(config_path: str) -> dict:
    """Load and return a YAML experiment config."""
    path = Path(config_path)
    if not path.is_absolute():
        path = _get_project_dir() / path
    if not path.exists():
        print(f"Error: config file not found: {path}")
        sys.exit(1)
    with open(path) as f:
        return yaml.safe_load(f)


def load_mmtu_dataset(hf_dataset: str, hf_split: str) -> list[dict]:
    """Load the full MMTU dataset from HuggingFace."""
    print(f"Loading MMTU dataset from {hf_dataset} (split={hf_split})...")
    ds = load_dataset(hf_dataset, split=hf_split)
    records = [{"prompt": row["prompt"], "metadata": row["metadata"]} for row in ds]
    print(f"  Loaded {len(records)} total records.")
    return records


def sample_records(
    records: list[dict],
    tasks: list[str],
    n_per_task: int | None,
    seed: int,
    max_input_tokens: int,
    n_total: int | None = None,
) -> list[dict]:
    """Sample records, excluding prompts that exceed max_input_tokens.

    If n_total is set, take a flat random sample of that size across all tasks.
    Otherwise, sample n_per_task records per task.
    """
    mmtu_root = _get_mmtu_root()
    if str(mmtu_root) not in sys.path:
        sys.path.insert(0, str(mmtu_root))
    from utils.count_token import count_tokens_mp

    task_set = set(tasks)

    # Collect task-relevant records
    task_records: list[tuple[str, dict]] = []
    for rec in records:
        meta = json.loads(rec["metadata"])
        task = meta["task"]
        if task in task_set:
            task_records.append((task, rec))

    # Batch token count
    prompts = [rec["prompt"] for _, rec in task_records]
    token_counts = count_tokens_mp(prompts)

    # Filter by token limit and bucket by task
    by_task: dict[str, list[dict]] = {t: [] for t in tasks}
    skipped_counts: dict[str, int] = {t: 0 for t in tasks}

    for (task, rec), tc in zip(task_records, token_counts):
        if tc > max_input_tokens:
            skipped_counts[task] += 1
        else:
            by_task[task].append(rec)

    # Print token filter stats
    for task in sorted(tasks):
        pool = by_task[task]
        total = len(pool) + skipped_counts[task]
        if len(pool) == 0:
            print(f"  {task}: 0/{total} fit <={max_input_tokens} tokens — SKIPPED")
        else:
            print(f"  {task}: {len(pool)}/{total} qualifying"
                  f" ({skipped_counts[task]} exceeded token limit)")

    rng = random.Random(seed)
    sampled = []

    if n_total is not None:
        # Flat random sample across all tasks
        all_qualifying = []
        for task in sorted(tasks):
            all_qualifying.extend(by_task[task])
        n = min(n_total, len(all_qualifying))
        sampled = rng.sample(all_qualifying, n)
        print(f"  Flat sample: {n}/{len(all_qualifying)} total qualifying records")
    else:
        # Per-task sampling
        for task in sorted(tasks):
            pool = by_task[task]
            if len(pool) == 0:
                continue
            n = min(n_per_task, len(pool))
            chosen = rng.sample(pool, n)
            sampled.extend(chosen)
            print(f"  {task}: sampled {n}/{len(pool)}")

    print(f"  Total sampled: {len(sampled)}")
    return sampled


def run_experiment(
    config: dict,
    config_path: str,
    resume: bool | str = False,
    tag: str | None = None,
) -> None:
    """Execute a full experiment: load model, sample data, run inference, evaluate.

    Args:
        resume: False for a fresh run, True to resume the latest run, or a
                specific run key string to resume that run.
        tag: Optional tag appended to the run key (e.g. "oom-fix").
    """
    exp = config["experiment"]
    model_cfg = config["model"]
    inference_cfg = config["inference"]
    dataset_cfg = config["dataset"]

    experiment_name = exp["name"]
    seed = exp["seed"]
    model_alias = model_cfg["alias"]

    # Resolve run key
    if resume:
        if isinstance(resume, str):
            # Resume a specific run
            run_key = resume
            candidate = _get_project_dir() / "output" / experiment_name / run_key
            if not candidate.exists():
                print(f"Error: run '{run_key}' not found in output/{experiment_name}/")
                sys.exit(1)
        else:
            # Resume latest
            latest = _find_latest_run(experiment_name)
            if latest is None:
                print(f"Error: no previous runs found for '{experiment_name}'")
                sys.exit(1)
            run_key = latest.name
        print(f"Resuming run: {run_key}")
    else:
        run_key = _make_run_key(tag)

    output_dir = _get_output_dir(experiment_name, run_key)
    _update_latest_symlink(output_dir)

    print("=" * 60)
    print(f"EXPERIMENT: {experiment_name}")
    print(f"Run key:  {run_key}")
    print(f"Backend: {model_cfg['backend']} | Model: {model_cfg['model_path']}")
    print(f"Output: {output_dir}")
    print("=" * 60)

    # Freeze config into output dir for traceability
    frozen_config = output_dir / "config.yaml"
    shutil.copy2(config_path if Path(config_path).is_absolute()
                 else str(_get_project_dir() / config_path), str(frozen_config))

    # Record provenance
    provenance = {
        "experiment_name": experiment_name,
        "git_sha": _git_sha(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "config_path": config_path,
    }
    with open(output_dir / "provenance.json", "w") as f:
        json.dump(provenance, f, indent=2)

    # 1. Load backend
    print("\n[1/4] Loading model...")
    project_dir = _get_project_dir()
    if str(project_dir) not in sys.path:
        sys.path.insert(0, str(project_dir))
    from backends import get_backend

    backend_cls = get_backend(model_cfg["backend"])
    backend = backend_cls()
    backend.load(config)

    if not backend.health_check():
        print("FATAL: Backend health check failed.")
        sys.exit(1)

    # 2. Load and sample dataset
    print("\n[2/4] Loading and sampling dataset...")
    records = load_mmtu_dataset(dataset_cfg["name"], dataset_cfg["split"])
    sampled = sample_records(
        records,
        dataset_cfg["tasks"],
        dataset_cfg.get("samples_per_task"),
        seed,
        inference_cfg["max_input_tokens"],
        n_total=dataset_cfg.get("total_samples"),
    )

    # 3. Run inference
    batch_size = inference_cfg.get("batch_size", 1)
    print(f"\n[3/4] Running inference on {len(sampled)} samples (batch_size={batch_size})...")
    input_file = output_dir / "input.jsonl"
    result_file = output_dir / f"{experiment_name}.{model_alias}.result.jsonl"

    with open(input_file, "w") as f:
        for rec in sampled:
            f.write(json.dumps(rec) + "\n")

    # Process each sample, with resumption support
    existing_results = set()
    if result_file.exists():
        with open(result_file) as f:
            for line in f:
                row = json.loads(line)
                existing_results.add(row.get("prompt", "")[:200])
        print(f"  Resuming: {len(existing_results)} existing results found.")

    # Filter out already-processed samples
    pending = [rec for rec in sampled if rec["prompt"][:200] not in existing_results]
    completed = len(existing_results)
    total = len(sampled)

    with open(result_file, "a") as out_f:
        for batch_start in range(0, len(pending), batch_size):
            batch = pending[batch_start:batch_start + batch_size]
            batch_prompts = [rec["prompt"] for rec in batch]

            print(f"  [{completed + 1}-{completed + len(batch)}/{total}] "
                  f"Generating batch of {len(batch)}...", end=" ", flush=True)
            t0 = time.time()

            try:
                if len(batch) == 1:
                    responses = [backend.generate(batch_prompts[0])]
                else:
                    responses = backend.generate_batch(batch_prompts)
                elapsed = time.time() - t0
                print(f"done ({elapsed:.1f}s, {elapsed / len(batch):.1f}s/sample)")
            except Exception as e:
                elapsed = time.time() - t0
                print(f"ERROR ({elapsed:.1f}s): {e}")
                responses = [f"[ERROR] {e}"] * len(batch)

            for rec, response in zip(batch, responses):
                result_row = {
                    "prompt": rec["prompt"],
                    "metadata": rec["metadata"],
                    "response": response,
                    "model": model_alias,
                    "experiment": experiment_name,
                }
                out_f.write(json.dumps(result_row) + "\n")
            out_f.flush()
            completed += len(batch)

    # 4. Evaluate
    # Some evaluators (Data-transform-pbe, Transform-by-output-target-schema,
    # Transform-by-input-output-table) execute generated code via subprocess
    # and need MMTU_HOME to locate a temp directory for that.
    import os
    os.environ.setdefault("MMTU_HOME", str(_get_mmtu_root()))

    print("\n[4/5] Evaluating results...")
    rc = run_evaluation(result_file, _get_mmtu_root())
    if rc != 0:
        print(f"Evaluation exited with code {rc}")

    # 5. Post-run analysis
    print("\n[5/5] Running post-run analysis...")
    rc2 = run_analysis(result_file)
    if rc2 != 0:
        print(f"Analysis exited with code {rc2}")
    else:
        print(f"\nExperiment '{experiment_name}' complete!")
        print(f"Results: {output_dir}")


def run_evaluation(result_file: Path, mmtu_root: Path, n_jobs: int = -1) -> int:
    """Run evaluate.py via subprocess."""
    cmd = [
        sys.executable, str(mmtu_root / "evaluate.py"),
        str(result_file),
        "--n_jobs", str(n_jobs),
    ]
    print(f"  Running: {' '.join(cmd)}")
    proc = subprocess.run(cmd, cwd=str(mmtu_root))
    return proc.returncode


def run_analysis(result_file: Path) -> int:
    """Run analyze.py on the result file."""
    analyze_script = _get_project_dir() / "analyze.py"
    cmd = [sys.executable, str(analyze_script), str(result_file)]
    print(f"  Running: {' '.join(cmd)}")
    proc = subprocess.run(cmd, cwd=str(_get_mmtu_root()))
    return proc.returncode


def cmd_run(args):
    """Run an experiment from a YAML config."""
    config = load_config(args.config)
    # --resume with no value → True, --resume KEY → "KEY", absent → False
    resume = args.resume if args.resume is not None else False
    if resume == "":
        resume = True
    run_experiment(config, args.config, resume=resume, tag=args.tag)


def cmd_evaluate(args):
    """Standalone evaluation of a result file."""
    result_file = Path(args.result_file).resolve()
    if not result_file.exists():
        print(f"Error: {result_file} does not exist")
        sys.exit(1)
    rc = run_evaluation(result_file, _get_mmtu_root(), n_jobs=args.n_jobs)
    sys.exit(rc)


def cmd_list(args):
    """List all experiments and their runs."""
    output_root = _get_project_dir() / "output"
    if not output_root.exists():
        print("No experiments found.")
        return

    experiments = sorted(
        [d for d in output_root.iterdir() if d.is_dir()],
        key=lambda d: d.name,
    )
    if not experiments:
        print("No experiments found.")
        return

    for exp_dir in experiments:
        # Detect old-style (flat) vs new-style (run key subdirs)
        run_dirs = sorted(
            [d for d in exp_dir.iterdir() if d.is_dir() and not d.is_symlink()],
            key=lambda d: d.name,
        )

        # Old-style: result files directly in exp_dir
        flat_results = list(exp_dir.glob("*.result.jsonl"))
        if flat_results and not run_dirs:
            run_dirs = [exp_dir]

        latest_link = exp_dir / "latest"
        latest_target = (
            latest_link.resolve().name
            if latest_link.is_symlink()
            else None
        )

        print(f"\n{exp_dir.name}  ({len(run_dirs)} run{'s' if len(run_dirs) != 1 else ''})")
        print(f"  {'Run key':<30} {'Results':<12} {'Timestamp':<22}")
        print(f"  {'-' * 64}")

        for run_dir in run_dirs:
            prov_file = run_dir / "provenance.json"
            if prov_file.exists():
                with open(prov_file) as f:
                    prov = json.load(f)
                timestamp = prov.get("timestamp", "unknown")[:19]
            else:
                timestamp = "unknown"

            result_files = list(run_dir.glob("*.result.jsonl"))
            if result_files:
                with open(result_files[0]) as f:
                    n_results = sum(1 for _ in f)
                status = f"{n_results} results"
            else:
                status = "no results"

            label = run_dir.name
            if run_dir == exp_dir:
                label = "(flat)"
            elif label == latest_target:
                label = f"{label} ← latest"

            print(f"  {label:<30} {status:<12} {timestamp:<22}")


def main():
    parser = argparse.ArgumentParser(
        description="MMTU baseline experiment runner"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # run
    sub_run = subparsers.add_parser("run", help="Run an experiment from a YAML config")
    sub_run.add_argument("config", type=str, help="Path to experiment YAML config")
    sub_run.add_argument(
        "--resume", nargs="?", const="", default=None,
        help="Resume a previous run (latest if no key given, or specify a run key)",
    )
    sub_run.add_argument(
        "--tag", type=str, default=None,
        help="Tag appended to run key (e.g. --tag oom-fix → 20260311-143022_oom-fix)",
    )

    # evaluate
    sub_eval = subparsers.add_parser("evaluate", help="Evaluate a result file")
    sub_eval.add_argument("result_file", type=str)
    sub_eval.add_argument("--n_jobs", type=int, default=-1)

    # list
    subparsers.add_parser("list", help="List all experiments")

    args = parser.parse_args()
    commands = {"run": cmd_run, "evaluate": cmd_evaluate, "list": cmd_list}
    commands[args.command](args)


if __name__ == "__main__":
    main()
