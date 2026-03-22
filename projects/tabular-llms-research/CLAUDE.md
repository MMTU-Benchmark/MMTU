# tabular-llms-research

## Goal
Compare encoder-decoder (T5Gemma 9B-9B UL2 IT) vs decoder-only (Qwen2.5-14B-Instruct) architectures
on MMTU table understanding tasks. Investigate whether encoder-decoder's bidirectional
attention provides structural advantages for table comprehension, and measure
robustness to column/row permutations.

## Architecture

```
projects/tabular-llms-research/
├── build_dataset.py            # Step 1: Deterministic artifact generator
├── run.py                      # Step 2: Entry point (run, evaluate, list)
├── analyze.py                  # Step 3: Post-run analysis
├── compare.py                  # Step 4: Side-by-side model comparison
├── table_permuter.py           # Used by build_dataset.py
├── backends/
│   ├── base.py
│   ├── qwen_backend.py         # Qwen2.5 via vLLM OpenAI API
│   └── t5gemma_backend.py      # T5Gemma via HuggingFace transformers
├── configs/
│   ├── dataset_baseline.yaml   # Config for dataset generation
│   ├── dataset_colperm.yaml
│   ├── run_qwen_baseline.yaml  # Config for model inference
│   └── run_t5gemma_baseline.yaml
└── output/
    └── encoder_vs_decoder_baseline/     # Experiment Name
        ├── Qwen2.5-14B-Instruct/        # Model output directory
        │   ├── config.yaml
        │   ├── result.jsonl
        │   └── analysis.md
        └── t5gemma-9b-9b-ul2-it/
```

## Workflow (Deterministic & Tracked)

To ensure fair comparison, models DO NOT sample datasets independently. We first generate a static deterministic dataset artifact, then run both models against it.
Outputs are grouped by *experiment*, not by model, so you can easily compare runs. A registry row is also automatically appended to `experiments.md` upon completion.

### Step 1: Generate Dataset Artifact
```bash
# Builds artifacts/datasets/baseline_150_samples.jsonl
python projects/tabular-llms-research/build_dataset.py configs/dataset_baseline.yaml
```

### Step 2: Run Inference
```bash
# Both models evaluate the exact same artifact
# Note: Add `wandb: true` to the `experiment` block in your YAML to automatically
# sync your metrics, inputs, and outputs to the Weights & Biases dashboard!
python projects/tabular-llms-research/run.py run configs/run_qwen_baseline.yaml
python projects/tabular-llms-research/run.py run configs/run_t5gemma_baseline.yaml
```

### Step 3: Compare Results
```bash
# View side-by-side delta of the two runs
python projects/tabular-llms-research/compare.py \
    projects/tabular-llms-research/output/encoder_vs_decoder_baseline/Qwen2.5-14B-Instruct \
    projects/tabular-llms-research/output/encoder_vs_decoder_baseline/t5gemma-9b-9b-ul2-it
```
