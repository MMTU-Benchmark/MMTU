# MMTU -- A Massive Multi-Task Table Understanding and Reasoning Benchmark

<!-- |[**🤗 Dataset**](https://huggingface.co/datasets/MMTU-benchmark/MMTU) | [**🏆Leaderboard**]() | [**📖 Paper**](https://arxiv.org/abs/2506.05587) | -->

|[**🤗 Dataset**](https://huggingface.co/datasets/MMTU-benchmark/MMTU) |[**🏆Leaderboard**](https://github.com/MMTU-Benchmark/MMTU/edit/main/README.md#-leaderboard)|[**📖 Paper**](https://arxiv.org/abs/2506.05587) |

This repo contains the evaluation code for the paper "[MMTU: A Massive Multi-Task Table Understanding and Reasoning Benchmark](https://arxiv.org/abs/2506.05587)" 


## 📚 Table of Contents
- [Introduction](#introduction)
- [Leaderboard](#leaderboard)
- [Evaluate Your Model](#evaluate-your-model)


## 🧠 Introduction

Tables and table-based use cases play a crucial role in many real-world applications, such as spreadsheets, databases, and computational notebooks, which traditionally require expert-level users like data engineers, analysts, and database administrators to operate. Although LLMs have shown remarkable progress in working with tables, comprehensive benchmarking of such capabilities remains limited, often narrowly focusing on tasks like NL-to-SQL and Table-QA, while overlooking the broader spectrum of real-world tasks that professional users face today. 

We introduce **MMTU**, a large-scale benchmark with over **30K questions** across **25 real-world table tasks**, designed to comprehensively evaluate models ability to understand, reason, and manipulate real tables at the expert-level. These tasks are drawn from decades' worth of computer science research on tabular data, with a focus on complex table tasks faced by professional users. We show that MMTU require a combination of skills -- including table understanding, reasoning, and coding -- that remain challenging for today's frontier models, where even frontier reasoning models like OpenAI o4-mini and DeepSeek R1 score only around 60%, suggesting significant room for improvement. 

<img width="839" alt="mmtu" src="https://github.com/user-attachments/assets/95dd2a05-755e-40cf-a6cb-9d2953394241" />


## 🛠️ Dataset Creation
MMTU was developed through the meticulous curation of 52 datasets across 25 task categories, each carefully labeled by computer science researchers, in decades’ worth of research on tabular data from communities such as data management (SIGMOD/VLDB), programming languages (PLDI/POPL), and web data (WWW/WSDM).  The benchmark emphasizes real-world, complex table tasks encountered by professional users—tasks that demand advanced skills in table understanding, coding, and reasoning. Plesae see the table below for key statistics of the benchmark, and please visit our 🤗 [Dataset](https://huggingface.co/datasets/MMTU-benchmark/MMTU) page for additional details.

<div align="center">
  <img src="https://github.com/user-attachments/assets/fc59e5fc-964b-4716-8e31-657edbdd7edb" width="400"/>
</div>

## 🏆 Leaderboard

*Coming Soon*


## 🚀 Evaluate Your Model

⚠️ This benchmark involves automated code execution for some complex table tasks (e.g., for NL-2-SQL and data transformation). We recommend executing model-generated code in an isolated sandbox environment.


### Step 0: Download the Data

Download the original data from [OneDrive](https://1drv.ms/f/c/4eea81351af2d84b/Em8WdXGOGwBFnx92aN8ZKNEBYLCkJlkwzZYTlmkx3jUykg?e=pBb24n) and extract the contents.

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
