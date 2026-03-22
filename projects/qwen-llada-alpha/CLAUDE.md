# qwen-llada-alpha

## Goal
Shared experiment runner for evaluating multiple models on MMTU benchmark tasks.
Pluggable inference backends (starting with LLaDA), YAML-driven experiment configs,
and traceable results.

## Status
- [x] Project structure and backend interface
- [x] LLaDA backend (vendored generate.py from LLaDA repo @ 0474aa1)
- [x] Experiment configs: llada-8b-smoke, llada-8b-baseline
- [x] Shared run.py with run/evaluate/list commands
- [x] Dockerfile and entrypoint
- [ ] First smoke test run on GPU
- [ ] Full baseline run

## Architecture

```
projects/qwen-llada-alpha/
├── run.py                          # Shared entry point (run, evaluate, list)
├── backends/
│   ├── base.py                     # InferenceBackend ABC
│   ├── llada_backend.py            # LLaDA diffusion backend
│   └── llada_generate.py           # Vendored from LLaDA repo
├── configs/                        # YAML experiment definitions
│   ├── llada-8b-smoke.yaml
│   └── llada-8b-baseline.yaml
├── docker/
│   ├── Dockerfile                  # Single image for all backends
│   └── entrypoint.sh
└── output/
    └── {experiment_name}/          # Auto-created per experiment
        ├── config.yaml             # Frozen copy of config used
        ├── provenance.json         # git SHA, timestamp
        ├── input.jsonl
        └── {name}.{alias}.result.jsonl
```

## Key Decisions
- **Vendored generate.py**: LLaDA's core sampling is ~130 lines with no internal deps.
  Copied into backends/llada_generate.py (pinned to SHA 0474aa1) rather than adding
  a cross-repo dependency.
- **Single Dockerfile**: Uses pytorch base image. Additional backends (e.g. vLLM for
  autoregressive models) can be pip-installed without a separate image.
- **YAML configs**: Each experiment is a YAML file. Spinning up a new experiment =
  copy a YAML and change a few fields.
- **Traceability**: Every run freezes config + provenance (git SHA, timestamp) into
  the output directory. `run.py list` shows all experiments at a glance.
- **Resumption**: If run.py is interrupted, re-running the same config skips already-
  processed prompts.
- **Subprocess evaluation**: Same approach as qwen-base-line — calls evaluate.py via
  subprocess to avoid its module-level `args` globals.

## Testing

Unit tests live in `tests/` and use a `FakeModel` mock (no GPU or checkpoint needed).
Run with: `pytest tests/ -v`

Existing coverage: `tests/test_llada_generate.py` — tensor shapes, batch dims, remasking
strategies, CFG, semi-autoregressive blocks, `get_num_transfer_tokens`.

When adding new backends or modifying core logic, add unit tests for tensor plumbing
and shape invariants. Integration tests (requiring a real model or dataset) are not
needed for every change, but should be added where they would catch non-obvious bugs
(e.g. batched vs single inference consistency, padding/truncation edge cases,
end-to-end prompt→evaluation round-trips with a small fixture dataset).

## Adding a New Model Backend
1. Create `backends/new_backend.py` implementing `InferenceBackend` (load, generate, health_check)
2. Register it in `backends/__init__.py`
3. Create a YAML config in `configs/`
4. Run: `python projects/qwen-llada-alpha/run.py run configs/your-config.yaml`

## Commands

```bash
# Run an experiment
python projects/qwen-llada-alpha/run.py run configs/llada-8b-smoke.yaml

# Evaluate a result file standalone
python projects/qwen-llada-alpha/run.py evaluate output/llada-8b-smoke/llada-8b-smoke.LLaDA-8B-Instruct.result.jsonl

# List all experiments
python projects/qwen-llada-alpha/run.py list
```

## Configuration Reference

```yaml
experiment:
  name: <unique-name>         # Used for output directory
  seed: 42                    # Random seed for sampling
  phase: smoke|baseline       # Informational tag
  tags: [...]                 # Informational tags

model:
  backend: llada              # Backend name (registered in backends/__init__.py)
  model_path: <HF model ID>
  alias: <sanitized-name>     # For evaluate.py filename parsing (no dots/slashes)
  dtype: bfloat16

inference:
  max_input_tokens: 3584
  max_output_tokens: 512
  temperature: 0.0
  steps: 128                  # LLaDA: denoising steps
  block_length: 128           # LLaDA: semi-autoregressive block size
  remasking: low_confidence   # LLaDA: remasking strategy
  cfg_scale: 0.0              # LLaDA: classifier-free guidance

dataset:
  name: MMTU-benchmark/MMTU
  split: train
  tasks: [...]                # List of MMTU tasks
  samples_per_task: 9
```
