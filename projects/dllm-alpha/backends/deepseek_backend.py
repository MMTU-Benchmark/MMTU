"""DeepSeek V3 inference backend — OpenRouter API (OpenAI-compatible)."""

import concurrent.futures
import os
from typing import List

from openai import OpenAI

from backends.base import InferenceBackend


class DeepSeekBackend(InferenceBackend):
    """Runs inference against OpenRouter using the OpenAI-compatible client."""

    def __init__(self):
        self.client = None
        self.model_name = None
        self.max_tokens = 512
        self.temperature = 0.0

    def load(self, config: dict) -> None:
        model_cfg = config["model"]
        inference_cfg = config["inference"]
        api_cfg = inference_cfg.get("api", {})

        self.model_name = model_cfg.get("model_path", "deepseek-chat")
        self.max_tokens = inference_cfg.get("max_output_tokens", 512)
        self.temperature = inference_cfg.get("temperature", 0.0)

        base_url = api_cfg.get("base_url", "https://openrouter.ai/api/v1")
        api_key = api_cfg.get("api_key") or os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError(
                "OpenRouter API key required. Set inference.api.api_key in the "
                "config or the OPENROUTER_API_KEY environment variable."
            )

        print(f"Connecting to OpenRouter API: {base_url}")
        print(f"  Model: {self.model_name}")
        self.client = OpenAI(base_url=base_url, api_key=api_key)

        print(f"  OpenRouter ready. max_tokens={self.max_tokens}, "
              f"temperature={self.temperature}")

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        return response.choices[0].message.content.strip()

    def generate_batch(self, prompts: List[str]) -> List[str]:
        # DeepSeek API handles rate limiting server-side; send concurrent
        # requests and let the client handle backpressure.
        max_workers = min(len(prompts), 8)
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as pool:
            futures = [pool.submit(self.generate, p) for p in prompts]
            return [f.result() for f in futures]

    def health_check(self) -> bool:
        if self.client is None:
            return False
        try:
            # Quick test call with minimal tokens
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": "hi"}],
                max_tokens=1,
            )
            return response.choices[0].message.content is not None
        except Exception:
            return False
