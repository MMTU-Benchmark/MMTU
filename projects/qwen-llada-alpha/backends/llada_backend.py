"""LLaDA inference backend — diffusion-based text generation."""

from typing import List

import torch
from transformers import AutoModel, AutoTokenizer

from backends.base import InferenceBackend
from backends.llada_generate import generate


class LLaDABackend(InferenceBackend):
    """Runs inference using LLaDA's masked-diffusion generate() loop."""

    MASK_ID = 126336  # LLaDA's [MASK] token id

    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.device = "cuda"
        # Generation defaults (overridden by config)
        self.gen_length = 512
        self.steps = 128
        self.block_length = 128
        self.temperature = 0.0
        self.cfg_scale = 0.0
        self.remasking = "low_confidence"

    def load(self, config: dict) -> None:
        model_cfg = config["model"]
        inference_cfg = config["inference"]

        model_path = model_cfg["model_path"]
        dtype = getattr(torch, model_cfg.get("dtype", "bfloat16"))

        print(f"Loading LLaDA model: {model_path} (dtype={dtype})...")
        self.model = AutoModel.from_pretrained(
            model_path,
            trust_remote_code=True,
            torch_dtype=dtype,
        ).to(self.device).eval()

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            trust_remote_code=True,
        )

        # Apply inference config
        self.gen_length = inference_cfg.get("max_output_tokens", 512)
        self.steps = inference_cfg.get("steps", 128)
        self.block_length = inference_cfg.get("block_length", 128)
        self.temperature = inference_cfg.get("temperature", 0.0)
        self.cfg_scale = inference_cfg.get("cfg_scale", 0.0)
        self.remasking = inference_cfg.get("remasking", "low_confidence")

        print(f"  LLaDA ready. gen_length={self.gen_length}, steps={self.steps}, "
              f"block_length={self.block_length}, remasking={self.remasking}")

    def generate(self, prompt: str) -> str:
        messages = [{"role": "user", "content": prompt}]
        text = self.tokenizer.apply_chat_template(
            messages, add_generation_prompt=True, tokenize=False
        )
        input_ids = self.tokenizer(text)["input_ids"]
        input_ids = torch.tensor(input_ids, device=self.device).unsqueeze(0)

        output = generate(
            self.model,
            input_ids,
            steps=self.steps,
            gen_length=self.gen_length,
            block_length=self.block_length,
            temperature=self.temperature,
            cfg_scale=self.cfg_scale,
            remasking=self.remasking,
            mask_id=self.MASK_ID,
        )

        # Decode only the generated tokens (after prompt)
        generated_ids = output[0, input_ids.shape[1]:]
        response = self.tokenizer.decode(generated_ids, skip_special_tokens=True)
        return response.strip()

    def generate_batch(self, prompts: List[str]) -> List[str]:
        # Tokenize all prompts
        all_input_ids = []
        for prompt in prompts:
            messages = [{"role": "user", "content": prompt}]
            text = self.tokenizer.apply_chat_template(
                messages, add_generation_prompt=True, tokenize=False
            )
            ids = self.tokenizer(text)["input_ids"]
            all_input_ids.append(ids)

        # Left-pad to the longest prompt in the batch
        max_len = max(len(ids) for ids in all_input_ids)
        pad_id = self.tokenizer.pad_token_id or 0
        padded = []
        prompt_lengths = []
        for ids in all_input_ids:
            pad_len = max_len - len(ids)
            padded.append([pad_id] * pad_len + ids)
            prompt_lengths.append(len(ids))

        batch_tensor = torch.tensor(padded, device=self.device)

        output = generate(
            self.model,
            batch_tensor,
            steps=self.steps,
            gen_length=self.gen_length,
            block_length=self.block_length,
            temperature=self.temperature,
            cfg_scale=self.cfg_scale,
            remasking=self.remasking,
            mask_id=self.MASK_ID,
        )

        # Decode each result — generated tokens start after the (padded) prompt
        responses = []
        for i in range(len(prompts)):
            generated_ids = output[i, max_len:]
            response = self.tokenizer.decode(generated_ids, skip_special_tokens=True)
            responses.append(response.strip())
        return responses

    def health_check(self) -> bool:
        return self.model is not None
