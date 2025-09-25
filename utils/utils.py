import pandas as pd
import os
import numpy as np
import json

def makedir(dir_list, file=None):
    save_dir = os.path.join(*dir_list)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    if file is not None:
        save_dir = os.path.join(save_dir, file)
    return save_dir

def load_df(df_path, info=None):
    try:
        df = pd.read_csv(df_path)
    except:
        try:
            df = pd.read_csv(df_path, encoding="latin")
        except Exception as e:
            print(str(e))
            raise
    
    if info is not None:
        if "rename_columns" in info:
            df = df.rename(columns=info["rename_columns"])
        if "drop_columns" in info:
            drop_columns = [c for c in df.columns if c in info["drop_columns"]]
            df = df.drop(columns=drop_columns)
    return df

def load_data(data_dir, dataset):
    with open(os.path.join(data_dir, dataset, "info.json"), "r") as f:
        info = json.load(f)
        
    left = load_df(os.path.join(data_dir, dataset, "tableA.csv"), info=info)
    right = load_df(os.path.join(data_dir, dataset, "tableB.csv"), info=info)
    train = load_df(os.path.join(data_dir, dataset, "train.csv"))
    val = load_df(os.path.join(data_dir, dataset, "valid.csv"))
    test = load_df(os.path.join(data_dir, dataset, "test.csv"))
    return left, right, train, val, test, info
    
def sample_df(df, class_balance, max_size=None, random_state=1):
    np.random.seed(random_state)
    
    # downsample majority class
    if class_balance: 
        labels = sorted(set(df["label"].values))
        sub_df_list = []
        for l in labels:
            sub_df = df[df["label"] == l]
            sub_df_list.append(sub_df)
        min_num = min([len(sub_df) for sub_df in sub_df_list])
        balanced_df_list = []
        for sub_df in sub_df_list:
            balanced_df_list.append(sub_df.sample(n=min_num, axis=0))
        df = pd.concat(balanced_df_list, axis=0).reset_index(drop=True)
    
    # sample data
    if max_size is None:
        max_size = len(df)
        
    max_size = min(max_size, len(df))
    sample_df = df.sample(n=max_size, axis=0).reset_index(drop=True)
    return sample_df

def generate_metadata(test_data, info):
    test_ids = []
    for _, row in test_data.iterrows():
        key = f"benchmark_{info['benchmark']}___dataset_{info['dataset']}___sampleMethod_{info['sampleMethod']}___numSamples_{info['numSamples']}___trial_{info['trial']}___id_{row.lrid}___label_{row.label}"
        test_ids.append(key)
    return test_ids

def load_api_keys(path):
    api_keys = []
    with open(path, "r") as f:
        for l in f:
            api_keys.append(l.strip())
    return api_keys

def parse_metadata(metadata):
    key_value_list = metadata.split("___")
    result = {}
    for key_value in key_value_list:
        key = key_value.split("_")[0]
        value = key_value[len(key)+1:]
        result[key] = value
    if "note" not in result:
        result["note"] = ""
    return result

def get_model_name(model):
    if model == "D3":
        model_name = "text-davinci-003"
    elif model == "D2":
        model_name = "text-davinci-002"
    elif model == "T3.5":
        model_name = "gpt-3.5-turbo"
    elif model == "A":
        model_name = "text-ada-001"
    elif model == "B":
        model_name = "text-babbage-001"
    elif model == "C":
        model_name = "text-curie-001"
    elif model == "G4":
        model_name = "gpt-4"
    elif model == "G4-32":
        model_name = "gpt-4-32k"
    else:
        raise Exception(f"Wrong GPT model name: {model}")
    return model_name

def save_as_jsonl(df, jsonl_save_dir):
    return df.to_json(jsonl_save_dir, orient='records', lines=True)

