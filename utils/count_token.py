import tiktoken
from multiprocessing import cpu_count

def count_tokens_mp(prompt_lists, model="gpt-4o", num_processes=cpu_count()):
    num_processes = min(num_processes, cpu_count())
    encoder = tiktoken.encoding_for_model(model)
    tokens = encoder.encode_batch(prompt_lists, num_threads=num_processes)
    num_tokens = [len(token) for token in tokens]
    return num_tokens

if __name__ == "__main__":
    import argparse
    import os
    import pandas as pd
    
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt_files", type=str, nargs="+")
    parser.add_argument("--model", type=str, default="gpt-4o")
    args = parser.parse_args()
    
    nums = []
    for prompt_file in args.prompt_files:
        if not os.path.exists(prompt_file):
            raise FileNotFoundError(f"File not found: {prompt_file}")
    
        df = pd.read_json(prompt_file, lines=True)
        assert "prompt" in df.columns, "prompt column not found"
        prompt_lists = df["prompt"].tolist()
        num_tokens = count_tokens_mp(prompt_lists, model=args.model)
        nums.append(sum(num_tokens))
        print("-" * 50)
        print(f"Prompt file: {prompt_file}")
        print(f"Total tokens in Million: {sum(num_tokens) / 1e6}M")
        print(f"Ave tokens: {sum(num_tokens) / len(num_tokens)}")
    
    print("-" * 50)
    print(f"Total tokens in Million: {sum(nums) / 1e6}M")
