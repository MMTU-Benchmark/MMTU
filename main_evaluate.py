import pandas as pd
import os
import argparse
import numpy as np
from datetime import date
import json
from collections import defaultdict
import pickle
import time
import shutil
import utils.utils as utils

from evaluators.nl2sql import NSEvaluator
from evaluators.tableqa_evaluator import TQAEvaluator
from evaluators.tfv_evaluator import TFVEvaluator
from evaluators.ed_evaluator import EDEvaluator
from evaluators.data_transform_pbe_python_evaluator import DTPBEPythonEvaluator
from evaluators.em_evaluator import EMEvaluator
from evaluators.tniah_evaluator import TNIAHEvaluator
from evaluators.tablelocate_evaluator import TableLocateEvaluator
from evaluators.sm_evaluator import SMEvaluator
from evaluators.data_transform_reshape_evaluator import DataTransformReshapeEvaluator
from evaluators.data_imputation_evaluator import DataImputationEvaluator
from evaluators.list_to_table_evaluator import ListToTableEvaluator
from evaluators.formula_context_evaluator import FormulaPredictContextEvaluator
from evaluators.transform_by_output_target_schema_evaluator import TransformByTargetSchemaEvaluator
from evaluators.transform_by_input_output_evaluator import TransformByInputOutputEvaluator
from evaluators.semantic_transform_evaluator import SemanticTransformEvaluator
from evaluators.semantic_join_evaluator import SemanticJoinEvaluator
from evaluators.header_value_match_evaluator import HeaderValueMatchEvaluator
from evaluators.ar_evaluator import AREvaluator
from evaluators.fd_evaluator import FDEvaluator
from evaluators.sr_evaluator import SREvaluator
from evaluators.cta_evaluator import CTAEvaluator
from evaluators.cea_evaluator import CEAEvaluator
from evaluators.cpa_evaluator import CPAEvaluator
from evaluators.ejd_evaluator import EquiJoinDetectEvaluator

    
summary_metric = {
    "NL2SQL": "acc",
    "Table-QA": "acc",
    "Table-Fact-Verification": "acc",
    "Error-Detect": ["prec", "recall", "f1"],
    "Data-transform-pbe": "acc",
    "Entity-Matching": "acc",
    "Table-needle-in-a-haystack": ["acc", "row_acc", "col_acc"],
    "Table-Locate-by-Row-Col": "acc",
    "Schema-Matching": ["prec", "recall", "f1"],
    "Data-transform-reshape": "acc",
    "Data-Imputation": "acc",
    "List-to-table": "acc",
    "Formula-prediction-context": "acc",
    "Transform-by-output-target-schema": "acc",
    "Transform-by-input-output-table": "acc",
    "semantic-transform": "acc",
    "semantic-join": "acc",
    "header-value-matching": "acc",
    "Arithmetic-Relationship": ["prec", "recall", "f1"],
    "Functional-Dependency": ["prec", "recall", "f1"],
    "String-Relationship": ["prec", "recall", "f1"],
    "Cell-entity-annotation": "acc",
    "Column-type-annotation": "acc",
    "Columns-property-anotation": "acc",
    "equi-join-detect": ["prec", "recall", "f1"],
}

evaluator_dict = {
    "NL2SQL": NSEvaluator(),
    "Table-QA": TQAEvaluator(),
    "Table-Fact-Verification": TFVEvaluator(),
    "Error-Detect": EDEvaluator(),
    "Data-transform-pbe": DTPBEPythonEvaluator(),
    "Entity-Matching": EMEvaluator(),
    "Table-needle-in-a-haystack": TNIAHEvaluator(),
    "Table-Locate-by-Row-Col": TableLocateEvaluator(),
    "Schema-Matching": SMEvaluator(),
    "Data-transform-reshape": DataTransformReshapeEvaluator(),
    "Data-Imputation": DataImputationEvaluator(),
    "List-to-table": ListToTableEvaluator(),
    "Formula-prediction-context": FormulaPredictContextEvaluator(),
    "Transform-by-output-target-schema": TransformByTargetSchemaEvaluator(),
    "Transform-by-input-output-table": TransformByInputOutputEvaluator(),
    "semantic-transform": SemanticTransformEvaluator(),
    "semantic-join": SemanticJoinEvaluator(),
    "header-value-matching": HeaderValueMatchEvaluator(),
    "Arithmetic-Relationship": AREvaluator(),
    "Functional-Dependency": FDEvaluator(),
    "String-Relationship": SREvaluator(),
    "Cell-entity-annotation": CEAEvaluator(),
    "Column-type-annotation": CTAEvaluator(),
    "Columns-property-anotation": CPAEvaluator(),
    "equi-join-detect": EquiJoinDetectEvaluator(),
}