def balance_sample_two_classes(df, sample_size, random_state=1):
    np.random.seed(random_state)
    
    labels = sorted(set(df["label"].values))
    assert len(labels) == 2

    sub_df_list = []
    for l in labels:
        sub_df = df[df["label"] == l]
        sub_df_list.append(sub_df)
        
    min_num = min([len(sub_df) for sub_df in sub_df_list])
    sample_sub_size = min(min_num, sample_size//2)
    balanced_df_list = []
    for sub_df in sub_df_list:
        balanced_df_list.append(sub_df.sample(n=sample_sub_size, axis=0))
    
    sample_df = pd.concat(balanced_df_list, axis=0).sort_values(by="label").reset_index(drop=True)
    return sample_df

def save_version(data_dir, version):
    with open(os.path.join(data_dir, "version"), "w") as f:
        f.write(version)
        
def load_version(data_dir):
    with open(os.path.join(data_dir, "version"), "r") as f:
        line = f.readlines()
    return line[0].strip()

class MMTUDataset:
    """A dataset wrapper that mimics HuggingFace datasets interface for MMTU data."""
    
    def __init__(self, df):
        self.df = df
    
    def to_json(self, path, lines=True, orient="records"):
        """Save dataset to JSON lines format."""
        self.df.to_json(path, lines=lines, orient=orient)
    
    def __len__(self):
        return len(self.df)
    
    def __getitem__(self, idx):
        return self.df.iloc[idx].to_dict()

def load_dataset(dataset_name, split="train", data_dir=None):
    """
    Load MMTU dataset from local JSONL files.
    
    This function loads pre-built MMTU dataset files created by build_data.py.
    If no pre-built dataset is found, it provides guidance on how to build one.
    
    Args:
        dataset_name (str): Name of the dataset (e.g., "MMTU-benchmark/MMTU")
        split (str): Dataset split to load (default: "train")
        data_dir (str): Directory containing the dataset files. If None, looks for 
                       environment variable MMTU_DATA_DIR or defaults to "./datasets_prompt"
    
    Returns:
        MMTUDataset: Dataset object with to_json method
        
    Example:
        >>> ds = load_dataset("MMTU-benchmark/MMTU", split="train")
        >>> ds.to_json("mmtu.jsonl", lines=True)
    """
    if data_dir is None:
        # Try to get data directory from environment variable
        data_dir = os.environ.get("MMTU_DATA_DIR", "./datasets_prompt")
    
    # Look for JSONL files in the data directory
    jsonl_files = []
    if os.path.exists(data_dir):
        for file in os.listdir(data_dir):
            if file.endswith(".jsonl") and "valid" in file:
                jsonl_files.append(os.path.join(data_dir, file))
    
    if not jsonl_files:
        # If no built dataset found, provide helpful guidance
        print(f"Warning: No pre-built MMTU dataset found in {data_dir}")
        print("To build the dataset:")
        print("1. Download the raw data from the OneDrive link in README.md")
        print("2. Set the MMTU_HOME environment variable: export MMTU_HOME=<path_to_data>")
        print("3. Run: python build_data.py one --config <config_file>")
        print("4. Or set MMTU_DATA_DIR to point to directory with pre-built JSONL files")
        print("")
        print("For now, using sample data for testing purposes...")
        
        # Create a sample dataset structure for testing
        sample_data = {
            "prompt": ["This is a sample prompt for testing the MMTU dataset loading functionality."],
            "metadata": ['{"task": "sample", "dataset": "test", "note": "This is sample data - please build the actual dataset"}']
        }
        df = pd.DataFrame(sample_data)
        return MMTUDataset(df)
    
    # Load the first available JSONL file (preferably the largest one)
    jsonl_files.sort(key=lambda x: os.path.getsize(x), reverse=True)
    jsonl_file = jsonl_files[0]
    print(f"Loading MMTU dataset from: {jsonl_file}")
    
    try:
        df = pd.read_json(jsonl_file, lines=True)
        print(f"Successfully loaded {len(df)} examples from MMTU dataset")
        return MMTUDataset(df)
    except Exception as e:
        print(f"Error loading dataset from {jsonl_file}: {e}")
        print("Using sample data as fallback...")
        # Return sample dataset as fallback
        sample_data = {
            "prompt": ["Sample prompt for testing"],
            "metadata": ['{"task": "sample", "dataset": "test", "error": "Failed to load actual dataset"}']
        }
        df = pd.DataFrame(sample_data)
        return MMTUDataset(df)