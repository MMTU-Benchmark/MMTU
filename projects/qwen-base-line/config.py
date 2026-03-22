"""Configuration constants for qwen-base-line project."""

# vLLM server settings
VLLM_BASE_URL = "http://localhost:8000/v1"
VLLM_API_KEY = "EMPTY"  # vLLM default
VLLM_MODEL = "Qwen/Qwen2.5-7B-Instruct"  # HF name — what vLLM expects

# Model alias for filenames (no dots or slashes)
# evaluate.py line 114: model_name = os.path.basename(jsonl_file).split(".")[-3]
MODEL_ALIAS = "Qwen2_5-7B-Instruct"

# Inference settings
TEMPERATURE = 0.0  # Deterministic baseline

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

# Token limits
# LLada comparison: 4096 context, reserve 512 for output → 3584 max input.
MAX_INPUT_TOKENS = 3_584
VLLM_MAX_MODEL_LEN = 4096
