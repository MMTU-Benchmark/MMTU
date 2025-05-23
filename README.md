# MMTU -- A Massive Multi-Task Table Understanding and Reasoning Benchmark

<!-- |[**🤗 Dataset**](https://huggingface.co/datasets/MMTU-benchmark/MMTU) | [**🏆Leaderboard**]() | [**📖 Paper**]() | -->

|[**🤗 Dataset**](https://huggingface.co/datasets/MMTU-benchmark/MMTU) |

⚠️ **Disclaimer**:
This benchmark involves automated code execution (e.g., for data transformation). While safety precautions are in place, executing code—especially from external sources—carries inherent risks. We strongly recommend reviewing the code before running and executing in a secure, isolated environment. Use at your own discretion.

## 📚 Table of Contents
- [Introduction](#introduction)
- [Leaderboard](#leaderboard)
- [Evaluate Your Model](#evaluate-your-model)


## 🧠 Introduction

**MMTU** is a large-scale benchmark designed to evaluate the table reasoning capabilities of large language models (LLMs). It consists of over **30,000 questions** across **25 real-world table tasks**, focusing on deep understanding, reasoning, and manipulation of tabular data.

These tasks are curated from decades of computer science research and represent challenges encountered by expert users in real applications, making MMTU a rigorous test for LLMs aspiring to professional-level table understanding.


## 🏆 Leaderboard

*Coming Soon*


## 🚀 Evaluate Your Model

### Step 0: Download the Data

Download the original data from [OneDrive](https://microsoft-my.sharepoint.com/:f:/p/junjiexing/EqFGfJ01UupJvlcmty70eewBPdSDqtZtaHiWOqcnXTLuJQ?e=t24Sir) and extract the contents.

### Step 1: Set Up Environment

```bash
export MMTU_HOME=<YOUR_DIRECTORY_PATH>
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 2: Run Inference

MMTU supports the following API providers:
- OpenAI
- Azure OpenAI
- Azure AI Foundry

To use a custom or self-hosted model, implement the `self_deploy_query_function()` in [`inference.py`](https://github.com/MMTU-Benchmark/MMTU/blob/main/inference.py).

Example using Azure OpenAI:

```bash
python3 inference.py azure_openai \
    --endpoint https://<YOUR_DEPLOYMENT>.openai.azure.com \
    --api_key $AZURE_API_KEY \
    --model <MODEL_NAME> \
    --api_version 2024-08-01-preview
```

This step will:

- Download the dataset from Hugging Face 🤗
- Use the specified model to generate responses for each task
- Save two output files:
  - `mmtu.jsonl`: the evaluation dataset in JSONL format
  - `mmtu.jsonl.<MODEL_NAME>.result.jsonl`: the model’s responses to each task

### Step 3: Evaluation

After inference, evaluate your model’s outputs with:

```python
python3 evaluate.py mmtu.jsonl.<MODEL_NAME>.result.jsonl
```

This script will compute performance metrics for your model on the MMTU benchmark.