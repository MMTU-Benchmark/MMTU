import pandas as pd
import numpy as np
import os
import re
import json
import shutil
import tiktoken
from tqdm import tqdm
from multiprocessing import Pool, cpu_count


def colortext(text, color="white"):
    colors = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }
    return colors[color] + text + colors["reset"]


class Template:
    def __init__(self, template):
        self.template = template

    def check(self):
        """Check if the template is valid."""
        try:
            # Use a regex to find all placeholders in the template
            placeholders = re.findall(r"\{\{\{(.*?)\}\}\}", self.template)
            # Ensure all placeholders are valid identifiers
            for placeholder in placeholders:
                if not placeholder.isidentifier():
                    return False
            return True
        except Exception as e:
            return False

    def instantiate(self, data):
        """Instantiate the template with the given data dictionary."""
        try:
            # Use a regex to find all placeholders in the template
            placeholders = re.findall(r"\{\{\{(.*?)\}\}\}", self.template)

            # Replace placeholders with data if key exists, else keep the placeholder
            result = self.template
            for placeholder in placeholders:
                if placeholder in data:
                    result = result.replace("{{{" + placeholder + "}}}", data[placeholder])

            return result
        except Exception as e:
            return f"An error occurred: {e}"

def config_sanity_check(config_file):
    """Check if the configuration file is valid."""
    with open(config_file, "r") as f:
        context = {}
        exec(f.read(), context)

    assert "prompt_template" in context
    assert "dataset_config" in context

    template = Template(context["prompt_template"])
    assert template.check()

    dataset_config = context["dataset_config"]
    assert "task" in dataset_config
    assert "version" in dataset_config
    assert "path" in dataset_config
    assert "fields" in dataset_config

    for field in dataset_config["fields"].values():
        assert "type" in field
        if field["type"] == "table.csv":
            assert "path" in field
            assert "serializer" in field
        elif field["type"] == "list":
            assert "template" in field
            assert "fields" in field

# Load tokenizer
def count_tokens(text, model="gpt-4o"):
    if len(text) > 128000*5:
        return np.inf
    encoder = tiktoken.encoding_for_model(model)
    tokens = encoder.encode(text)
    return len(tokens)

def count_tokens_mp(prompt_lists, model="gpt-4o", num_processes=cpu_count()):
    num_processes = min(num_processes, cpu_count())
    encoder = tiktoken.encoding_for_model(model)
    tokens = encoder.encode_batch(prompt_lists, num_threads=num_processes)
    num_tokens = [len(token) for token in tokens]
    return num_tokens


def parallelize_dataframe(df, func, num_processes=cpu_count()):
        num_processes = min(num_processes, cpu_count())
        print(f"Using {num_processes} processes")
        df_split = np.array_split(df, num_processes)
        with Pool(num_processes) as p:
            df = pd.concat(p.map(func, df_split))
        return df

def parallelize_token_count(df):
    df["token_count"] = df["prompt"].apply(lambda x: count_tokens(x, model="gpt-4o"))
    return df

def multiprocess_token_count(prompt_lists, num_processes=cpu_count()):
    num_processes = min(num_processes, cpu_count())
    print(f"Using {num_processes} processes to count tokens")
    with Pool(num_processes) as p:
        results = p.map(count_tokens, prompt_lists)
    return results


