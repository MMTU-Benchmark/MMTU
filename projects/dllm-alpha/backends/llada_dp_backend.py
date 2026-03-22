"""LLaDA data-parallel backend — runs replicas across multiple GPUs.

Uses ThreadPoolExecutor to run GPU shards concurrently.  This works because
CUDA kernels release the Python GIL: each thread spends >99% of wall-time
inside GPU kernels (model forward passes, softmax, topk, …) while holding
the GIL only for the microseconds of Python dispatch between ops.  Four
threads driving four GPUs therefore achieve near-linear speedup without
contention.
"""

import time

import torch
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List

from backends.llada_backend import LLaDABackend


class LLaDADataParallelBackend(LLaDABackend):
    """Loads one LLaDA model replica per GPU for data-parallel inference.

    Each batch is split across GPUs, each replica processes its shard,
    and results are gathered back.
    """

    def __init__(self):
        super().__init__()
        self.replicas: list[torch.nn.Module] = []
        self.devices: list[str] = []

    def load(self, config: dict) -> None:
        model_cfg = config["model"]
        inference_cfg = config["inference"]

        model_path = model_cfg["model_path"]
        dtype = getattr(torch, model_cfg.get("dtype", "bfloat16"))

        n_gpus = torch.cuda.device_count()
        if n_gpus == 0:
            raise RuntimeError("No GPUs available for data-parallel backend")

        self.devices = [f"cuda:{i}" for i in range(n_gpus)]

        # Load tokenizer once (CPU-only, shared)
        from transformers import AutoModel, AutoTokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path, trust_remote_code=True,
        )

        # Load one replica per GPU
        print(f"Loading {n_gpus} LLaDA replicas: {model_path} (dtype={dtype})...")
        for i, device in enumerate(self.devices):
            print(f"  Loading replica {i} on {device}...")
            replica = AutoModel.from_pretrained(
                model_path,
                trust_remote_code=True,
                torch_dtype=dtype,
            ).to(device).eval()
            self.replicas.append(replica)

        # Keep self.model pointing to first replica for health_check / single generate
        self.model = self.replicas[0]
        self.device = self.devices[0]

        # Apply inference config
        self.gen_length = inference_cfg.get("max_output_tokens", 512)
        self.block_length = inference_cfg.get("block_length", 128)
        self.tokens_per_step = inference_cfg.get("tokens_per_step", 2)
        self.temperature = inference_cfg.get("temperature", 0.0)
        self.cfg_scale = inference_cfg.get("cfg_scale", 0.0)
        self.remasking = inference_cfg.get("remasking", "low_confidence")

        # Compute steps dynamically: total_steps = gen_length / tokens_per_step
        assert self.block_length % self.tokens_per_step == 0, (
            f"block_length ({self.block_length}) must be divisible by "
            f"tokens_per_step ({self.tokens_per_step})"
        )
        self.steps = self.gen_length // self.tokens_per_step

        print(f"  LLaDA DP ready ({n_gpus} GPUs). gen_length={self.gen_length}, "
              f"steps={self.steps} (tokens_per_step={self.tokens_per_step}), "
              f"block_length={self.block_length}, remasking={self.remasking}")

    def _run_shard(
        self,
        gpu_idx: int,
        shard: list[tuple[int, list[int]]],
    ) -> list[tuple[int, str]]:
        """Run a single GPU shard and return (orig_idx, response) pairs.

        Designed to be called from a worker thread.  All heavy computation
        happens inside CUDA kernels which release the GIL, so multiple
        threads can drive multiple GPUs with near-zero contention.
        """
        from backends.llada_generate import generate

        device = self.devices[gpu_idx]
        model = self.replicas[gpu_idx]

        indices = [s[0] for s in shard]
        shard_ids = [s[1] for s in shard]

        print(f"    [{device}] starting {len(shard)} samples", flush=True)
        t0 = time.time()

        # Left-pad to longest in this shard
        max_len = max(len(ids) for ids in shard_ids)
        pad_id = self.tokenizer.pad_token_id or 0
        padded = []
        for ids in shard_ids:
            pad_len = max_len - len(ids)
            padded.append([pad_id] * pad_len + ids)

        batch_tensor = torch.tensor(padded, device=device)

        # Build attention mask: 0 for left-padding positions, 1 elsewhere
        attention_mask = (batch_tensor != pad_id).long()

        output = generate(
            model,
            batch_tensor,
            steps=self.steps,
            gen_length=self.gen_length,
            block_length=self.block_length,
            temperature=self.temperature,
            cfg_scale=self.cfg_scale,
            remasking=self.remasking,
            mask_id=self.MASK_ID,
            attention_mask=attention_mask,
        )

        elapsed = time.time() - t0
        print(f"    [{device}] done {len(shard)} samples in {elapsed:.1f}s "
              f"({elapsed / len(shard):.1f}s/sample)", flush=True)

        results: list[tuple[int, str]] = []
        for i, orig_idx in enumerate(indices):
            generated_ids = output[i, max_len:]
            response = self.tokenizer.decode(
                generated_ids, skip_special_tokens=True
            )
            results.append((orig_idx, response.strip()))
        return results

    def generate_batch(self, prompts: List[str]) -> List[str]:
        n_gpus = len(self.replicas)

        # Tokenize all prompts (CPU, fast)
        all_input_ids = []
        for prompt in prompts:
            messages = [{"role": "user", "content": prompt}]
            text = self.tokenizer.apply_chat_template(
                messages, add_generation_prompt=True, tokenize=False
            )
            ids = self.tokenizer(text)["input_ids"]
            all_input_ids.append(ids)

        # Sort prompts by token length so each GPU shard has similar-length
        # sequences, minimizing padding waste within each shard.
        indexed_ids = sorted(enumerate(all_input_ids), key=lambda x: len(x[1]))
        gpu_shards: list[list[tuple[int, list[int]]]] = [[] for _ in range(n_gpus)]
        chunk_size = max(1, (len(indexed_ids) + n_gpus - 1) // n_gpus)
        for i, (orig_idx, ids) in enumerate(indexed_ids):
            gpu_idx = min(i // chunk_size, n_gpus - 1)
            gpu_shards[gpu_idx].append((orig_idx, ids))

        # Run all GPU shards concurrently — each thread drives one GPU.
        # CUDA kernels release the GIL so threads achieve true parallelism.
        results: list[tuple[int, str]] = []
        with ThreadPoolExecutor(max_workers=n_gpus) as pool:
            futures = {
                pool.submit(self._run_shard, gpu_idx, shard): gpu_idx
                for gpu_idx, shard in enumerate(gpu_shards)
                if shard
            }
            for future in as_completed(futures):
                results.extend(future.result())

        # Reassemble in original order
        results.sort(key=lambda x: x[0])
        return [r[1] for r in results]
