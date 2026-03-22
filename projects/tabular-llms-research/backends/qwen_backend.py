"""Qwen2.5 inference backend — vLLM via OpenAI-compatible API."""

import concurrent.futures

from openai import OpenAI

from backends.base import InferenceBackend


class QwenBackend(InferenceBackend):
    """Runs inference against a vLLM server using the OpenAI-compatible API."""

    def __init__(self):
        self.client = None
        self.model_name = None
        self.max_tokens = 512
        self.temperature = 0.0

    def load(self, config: dict) -> None:
        model_cfg = config["model"]
        inference_cfg = config["inference"]
        vllm_cfg = inference_cfg.get("vllm", {})

        self.model_name = model_cfg["model_path"]
        self.max_tokens = inference_cfg.get("max_output_tokens", 512)
        self.temperature = inference_cfg.get("temperature", 0.0)

        base_url = vllm_cfg.get("base_url", "http://localhost:8000/v1")
        api_key = vllm_cfg.get("api_key", "EMPTY")

        print(f"Connecting to vLLM server: {base_url}")
        print(f"  Model: {self.model_name}")
        self.client = OpenAI(base_url=base_url, api_key=api_key)

        print(f"  Qwen ready (vLLM). max_tokens={self.max_tokens}, "
              f"temperature={self.temperature}")

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        return response.choices[0].message.content.strip()

    def generate_batch(self, prompts: list[str]) -> list[str]:
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(prompts)) as pool:
            futures = [pool.submit(self.generate, p) for p in prompts]
            return [f.result() for f in futures]

    def health_check(self) -> bool:
        if self.client is None:
            return False
        try:
            models = self.client.models.list()
            return any(m.id == self.model_name for m in models.data)
        except Exception:
            return False
