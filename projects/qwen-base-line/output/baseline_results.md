# Qwen2.5-7B-Instruct Baseline Results

**Date**: 2026-03-02
**Model**: Qwen2.5-7B-Instruct via vLLM
**Settings**: temperature=0, max_model_len=65536, seed=42
**Samples**: 99 (11 tasks x 9 per task)

## Overall Score: 0.398

## Results by Task

| Task | Questions | Metric | Score |
|:--|--:|:--|--:|
| Entity-Matching | 9 | acc | 1.000 |
| Functional-Dependency | 9 | f1 | 0.709 |
| semantic-transform | 9 | acc | 0.533 |
| Schema-Matching | 9 | f1 | 0.493 |
| semantic-join | 9 | f1 | 0.485 |
| List-to-table | 9 | acc | 0.444 |
| equi-join-detect | 9 | f1 | 0.320 |
| Data-Imputation | 9 | acc | 0.000 |
| String-Relationship | 9 | f1 | 0.000 |
| Table-Locate-by-Row-Col | 9 | acc | 0.000 |
| Arithmetic-Relationship | 9 | f1 | NaN |

## Notes

- 99/99 queries received responses (0 context-limit failures after bumping
  `--max-model-len` to 65536).
- Arithmetic-Relationship NaN is a format mismatch: the evaluator filters
  predictions against `labeled_formulas` and the model's output format doesn't
  match.
- Zero-score tasks (Data-Imputation, String-Relationship, Table-Locate-by-Row-Col)
  reflect model capability limits at 7B scale, not infrastructure issues.
