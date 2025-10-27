# MMTU -- A Massive Multi-Task Table Understanding and Reasoning Benchmark

<!-- |[**🤗 Dataset**](https://huggingface.co/datasets/MMTU-benchmark/MMTU) | [**🏆Leaderboard**]() | [**📖 Paper**](https://arxiv.org/abs/2506.05587) | -->

|[**🤗 Dataset**](https://huggingface.co/datasets/MMTU-benchmark/MMTU) |[**🏆Leaderboard**](#-leaderboard) |[**📖 Paper**](https://arxiv.org/abs/2506.05587) |

This repo contains the evaluation code for the NeurIPS'25 benchmark paper "[MMTU: A Massive Multi-Task Table Understanding and Reasoning Benchmark](https://arxiv.org/abs/2506.05587)".

## Update • October 2025

During the rebuttal period, we performed an LLM-based filtering process. After filtering, the number of questions in **MMTU** has been reduced from **30,647** to **28,136**.

For more information, please check:
- 📄 Our **paper**: <https://arxiv.org/abs/2506.05587>
- 🤗 The updated **dataset**: <https://huggingface.co/datasets/MMTU-benchmark/MMTU>
- 🏆 The refreshed **leaderboard**: [Jump to Leaderboard](#-leaderboard)

## 📚 Table of Contents
- [Introduction](#-introduction)
- [Leaderboard](#-leaderboard)
- [Evaluate Your Model](#-evaluate-your-model)
  -  [Alternative: Evaluation with Docker](#step-3-alternative-evaluation-with-docker)
- [Extension](#-extension-customizing-table-tasks-prompts-and-evaluation)


## 🧠 Introduction

Tables and table-based use cases play a crucial role in many real-world applications, such as spreadsheets, databases, and computational notebooks, which traditionally require expert-level users like data engineers, analysts, and database administrators to operate. Although LLMs have shown remarkable progress in working with tables, comprehensive benchmarking of such capabilities remains limited, often narrowly focusing on tasks like NL-to-SQL and Table-QA, while overlooking the broader spectrum of real-world tasks that professional users face today. 

We introduce **MMTU**, a large-scale benchmark with around **28K questions** across **25 real-world table tasks**, designed to comprehensively evaluate models ability to understand, reason, and manipulate real tables at the expert-level. These tasks are drawn from decades' worth of computer science research on tabular data, with a focus on complex table tasks faced by professional users. We show that MMTU require a combination of skills -- including table understanding, reasoning, and coding -- that remain challenging for today's frontier models, where even frontier reasoning models like OpenAI o4-mini and DeepSeek R1 score only around 60%, suggesting significant room for improvement. 

<img width="839" alt="mmtu" src="https://github.com/user-attachments/assets/95dd2a05-755e-40cf-a6cb-9d2953394241" />


## 🛠️ Dataset Creation
MMTU was developed through the meticulous curation of 52 datasets across 25 task categories, each carefully labeled by computer science researchers, in decades’ worth of research on tabular data from communities such as data management (SIGMOD/VLDB), programming languages (PLDI/POPL), and web data (WWW/WSDM).  The benchmark emphasizes real-world, complex table tasks encountered by professional users—tasks that demand advanced skills in table understanding, coding, and reasoning. Plesae see the table below for key statistics of the benchmark, and please visit our 🤗 [Dataset](https://huggingface.co/datasets/MMTU-benchmark/MMTU) page for additional details.

<div align="center">
  <img src="https://github.com/user-attachments/assets/f6410469-6a7a-44d9-843e-c6acf19278bc" width="400"/>
</div>


## 🏆 Leaderboard

Below is a portion of our evaluation results. For the complete leaderboard and additional details, please visit the **[MMTU Leaderboard](https://huggingface.co/datasets/MMTU-benchmark/MMTU)**.


| **Model Type** | **Model**           | **MMTU Score**     | 
|----------------|---------------------|----------------------|
| Reasoning      | GPT-5               | **0.696 ± 0.01**     |
| Reasoning      | o3                  | 0.691 ± 0.01         |
| Reasoning      | GPT-5-mini          | 0.667 ± 0.01         |
| Reasoning      | Gemini-2.5-Pro      | 0.665 ± 0.01         |
| Reasoning      | o4-mini (2024-11-20)| 0.660 ± 0.01         |
| Reasoning      | Deepseek-R1         | 0.597 ± 0.01         |
| Chat           | GPT-5-Chat          | 0.577 ± 0.01         |
| Chat           | Deepseek-V3         | 0.555 ± 0.01         |
| Chat           | GPT-4o (2024-11-20) | 0.507 ± 0.01         |
| Chat           | Llama-3.3-70B       | 0.454 ± 0.01         |
| Chat           | Mistral-Large-2411  | 0.446 ± 0.01         |
| Chat           | Mistral-Small-2503  | 0.417 ± 0.01         |
| Chat           | GPT-4o-mini (2024-07-18)| 0.400 ± 0.01         |



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

### Step 3 (Alternative): Evaluation with Docker

This directory contains Docker configuration files to run the `evaluate.py` script in an isolated container environment.

Please make sure that Docker is installed and is executable without root.

```bash
# Make the script executable (if not already done)
chmod +x run_evaluate_docker.sh

# Run evaluation on a result file
./run_evaluate_docker.sh mmtu.jsonl.<MODEL_NAME>.result.jsonl
```
## 🔧 Extension: Customizing Table Tasks, Prompts, and Evaluation

Our framework is designed to be easily extensible. You can add new table tasks, customize prompt templates, and define your own evaluation metrics with minimal effort.

✨ Customizing Prompt Templates

To modify the prompt template for a specific task (e.g., NL2SQL), simply update the prompt_template in the corresponding configuration file.

1. Open the file: `configurations/NL2SQL/v1.0/ns_singletable_v1.0_sample1000_markdown.py`
2. Modify the `prompt_template` as desired.
3. Regenerate the prompts by running:

```bash
python3 build_data.py one --config configurations/NL2SQL/v1.0/ns_singletable_v1.0_sample1000_markdown.py
```
🧪 Adding Custom Evaluation Metrics
To introduce new evaluation metrics for a task (e.g., NL2SQL), modify the _evaluate_one method in the relevant evaluator class.

For example:

- Edit the `NSEvaluator` class in `evaluators/nl2sql.py`
- Update the `_evaluate_one` function to include your custom metric logic.

## Citation


```bibtex
@article{mmtu,
  title={{MMTU}: A Massive Multi-Task Table Understanding and Reasoning Benchmark},
  author={Junjie Xing and Yeye He and Mengyu Zhou and Haoyu Dong and Shi Han and Lingjiao Chen and Dongmei Zhang and Surajit Chaudhuri and H. V. Jagadish},
  journal={arXiv preprint arXiv:2506.05587},
  year={2025}
}
```