def process(template: Template, fields_config: dict, info: dict, current_path: str):
    data = {}
    for field, field_config in fields_config.items():
        if field_config["type"] == "table.csv":
            if field_config["reader"] == "pandas":
                df = pd.read_csv(os.path.join(current_path, field_config["path"]), keep_default_na=False)
            elif field_config["reader"] == "pandas.str":
                df = pd.read_csv(os.path.join(current_path, field_config["path"]), keep_default_na=False, dtype=str)
            elif field_config["reader"] == "pandas.w_idx":
                df = pd.read_csv(os.path.join(current_path, field_config["path"]), keep_default_na=False, dtype=str, index_col=0)
            elif field_config["reader"] == "pandas.no_header":
                df = pd.read_csv(os.path.join(current_path, field_config["path"]), header=None, keep_default_na=False)
            else:
                raise NotImplementedError(f"Reader {field_config['reader']} not implemented")

            table_processors = field_config.get("processors", [])
            for processor in table_processors:
                df = processor.process(df)
                
            serializer = field_config["serializer"]()
            data[field] = serializer.serialize_df(df)
        elif field_config["type"] == "text":
            if field_config["name"] in info:
                data[field] = str(info[field_config["name"]])
            else:
                print(f"Field {field_config['name']} not found in info.json")
        elif field_config["type"] == "table.csv.path":
            try:
                if field_config["reader"] == "pandas":
                    df = pd.read_csv(os.path.join(current_path, info[field]), keep_default_na=False)
                elif field_config["reader"] == "pandas.w_idx":
                    df = pd.read_csv(os.path.join(current_path, info[field]), keep_default_na=False, index_col=0)
                elif field_config["reader"] == "pandas.no_header":
                    df = pd.read_csv(os.path.join(current_path, info[field]), header=None, keep_default_na=False)
                else:
                    raise NotImplementedError(f"Reader {field_config['reader']} not implemented")
            except pd.errors.EmptyDataError:
                df = pd.DataFrame()
            except pd.errors.ParserError:
                if field_config["reader"] == "pandas":
                    df = pd.read_csv(os.path.join(current_path, info[field]), keep_default_na=False, nrows=100)
                elif field_config["reader"] == "pandas.w_idx":
                    df = pd.read_csv(os.path.join(current_path, info[field]), keep_default_na=False, index_col=0)
                elif field_config["reader"] == "pandas.no_header":
                    df = pd.read_csv(os.path.join(current_path, info[field]), header=None, keep_default_na=False)
                else:
                    raise NotImplementedError(f"Reader {field_config['reader']} not implemented")
            except Exception as e:
                raise e

            table_processors = field_config.get("processors", [])
            for processor in table_processors:
                df = processor.process(df)
                
            serializer = field_config["serializer"]()
            data[field] = serializer.serialize_df(df)
        elif field_config["type"] == "list":
            assert "template" in field_config
            assert "fields" in field_config
            items = [process(Template(field_config["template"]), field_config["fields"], item, current_path) for item in info[field]]
            data[field] = "\n".join(items)
        elif field_config["type"] == "fewshot":
            assert "template" in field_config
            assert "fields" in field_config
            assert "path" in field_config
            fewshot_path = os.path.join(current_path, field_config["path"])
            assert os.path.exists(fewshot_path), f"Fewshot path {fewshot_path} does not exist"
            items = []
            for fewshots_subdir in os.listdir(fewshot_path):
                fewshot_subdir_path = os.path.join(fewshot_path, fewshots_subdir)
                if not os.path.isdir(fewshot_subdir_path):
                    continue
                info = {}
                with open(os.path.join(fewshot_subdir_path, field_config["info"]), "r") as f:
                    info = json.load(f)
                items.append(process(Template(field_config["template"]), field_config["fields"], info, fewshot_subdir_path))
            data[field] = "\n".join(items)
        else:
            raise ValueError(f"Invalid field type: {field_config['type']}")

    prompt = template.instantiate(data)
    return prompt

def process_case(args):
        template, dataset_config, dataset, case_dir, dataset_path = args
        case_path = os.path.join(dataset_path, case_dir)
        if not os.path.isdir(case_path):
            return None, None, None

        info = {}
        if "info" in dataset_config:
            with open(os.path.join(case_path, dataset_config["info"]), "r") as f:
                info = json.load(f)

        fields_config = dataset_config.get(f"{dataset.lower()}_fields", dataset_config["fields"])
        
        try:
            prompt = process(template, fields_config, info, case_path)
            mmtu_home = os.environ["MMTU_HOME"]
            case_dir = case_dir.replace(mmtu_home, "$MMTU_HOME")
            case_path = case_path.replace(mmtu_home, "$MMTU_HOME")
            metadata = {
                "task": dataset_config["task"],
                "version": dataset_config["version"],
                "tag": dataset_config.get("tag", "") if isinstance(dataset_config.get("tag", ""), str) else dataset_config["tag"][0],
                "note": dataset_config.get("note", ""),
                "dataset": dataset,
                "test_case": case_dir,
                "case_path": case_path,
            }
            metadata.update(info)
        except Exception as e:
            print(f"Error processing case {case_dir}: {e}")
            return None, None, None

        return prompt, json.dumps(metadata), dataset

