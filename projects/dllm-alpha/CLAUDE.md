# dllm-alpha

## Goal
Experiment runner for evaluating diffusion LLMs (LLaDA) vs autoregressive baselines (Qwen)
on MMTU table understanding tasks. Pluggable backends, YAML-driven configs, data-parallel
GPU inference, and traceable results.

## Status
- [x] Project structure and backend interface
- [x] LLaDA backend (vendored generate.py from LLaDA repo @ 0474aa1)
- [x] LLaDA data-parallel backend (multi-GPU replicas)
- [x] Qwen backend (vLLM OpenAI-compatible API)
- [x] DeepSeek V3 backend (OpenRouter API, OpenAI-compatible)
- [x] Flat random sampling (for smoke tests)
- [x] Experiment configs: llada-8b + qwen-7b + deepseek-v3 (smoke + full)
- [ ] First smoke test run on GPU
- [ ] Full experiment runs

## Architecture

```
projects/dllm-alpha/
├── run.py                          # Entry point (run, evaluate, list)
├── analyze.py                      # Post-run analysis (per-task scores, token stats)
├── backends/
│   ├── base.py                     # InferenceBackend ABC
│   ├── llada_backend.py            # LLaDA single-GPU backend
│   ├── llada_dp_backend.py         # LLaDA data-parallel backend (multi-GPU)
│   ├── llada_generate.py           # Vendored from LLaDA repo
│   ├── qwen_backend.py             # Qwen via vLLM OpenAI API
│   └── deepseek_backend.py         # DeepSeek V3 via OpenRouter API
├── configs/
│   ├── llada-8b-smoke.yaml         # 25 flat random samples, llada-dp
│   ├── llada-8b-full.yaml          # 15 per task, llada-dp
│   ├── qwen-7b-smoke.yaml          # 25 flat random samples, vLLM
│   ├── qwen-7b-full.yaml           # 15 per task, vLLM
│   ├── deepseek-v3-smoke.yaml      # 25 flat random samples, DeepSeek API
│   ├── deepseek-v3-full.yaml       # 25 per task, DeepSeek API
│   └── qwen-7b-full-256.yaml      # 25 per task, vLLM, 256 max output tokens
├── docker/
│   ├── Dockerfile
│   └── entrypoint.sh
└── output/                         # Auto-created per experiment
```

## Tasks (9 MMTU tasks)

| Task | Abbrev | Metric |
|---|---|---|
| Data-transform-reshape | TTBR | acc |
| Transform-by-output-target-schema | TTBS | acc |
| Transform-by-input-output-table | TTBT | acc |
| Data-transform-pbe | PTBE | acc |
| Formula-prediction-context | FBC | acc |
| semantic-transform | STBE | acc |
| Arithmetic-Relationship | AR | f1 |
| Functional-Dependency | FR | f1 |
| String-Relationship | SR | f1 |

## Experiments

### Experiment 1: LLaDA
- Model: GSAI-ML/LLaDA-8B-Instruct
- Remasking: random, semi-autoregressive
- Block size: 64, steps: 256 (512/2), output context: 512
- Batch size: 16, data-parallel across 4 GPUs
- Backend: `llada-dp`

### Experiment 2: Qwen (baseline)
- Model: Qwen/Qwen2.5-7B-Instruct via vLLM
- Tensor-parallel across 4 GPUs (vLLM `--tensor-parallel-size 4`)
- Backend: `qwen`

### Experiment 3: DeepSeek V3 (baseline)
- Model: deepseek/deepseek-chat (DeepSeek V3) via OpenRouter
- API key: set via `OPENROUTER_API_KEY` env var
- Backend: `deepseek`

### Dataset splits
- **Smoke**: 25 flat random samples across all 9 tasks (after token filtering)
- **Full**: 25 samples per task
- Token filter: max_input_tokens = 3566 (4096 - 530)

## Commands

```bash
# Run experiments
python projects/dllm-alpha/run.py run configs/llada-8b-smoke.yaml
python projects/dllm-alpha/run.py run configs/qwen-7b-smoke.yaml

# Full runs
python projects/dllm-alpha/run.py run configs/llada-8b-full.yaml
python projects/dllm-alpha/run.py run configs/qwen-7b-full.yaml
python projects/dllm-alpha/run.py run configs/deepseek-v3-full.yaml

# DeepSeek V3 via OpenRouter (set API key first)
export OPENROUTER_API_KEY=<your-key>
python projects/dllm-alpha/run.py run configs/deepseek-v3-smoke.yaml

# Evaluate standalone
python projects/dllm-alpha/run.py evaluate <result_file>

# List experiments
python projects/dllm-alpha/run.py list

# Launch vLLM for Qwen (4 GPU tensor parallel)
python -m vllm.entrypoints.openai.api_server \
    --model Qwen/Qwen2.5-7B-Instruct \
    --tensor-parallel-size 4
```

## Key Decisions
- **Data-parallel LLaDA**: LLaDA-8B (~16GB bf16) fits on a single GPU. We load 4 replicas
  and split batches across them for 4x throughput.
- **Concurrent GPU dispatch**: `generate_batch` uses `ThreadPoolExecutor` to run all GPU
  shards in parallel. This works because CUDA kernels release the Python GIL — each thread
  spends >99% of wall time inside GPU kernels (forward passes, softmax, topk) and holds
  the GIL only for microseconds of Python dispatch between ops. Threads driving separate
  GPUs achieve near-linear speedup with negligible GIL contention.
- **Vendored generate.py**: Copied from LLaDA repo (SHA 0474aa1) to avoid cross-repo dep.
- **Flat sampling for smoke**: Smoke tests draw 25 random samples across all tasks
  (not per-task) for quick validation.
- **Resumption**: Re-running the same config skips already-processed prompts.
