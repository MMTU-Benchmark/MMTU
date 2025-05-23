# MMTU

<!-- |[**🤗 Dataset**](https://huggingface.co/datasets/MMTU-benchmark/MMTU) | [**🏆Leaderboard**]() | [**📖 Paper**]() | -->

|[**🤗 Dataset**](https://huggingface.co/datasets/MMTU-benchmark/MMTU) |

⚠️ Disclaimer:
This benchmark evaluation framework involves automated code execution for certain tasks (e.g., data transformation). While efforts have been made to ensure safety, executing code—especially from external sources—can carry inherent risks. Users are strongly advised to review and understand the code before running it, and to run the evaluation in a secure, isolated environment when possible. Use at your own discretion and risk.

# Table of Contents
- [MMTU](#mmtu)
- [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Leaderboard](#leaderboard)
  - [Evaluate your model](#evaluate-your-model)


## Introduction

MMTU is a large-scale benchmark with over 30K ques12 tions across 25 real-world table tasks, designed to comprehensively evaluate models ability to understand, reason, and manipulate real tables at the expert-level. Thesec tasks are drawn from decades’ worth of computer science research on tabular data, with a focus on complex table tasks faced by professional users.

## Leaderboard 


## Evaluate your model

0. Download data from [OneDrive](https://microsoft-my.sharepoint.com/:f:/p/junjiexing/EqFGfJ01UupJvlcmty70eewBPdSDqtZtaHiWOqcnXTLuJQ?e=t24Sir) and decompression.

1. Setup

```bash
export MMTU_HOME=<PATH-TO-YOUR-DIRECTORY>
```

Install your Python with the required packages.

2. Inference

We support the following API providers: OpenAI, Azure OpenAI and Azure AI Foundry. If you use other services or you are evaluating with your own model, simply implement `self_deploy_query_function()` in [inference.py](https://github.com/MMTU-Benchmark/MMTU/blob/main/inference.py).


Example code for using Azure OpenAI:

```python
python3 inference.py azure_openai \
    --endpoint https://<YOUR_DEPLOYMENT>.openai.azure.com \
    --api_key $AZURE_API_KEY \
    --model gpt-4o \
    --api_version 2024-08-01-preview
```

The code pulls our dataset from HuggingFace🤗 and calls the model completion function. This will result in two `jsonl` files, `mmtu.jsonl` (MMTU in JSONL), and `mmtu.jsonl.<model_name>.result.jsonl`, which contains model responses.


3. Evaluation

Simply run `python3 evaluate.py mmtu.jsonl.<model_name>.result.jsonl`