def build_data(config_file, num_workers=cpu_count(), debug=False, token_limit=64000, bypass=False, args_tag="", test=False, test_engines=[]):
    """Build data from configuration python file."""
    try:
        config_sanity_check(config_file)
    except Exception as e:
        print(f"Invalid configuration file: {e}")
        return "", pd.DataFrame(), pd.DataFrame(), ""
    print(f"Building data from {config_file}")
    context = {}
    with open(config_file, "r") as f:
        exec(f.read(), context)

    assert "prompt_template" in context
    prompt_template = context["prompt_template"]
    assert "dataset_config" in context
    dataset_config = context["dataset_config"]
    assert "tag" in dataset_config
    dataset_tag = dataset_config["tag"]
    dataset_version = dataset_config["version"]
    if not args_tag:
        args_tag = dataset_version

    template = Template(prompt_template)
    
    # save_dir = f"datasets_prompt/{dataset_config['task']}/v{dataset_config['version']}"
    save_dir = f"{args_tag}/{dataset_config['task']}/{dataset_config['version']}/{token_limit}"
    if debug:
        save_dir = os.path.join("datasets_prompt", "debug", save_dir)
    else:
        save_dir = os.path.join("datasets_prompt", save_dir)
    if os.path.exists(save_dir) and not debug:
        if bypass:
            shutil.rmtree(save_dir)
        else:
            print(f"Directory {save_dir} already exists. Do you want to overwrite it? (y/n)")
            choice = input().strip().lower()
            if choice != "y":
                return "", pd.DataFrame(), pd.DataFrame(), ""
            else:
                shutil.rmtree(save_dir)
    os.makedirs(save_dir, exist_ok=True)

    prompts = []
    metadatas = []
    datasets = []

    for dataset in os.listdir(dataset_config["path"]):
        dataset_path = os.path.join(dataset_config["path"], dataset)
        if not os.path.isdir(dataset_path):
            continue

        case_dirs = [case_dir for case_dir in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, case_dir))]
        args = [(template, dataset_config, dataset, case_dir, dataset_path) for case_dir in case_dirs]

        if debug:
            import random
            random.seed(42)
            args = random.sample(args, 25) if len(args) > 25 else args

        with Pool(min(cpu_count(), num_workers)) as pool:
            for prompt, metadata, dataset in tqdm(pool.imap_unordered(process_case, args), desc=f"Processing {dataset}", ncols=80, total=len(args)):
                if prompt is not None:
                    prompts.append(prompt)
                    metadatas.append(metadata)
                    datasets.append(dataset)

    df_prompts = pd.DataFrame({"prompt": prompts, "metadata": metadatas, "dataset": datasets})

    # Define token limit
    tqdm.pandas()

    from time import time
    start = time()
    print(colortext("\nCounting tokens...", color="red"))
    # df_prompts = parallelize_dataframe(df_prompts, parallelize_token_count, num_processes=num_workers)
    # df_prompts["token_count"] = multiprocess_token_count(df_prompts["prompt"].tolist(), num_processes=num_workers)
    # df_prompts["token_count"] = count_tokens_mp(df_prompts["prompt"].tolist(), num_processes=num_workers)
    df_prompts["token_count"] = df_prompts["prompt"].progress_apply(lambda x: count_tokens(x, model="gpt-35-turbo"))

    # Split DataFrame
    valid_df = df_prompts[df_prompts["token_count"] <= token_limit].copy()
    invalid_df = df_prompts[df_prompts["token_count"] > token_limit].copy()
    df_prompts["token_count_valid"] = df_prompts["token_count"] <= token_limit

    save_to = f"{dataset_config['task']}_{dataset_config['version']}_{token_limit}"

    if debug:
        save_to += "_debug"

    save_to_valid = os.path.join(save_dir, f"{save_to}_valid_size{len(valid_df)}.jsonl")
    save_to_valid_batch = os.path.join(save_dir, f"{save_to}_valid_size{len(valid_df)}_batch.jsonl")
    valid_df[["prompt", "metadata"]].to_json(save_to_valid, orient="records", lines=True)
    
    valid_df_batch = valid_df[["prompt", "metadata"]]
    print(valid_df_batch.head())
    # valid_df_batch["messages"] = valid_df_batch.apply(lambda x: [
    #         # {"role": "system", "content": "You are an AI assistant. Provide an answer to some data/table related questions."},
    #         {"role": "user", "content": x['prompt']},
    #     ], axis=1)
    print(valid_df_batch.columns)
    assert "prompt" in valid_df_batch.columns
    valid_df_batch["body"] = valid_df_batch.apply(lambda x:{
        "model": "gpt-4o-batch",
        "messages": [
            {"role": "user", "content": x['prompt']}
        ]
    }, axis=1)
    valid_df_batch["method"] = "POST"
    valid_df_batch["url"] = "/chat/completions"
    # valid_df_batch["custom_id"] = valid_df_batch.apply(lambda x: json.loads(x['metadata'])['test_case'], axis=1)
    # valid_df_batch[["custom_id", "method", "url", "body"]].to_json(save_to_valid_batch, orient="records", lines=True)
    valid_df_batch["custom_id"] = valid_df_batch["metadata"]
    valid_df_batch[["custom_id", "method", "url", "body"]].to_json(save_to_valid_batch, orient="records", lines=True)
    

    if len(invalid_df) > 0:
        save_to_invalid = os.path.join(save_dir, f"{save_to}_invalid_size{len(invalid_df)}.jsonl")
        invalid_df[["prompt", "metadata"]].to_json(save_to_invalid, orient="records", lines=True)

    for dataset in valid_df["dataset"].unique():
        print(colortext(f"\nDataset: {dataset}", color="green"))

        print("\nExample prompt:")
        print(">>>>>>>>>>>>>>>>>")
        # print the row with the smallest token count
        prompt_test = valid_df[valid_df["dataset"] == dataset].sort_values("token_count").head(1).reset_index(drop=True)["prompt"][0]
        print(prompt_test)
        # print(valid_df[valid_df["dataset"] == dataset].sample(1, random_state=42).reset_index(drop=True)["prompt"][0])
        print("<<<<<<<<<<<<<<<<<")

        print("\nExample metadata:")
        print(">>>>>>>>>>>>>>>>>")
        # print the row with the smallest token count
        print(valid_df[valid_df["dataset"] == dataset].sort_values("token_count").head(1).reset_index(drop=True)["metadata"][0])
        # print(valid_df[valid_df["dataset"] == dataset].sample(1, random_state=42).reset_index(drop=True)["metadata"][0])
        print("<<<<<<<<<<<<<<<<<")
        
        if test:
            from inference import get_query_func
            print("\nTesting the Prompt:")
            for engine in test_engines:
                query_funcs, model_name = get_query_func(engine)
                query_func = query_funcs[0]
                print(colortext(f"\n>>>>>>>>{model_name}>>>>>>>>>", color="red"))
                # print the row with the smallest token count
                print(query_func(prompt_test, 0))
                # print(valid_df[valid_df["dataset"] == dataset].sample(1, random_state=42).reset_index(drop=True)["metadata"][0])
                print("<<<<<<<<<<<<<<<<<")
                

    shutil.copy(config_file, os.path.join(save_dir, "config.py"))

    print(f"\nToken count took {time() - start:.2f} seconds")
    
    # print number of items per dataset
    result = df_prompts.groupby('dataset')['token_count_valid'].agg([ 
            ('valid_count', lambda x: (x == True).sum()),
            ('invalid_count', lambda x: (x == False).sum()),
            ('valid_rate', lambda x: (x == True).mean())
        ]).reset_index() # type: ignore

    # Calculate totals
    total_row = pd.DataFrame({
        'dataset': ['TOTAL'],
        'valid_count': [result['valid_count'].sum()],
        'invalid_count': [result['invalid_count'].sum()],
        'valid_rate': [result['valid_count'].sum() / (result['valid_count'].sum() + result['invalid_count'].sum())]
    })

    # Append the total row to the result
    result = pd.concat([result, total_row], ignore_index=True)
    print(result.to_markdown(index=False))

    # Plot histograms for each dataset
    datasets = df_prompts['dataset'].unique()

    bins = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 
        100000, 110000, 120000, np.inf]
    bin_labels = ["<10K", "10K-20K", "20K-30K", "30K-40K", "40K-50K", "50K-60K", "60K-70K", "70K-80K", "80K-90K", "90K-100K", "100K-110K", "110K-120K", ">120K"]

    bin_count = []

    for dataset in datasets:
        subset = df_prompts[df_prompts['dataset'] == dataset]['token_count']
        counts, _ = np.histogram(subset, bins=bins)
        bin_count.append([dataset] + list(counts))
    bin_count_df = pd.DataFrame(bin_count, columns=['dataset'] + bin_labels)
    print("\nToken count distribution by dataset:")
    print(bin_count_df.to_markdown(index=False))
    
    print(f"\nData saved to {save_to_valid}")
    
    return dataset_config['task'], result, bin_count_df, save_to_valid


