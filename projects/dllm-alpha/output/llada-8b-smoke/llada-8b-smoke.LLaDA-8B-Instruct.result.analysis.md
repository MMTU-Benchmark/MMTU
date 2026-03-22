# Analysis: llada-8b-smoke

**Result file:** `llada-8b-smoke.LLaDA-8B-Instruct.result.jsonl`  
**Samples:** 25

## Per-Question Metadata

| # | Task | Test Case | Input Tok | Output Tok | Metric | Score |
|---|---|---|---|---|---|---|
| 1 | Formula-prediction-context | case-556 | 1332 | 7 | acc | 0.00 |
| 2 | Formula-prediction-context | case-7 | 1058 | 13 | acc | 0.00 |
| 3 | Arithmetic-Relationship | case_448 | 3530 | 462 | f1 | 0.000 |
| 4 | Formula-prediction-context | case-958 | 1049 | 14 | acc | 0.00 |
| 5 | Formula-prediction-context | case-594 | 1083 | 11 | acc | 0.00 |
| 6 | Formula-prediction-context | case-100 | 2074 | 343 | acc | 0.00 |
| 7 | Formula-prediction-context | case-21 | 1651 | 13 | acc | 0.00 |
| 8 | Formula-prediction-context | case-486 | 1167 | 8 | acc | 0.00 |
| 9 | Formula-prediction-context | case-978 | 1736 | 207 | acc | 0.00 |
| 10 | Formula-prediction-context | case-481 | 1484 | 15 | acc | 0.00 |
| 11 | Formula-prediction-context | case-538 | 505 | 15 | acc | 0.00 |
| 12 | Formula-prediction-context | case-324 | 923 | 10 | acc | 0.00 |
| 13 | Formula-prediction-context | case-659 | 1791 | 8 | acc | 0.00 |
| 14 | Formula-prediction-context | case-84 | 720 | 16 | acc | 0.00 |
| 15 | Data-transform-reshape | transpose_test9 | 735 | 145 | acc | 0.00 |
| 16 | Formula-prediction-context | case-280 | 1191 | 14 | acc | 0.00 |
| 17 | Formula-prediction-context | case-560 | 1302 | 16 | acc | 0.00 |
| 18 | Arithmetic-Relationship | case_534 | 3138 | 448 | f1 | 0.000 |
| 19 | Arithmetic-Relationship | case_522 | 2891 | 441 | f1 | 0.000 |
| 20 | Formula-prediction-context | case-660 | 1485 | 15 | acc | 0.00 |
| 21 | Formula-prediction-context | case-829 | 1958 | 15 | acc | 0.00 |
| 22 | Formula-prediction-context | case-857 | 1090 | 9 | acc | 0.00 |
| 23 | Formula-prediction-context | case-932 | 1241 | 16 | acc | 0.00 |
| 24 | Formula-prediction-context | case-209 | 1652 | 363 | acc | 0.00 |
| 25 | Arithmetic-Relationship | case_462 | 3470 | 502 | f1 | 0.000 |

## Score Summary by Task

| Task | Metric | N | Mean Score | Perfect (=1.0) | Zero (=0.0) |
|---|---|---|---|---|---|
| Arithmetic-Relationship | f1 | 4 | 0.000 | 0/4 | 4/4 |
| Data-transform-reshape | acc | 1 | 0.000 | 0/1 | 1/1 |
| Formula-prediction-context | acc | 20 | 0.000 | 0/20 | 20/20 |

**Overall mean score:** 0.000

## Input Token Length Distribution

### Input Tokens

| Range | Count | Distribution |
|---|---|---|
| 505–808 | 3 | ██████████████████ |
| 808–1110 | 5 | ██████████████████████████████ |
| 1110–1412 | 5 | ██████████████████████████████ |
| 1412–1715 | 4 | ████████████████████████ |
| 1715–2018 | 3 | ██████████████████ |
| 2018–2320 | 1 | ██████ |
| 2320–2622 | 0 |  |
| 2622–2925 | 1 | ██████ |
| 2925–3228 | 1 | ██████ |
| 3228–3530 | 2 | ████████████ |

**Total:** 25 | **Mean:** 1610.2 | **Median:** 1332.0 | **Min:** 505 | **Max:** 3530

## Output Token Length Distribution

### Output Tokens

| Range | Count | Distribution |
|---|---|---|
| 7–56 | 17 | ██████████████████████████████ |
| 56–106 | 0 |  |
| 106–156 | 1 | ██ |
| 156–205 | 0 |  |
| 205–254 | 1 | ██ |
| 254–304 | 0 |  |
| 304–354 | 1 | ██ |
| 354–403 | 1 | ██ |
| 403–452 | 2 | ████ |
| 452–502 | 2 | ████ |

**Total:** 25 | **Mean:** 125.0 | **Median:** 15.0 | **Min:** 7 | **Max:** 502

## Per-Task Token Statistics

| Task | N | Input Mean | Input Med | Output Mean | Output Med |
|---|---|---|---|---|---|
| Arithmetic-Relationship | 4 | 3257 | 3304 | 463 | 455 |
| Data-transform-reshape | 1 | 735 | 735 | 145 | 145 |
| Formula-prediction-context | 20 | 1325 | 1272 | 56 | 14 |
