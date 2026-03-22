#!/usr/bin/env python3
"""
tabular-llms-research: Experiment runner.

Executes inference on a pre-built static dataset artifact.
Organizes output by <experiment_name>/<model_alias>/.

Usage:
    python projects/tabular-llms-research/run.py run configs/run_qwen_full.yaml
    python projects/tabular-llms-research/run.py evaluate <result_file>
    python projects/tabular-llms-research/run.py list
"""

import argparse
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml

try:
    import wandb
    WANDB_AVAILABLE = True
except ImportError:
    WANDB_AVAILABLE = False

def _make_run_key(tag: str | None = None) -> str:
    """Generate a timestamped run key, optionally with a tag suffix."""
    key = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    if tag:
        key = f"{key}_{tag}"
    return key

def _find_latest_run(exp_name: str, model_alias: str) -> Path | None:
    exp_root = _get_project_dir() / "output" / exp_name / model_alias
    if not exp_root.exists():
        return None
    latest_link = exp_root / "latest"
    if latest_link.is_symlink() and latest_link.resolve().is_dir():
        return latest_link.resolve()
    run_dirs = sorted(
        [d for d in exp_root.iterdir() if d.is_dir() and not d.is_symlink()],
        key=lambda d: d.name,
    )
    return run_dirs[-1] if run_dirs else None

def _update_latest_symlink(run_dir: Path) -> None:
    latest = run_dir.parent / "latest"
    if latest.is_symlink() or latest.exists():
        latest.unlink()
    latest.symlink_to(run_dir.name)

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

def _git_sha() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, cwd=str(_get_mmtu_root()),
        )
        return result.stdout.strip() or "unknown"
    except Exception:
        return "unknown"