def find_python_files(root_dir):
    python_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith(".py"):
                python_files.append(os.path.join(dirpath, file))
    return python_files


def check_file_tags(python_file, tag):
    with open(python_file, "r") as f:
        context = {}
        try:
            exec(f.read(), context)
        except Exception as e:
            print(f"Error executing {python_file}: {e}")
            raise e
    dataset_config = context["dataset_config"]
    config_tags = dataset_config.get("tag", [])
    if type(config_tags) == str:
        config_tags = [config_tags]
    return tag in config_tags


def build_batch(args):
    assert os.path.isdir(args.config[0]), f"Configuration directory not found: {args.config[0]}"
    assert args.tag, "Tag is required for batch processing."
    
    root_directory = args.config[0]
    python_files = find_python_files(root_directory)
    
    tagged_files = [python_file for python_file in python_files if check_file_tags(python_file, args.tag)]
    print(f"Found {len(tagged_files)} files with tag {args.tag}:")
    print("\t" + "\n\t".join(tagged_files))
    
    confirmation = input("Do you want to build data for these files? (y/n)")
    if confirmation.strip().lower() != "y":
        return
    
    stats = []
    for python_file in tagged_files:
        task, cnt_stat, bin_stat, save_to = build_data(python_file, num_workers=args.num_workers, debug=args.debug, token_limit=args.token_limit, bypass=args.y, args_tag=args.tag, test=args.test, test_engines=args.test_engines)
        stats.append((task, python_file, cnt_stat, bin_stat, save_to))
    
    print(colortext("\nSummary:", color="red"))
    for task, python_file, cnt_stat, bin_stat, save_to in stats:
        print(colortext(f"\nConfiguration file: {python_file}", color="blue"))
        print(colortext(f"\nTask: {task}", color="green"))
        print(cnt_stat.to_markdown(index=False))
        print("\nToken count distribution by dataset:")
        print(bin_stat.to_markdown(index=False))
        print(f"\nData saved to {save_to}")
        assert os.path.exists(save_to), f"Data not saved to {save_to}"
        
    print("To query \npython3 queryWithDeployment.py", " ".join([save_to for _, _, _, _, save_to in stats]), "-n 4 -e gpt-4o")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("cmd", type=str, choices=["one", "batch"], help="Command to run.")
    parser.add_argument("--config", type=str, required=True, help="Path to the configuration python file.", nargs="+")
    parser.add_argument("--num_workers", "-n", type=int, default=cpu_count(), help="Number of workers to use.")
    parser.add_argument("--debug", action="store_true", help="Debug mode. Sample 25 cases per dataset.")
    parser.add_argument("--test", action="store_true", help="Test the example prompt.")
    parser.add_argument("--test_engines", type=list, default=["gpt-4o", "gpt-4o-mini", "llama31-8b", "llama33-70b", "Deepseek-R1", "o4-mini"], help="Engines used for testing.")
    parser.add_argument("--token_limit", "-t", type=int, default=128000, help="Token limit.")
    parser.add_argument("--tag", type=str, default="", help="Tag for the dataset.")
    parser.add_argument("-y", action="store_true", help="Automatic yes to prompts.")
    args = parser.parse_args()
    
    if args.cmd == "one":
        save_tos = []
        for config_file in args.config:
            assert os.path.exists(config_file), f"Configuration file not found: {config_file}"
            _, _, _, save_to_valid = build_data(os.path.abspath(config_file), num_workers=args.num_workers, debug=args.debug, token_limit=args.token_limit, bypass=args.y, test=args.test, test_engines=args.test_engines)
            save_tos.append(save_to_valid)
        print("To query \npython3 queryWithDeployment.py", " ".join(save_tos))
    elif args.cmd == "batch":
        build_batch(args)