def evaluate_dir(result_dir):
    print("Evaluating", result_dir)
    summary_benchmarks = []
    summary_tasks = defaultdict(list)
    avg_results_dict = {} # avg_results_dict[task][model_name]
    detail_results_dict = {} # detail_results_dict[task][model_name]
    error_cnt_dict = {} # error_cnt_dict[task][model_name]

    for subfolder in ["metrics", "summary", "csv", "debug"]:
        if os.path.exists(os.path.join(result_dir, subfolder)):
            shutil.rmtree(os.path.join(result_dir, subfolder))


    for jsonl_file in os.listdir(os.path.join(result_dir, "preds")):
        print("Evaluating", jsonl_file)
        model_name = jsonl_file[:-6]
        if model_name.find(".jsonl") != -1:
            model_name = model_name[model_name.find(".jsonl")+7:]
        model_name = model_name.replace(".result", "")
        preds = pd.read_json(os.path.join(result_dir, "preds", jsonl_file), lines=True)
        if preds.shape[0] == 0:
            print("Empty preds file")
            continue
        preds["task"] = preds["metadata"].apply(lambda x: json.loads(x)["task"])
        
        summary_benchmark_list = []
        for task, preds_group in preds.groupby("task"):
            # if task != "SemanticDedup":
            #     continue
            if task not in avg_results_dict:
                avg_results_dict[task] = defaultdict(list)
                detail_results_dict[task] = defaultdict(list)
                error_cnt_dict[task] = defaultdict(list)
            print(task)
            debug_dir = utils.makedir([result_dir, "debug", task, model_name]) if args.debug else None
            viz_dir = utils.makedir([result_dir, "viz", task, model_name]) if args.viz else None
            evaluator = evaluator_dict[task]
            avg_results, detail_results, error_cnt = evaluator.evaluate(preds_group, debug_dir=debug_dir, viz_dir=viz_dir, n_jobs=args.n_jobs)
            # avg_results.to_excel(utils.makedir([result_dir, "metrics", task], f"{model_name}_avg.xlsx"))
            # detail_results.to_excel(utils.makedir([result_dir, "metrics", task], f"{model_name}_details.xlsx"))
            avg_results_dict[task][model_name].append(avg_results)
            detail_results_dict[task][model_name].append(detail_results)
            if error_cnt is not None:
                error_cnt["model"] = model_name
                error_cnt_dict[task][model_name].append(error_cnt)
            
            if not isinstance(summary_metric[task], list):
                summary_metric[task] = [summary_metric[task]]
            
            summ = []
            for metric in summary_metric[task]:
                summ_metric = avg_results[evaluator.merge_keys + [metric]].rename(columns={metric: f"{model_name}"})
                summ_metric["metric"] = metric
                summ.append(summ_metric)
            summ = pd.concat(summ, axis=0)
            
            # average over benchmark
            summ_benchmark = summ.groupby(["dataset", "tag", "note", "metric"], as_index=False).mean(numeric_only=True)
            summ_benchmark["task"] = task
            summary_benchmark_list.append(summ_benchmark)
            
            # save datasets results
            summ_task = summ.set_index(evaluator.merge_keys + ["metric"])
            summary_tasks[task].append(summ_task)
            
        summary_benchmark_df = pd.concat(summary_benchmark_list, axis=0)
        summary_benchmark_df = summary_benchmark_df.sort_values(by=["task", "dataset", "tag", "note", "metric"]).set_index(["task", "dataset", "tag", "note", "metric"])
        summary_benchmarks.append(summary_benchmark_df)

    for task in avg_results_dict:
        for model in avg_results_dict[task]:
            avg_results_dict[task][model] = pd.concat(avg_results_dict[task][model], axis=0)
            avg_results_dict[task][model].to_excel(utils.makedir([result_dir, "metrics", task], f"{model}_avg.xlsx"))
            detail_results_dict[task][model] = pd.concat(detail_results_dict[task][model], axis=0)
            detail_results_dict[task][model].to_excel(utils.makedir([result_dir, "metrics", task], f"{model}_details.xlsx"))

            error_cnt_dict[task][model] = pd.concat(error_cnt_dict[task][model], axis=0)
            # error_cnt_dict[task][model].to_excel(utils.makedir([result_dir, "metrics", task], f"{model}_error_cnt.xlsx"))
        error_cnt = pd.concat(error_cnt_dict[task].values(), axis=0)
        if error_cnt.shape[0] > 0:
            error_cnt = error_cnt.set_index(["dataset", "tag", "note", "model"])
            error_cnt.to_excel(utils.makedir([result_dir, "summary"], f"{task}_error_cnt.xlsx"))
            error_cnt.to_csv(utils.makedir([result_dir, "csv"], f"{task}_error_cnt.csv"))


    groups = {}
    for df in summary_benchmarks:
        # Using frozenset to ensure the columns can be used as a dictionary key
        key = frozenset(df.columns)
        if key not in groups:
            groups[key] = []
        groups[key].append(df)
    concatenated_dfs = [pd.concat(group, axis=0) for group in groups.values()]

    # def save_tasks_to_excel(df, file_name):
    #     print(df)
    #     with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
    #         for task in df["task"].unique():
    #             task_df = df[df["task"] == task]
    #             task_df.to_excel(writer, sheet_name=str(task), index=False)

    summary_benchmarks = pd.concat(concatenated_dfs, axis=1)
    summary_benchmarks.to_excel(utils.makedir([result_dir, "summary"], f"overall_average.xlsx"))
    summary_benchmarks.to_csv(utils.makedir([result_dir, "csv"], f"overall_average.csv"))
    # save_tasks_to_excel(summary_benchmarks, utils.makedir([result_dir, "summary"], f"overall_average.xlsx"))
    for task, summary in summary_tasks.items():
        res = pd.concat(summary, axis=1)
        res.to_excel(utils.makedir([result_dir, "summary"], f"{task}_summary.xlsx"))
        res.to_csv(utils.makedir([result_dir, "csv"], f"{task}_summary.csv"))
        print(f"------ {task} summary ----")
        print(res.to_markdown(tablefmt="grid"))
    return summary_benchmarks

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("result_dir", type=str)
    parser.add_argument("--n_jobs", default=-1, type=int)
    parser.add_argument("--debug", action="store_true", default=False)
    parser.add_argument("--viz", action="store_true", default=False)
    args = parser.parse_args()


    if args.n_jobs < 0:
        args.n_jobs = os.cpu_count()

    if "preds" in os.listdir(args.result_dir):
        evaluate_dir(args.result_dir)
    else:
        summs = []
        for subfolder in os.listdir(args.result_dir):
            subfolder = os.path.join(args.result_dir, subfolder)
            if not os.path.isdir(subfolder):
                continue
            summ = evaluate_dir(subfolder)
            summs.append(summ)
        summs = pd.concat(summs, axis=0)
        # print(summs)
        excel_filename  = utils.makedir([args.result_dir], f"overall_average.xlsx")
        if os.path.exists(excel_filename):
            os.remove(excel_filename)
        with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as writer:
            # Group by the 'task' column and write each group to a separate sheet
            for task, group in summs.groupby(level=0):
                group.sort_index().to_excel(writer, sheet_name=str(task)[:31])
                # group.to_excel(writer, sheet_name=str(task))