def run_experiment(config: dict, config_path: str, resume: bool | str = False, tag: str | None = None):
    exp_cfg = config["experiment"]
    model_cfg = config["model"]
    inf_cfg = config["inference"]
    data_cfg = config["data"]

    exp_name = exp_cfg["name"]
    model_alias = model_cfg["alias"]
    artifact_path = data_cfg["artifact_path"]

    # Resolve run key
    if resume:
        if isinstance(resume, str) and resume != "":
            run_key = resume
            candidate = _get_project_dir() / "output" / exp_name / model_alias / run_key
            if not candidate.exists():
                print(f"Error: run '{run_key}' not found.")
                sys.exit(1)
        else:
            latest = _find_latest_run(exp_name, model_alias)
            if latest is None:
                print(f"Error: no previous runs found for '{exp_name}/{model_alias}'")
                sys.exit(1)
            run_key = latest.name
        print(f"Resuming run: {run_key}")
    else:
        run_key = _make_run_key(tag)

    # Output dir: output/<experiment_name>/<model_alias>/<run_key>/
    out_dir = _get_project_dir() / "output" / exp_name / model_alias / run_key
    out_dir.mkdir(parents=True, exist_ok=True)
    _update_latest_symlink(out_dir)

    print("=" * 60)
    print(f"EXPERIMENT: {exp_name} | {exp_cfg.get('purpose', 'No purpose specified')}")
    print(f"Model: {model_alias} ({model_cfg['backend']})")
    print(f"Data Artifact: {artifact_path}")
    print(f"Output: {out_dir.relative_to(_get_project_dir())}")
    print("=" * 60)

    # Freeze config
    shutil.copy2(
        config_path if Path(config_path).is_absolute() else str(_get_project_dir() / config_path),
        str(out_dir / "config.yaml")
    )

    prov = {
        "experiment_name": exp_name,
        "model_alias": model_alias,
        "git_sha": _git_sha(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "config_path": str(config_path),
        "data_artifact": artifact_path,
    }
    with open(out_dir / "provenance.json", "w") as f:
        json.dump(prov, f, indent=2)

    # 1. Load Data
    artifact_file = Path(artifact_path)
    if not artifact_file.is_absolute():
        artifact_file = _get_project_dir() / artifact_file

    if not artifact_file.exists():
        print(f"FATAL: Dataset artifact not found at {artifact_file}")
        sys.exit(1)

    sampled = []
    with open(artifact_file) as f:
        for line in f:
            sampled.append(json.loads(line))

    # 2. Load Backend
    print(f"\n[1/5] Loading model {model_cfg['model_path']}...")
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

    # 3. Inference
    batch_size = inf_cfg.get("batch_size", 1)
    print(f"\n[2/5] Running inference on {len(sampled)} samples (batch_size={batch_size})...")

    result_file = out_dir / f"{exp_name}.{model_alias}.result.jsonl"

    existing_results = set()
    if resume and result_file.exists():
        with open(result_file) as f:
            for line in f:
                existing_results.add(json.loads(line).get("prompt", "")[:200])
        print(f"  Resuming: {len(existing_results)} existing results found.")

    pending = [rec for rec in sampled if rec["prompt"][:200] not in existing_results]
    completed = len(existing_results)

    with open(result_file, "a" if resume else "w") as out_f:
        for i in range(0, len(pending), batch_size):
            batch = pending[i:i + batch_size]
            batch_prompts = [rec["prompt"] for rec in batch]

            print(f"  [{completed + 1}-{completed + len(batch)}/{len(sampled)}] Generating batch...", end=" ", flush=True)
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
                res_row = {
                    "prompt": rec["prompt"],
                    "metadata": rec["metadata"],
                    "response": response,
                    "model": model_alias,
                    "experiment": exp_name,
                }
                out_f.write(json.dumps(res_row) + "\n")
            out_f.flush()
            completed += len(batch)

    # 4. Evaluate & Analyze
    import os
    os.environ.setdefault("MMTU_HOME", str(_get_mmtu_root()))
    print(f"\n[3/5] Running MMTU evaluation on {result_file.name}...")

    rc = subprocess.run([
        sys.executable, str(_get_mmtu_root() / "evaluate.py"),
        str(result_file)
    ], cwd=str(_get_mmtu_root())).returncode

    if rc != 0:
        print(f"evaluate.py exited with code {rc}")

    print("\n[4/5] Running local analysis...")
    subprocess.run([
        sys.executable, str(_get_project_dir() / "analyze.py"),
        str(result_file)
    ])

    # 5. Parse analysis and log automatically
    experiments_md = _get_project_dir() / "experiments.md"
    score_line = ""
    analysis_file = result_file.with_suffix(".analysis.md")

    task_scores = {}
    overall_score = 0.0
    if analysis_file.exists():
        in_table = False
        with open(analysis_file) as f:
            for line in f:
                if line.startswith("**Overall mean score:**"):
                    score_line = line.split("**:")[-1].strip()
                    overall_score = float(score_line)

                if "## Score Summary by Task" in line:
                    in_table = True
                    continue
                if "## Per-Task Token" in line:
                    in_table = False

                if in_table and line.startswith("| ") and not line.startswith("| Task") and "---" not in line:
                    parts = [p.strip() for p in line.split("|")]
                    if len(parts) > 4:
                        try:
                            task_scores[parts[1]] = float(parts[4])
                        except:
                            pass

    with open(experiments_md, "a") as f:
        date_str = datetime.now().strftime("%Y-%m-%d")
        f.write(f"| {date_str} | `{exp_name}` | `{model_alias}` | {exp_cfg.get('purpose', 'N/A')} | {score_line} |\n")

    # 6. Weights & Biases (W&B) Logging
    use_wandb = exp_cfg.get("wandb", False)
    if use_wandb:
        if not WANDB_AVAILABLE:
            print("WARNING: W&B is enabled in config, but 'wandb' package is not installed. Skipping W&B logging.")
        else:
            print(f"\n[5/5] Logging run to Weights & Biases...")
            wandb.init(
                project="mmtu-tabular-research",
                name=f"{exp_name}-{model_alias}",
                group=exp_name,
                tags=exp_cfg.get("tags", []),
                config=config,
            )

            # Build a unified dictionary to log all metrics in a single step
            metrics_to_log = {"overall_score": overall_score}
            for t_name, t_score in task_scores.items():
                metrics_to_log[f"task/{t_name}"] = t_score

            # Log all scores together so W&B displays them cleanly in one summary row
            wandb.log(metrics_to_log)

            # Log raw generation responses to W&B Table for visual debugging
            print(f"  Uploading predictions table to W&B...")
            table = wandb.Table(columns=["Task", "Test Case", "Prompt", "Generation", "Score", "Metric"])

            # Since analyze.py just ran, it dumped a parsed JSONL with "score" inline (or we can re-evaluate)
            # To keep it simple, we upload the raw results
            try:
                import pandas as pd
                df = pd.read_json(result_file, lines=True)
                for _, row in df.iterrows():
                    meta = json.loads(row["metadata"])
                    table.add_data(
                        meta.get("task", ""),
                        meta.get("test_case", ""),
                        row.get("prompt", "")[:2000] + "..." if len(row.get("prompt", "")) > 2000 else row.get("prompt", ""),
                        row.get("response", "")[:1000],
                        -1, # Actual parsed score is in analysis table
                        "raw"
                    )
                wandb.log({"predictions": table})
            except Exception as e:
                print(f"  Warning: failed to upload W&B Table: {e}")

            wandb.finish()

    print(f"\nExperiment complete. Output logged to experiments.md!")

def cmd_run(args):
    cfg = load_config(args.config)
    resume = args.resume if args.resume is not None else False
    if resume == "":
        resume = True
    run_experiment(cfg, args.config, resume=resume, tag=args.tag)

def cmd_evaluate(args):
    res_file = Path(args.result_file).resolve()
    subprocess.run([sys.executable, str(_get_mmtu_root() / "evaluate.py"), str(res_file)], cwd=str(_get_mmtu_root()))

def cmd_list(args):
    out_dir = _get_project_dir() / "output"
    if not out_dir.exists():
        print("No experiments found.")
        return
    exps = [d for d in out_dir.iterdir() if d.is_dir()]
    for exp in sorted(exps):
        print(f"\nExperiment: {exp.name}")
        models = [m for m in exp.iterdir() if m.is_dir()]
        for m in sorted(models):
            print(f"  └── Model: {m.name}")

def main():
    parser = argparse.ArgumentParser(description="tabular-llms-research runner")
    subs = parser.add_subparsers(dest="command", required=True)

    p_run = subs.add_parser("run", help="Run model on deterministic artifact")
    p_run.add_argument("config", type=str)
    p_run.add_argument(
        "--resume", nargs="?", const="", default=None,
        help="Resume a previous run (latest if no key given, or specify a run key)",
    )
    p_run.add_argument(
        "--tag", type=str, default=None,
        help="Tag appended to run key (e.g. --tag retry -> 20260321-143022_retry)",
    )

    p_eval = subs.add_parser("evaluate", help="Evaluate a result file")
    p_eval.add_argument("result_file", type=str)

    subs.add_parser("list", help="List experiments")

    args = parser.parse_args()
    cmds = {"run": cmd_run, "evaluate": cmd_evaluate, "list": cmd_list}
    cmds[args.command](args)

if __name__ == "__main__":
    main()
