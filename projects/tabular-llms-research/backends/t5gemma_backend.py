"""T5Gemma inference backend — HuggingFace transformers (encoder-decoder).

Currently configured for T5Gemma 9B-9B UL2 IT (~18B total params, ~9B active
during decoding). Uses Flash Attention 2 + torch.compile for optimization.
"""

import torch
from transformers import AutoProcessor, AutoModelForSeq2SeqLM

from backends.base import InferenceBackend


class T5GemmaBackend(InferenceBackend):
    """Runs inference using T5Gemma (encoder-decoder) via HuggingFace transformers."""

    def __init__(self):
        self.model = None
        self.processor = None
        self.device = None
        self.max_new_tokens = 512
        self.temperature = 0.0

    def load(self, config: dict) -> None:
        model_cfg = config["model"]
        inference_cfg = config["inference"]

        model_path = model_cfg["model_path"]
        dtype = getattr(torch, model_cfg.get("dtype", "bfloat16"))
        self.max_new_tokens = inference_cfg.get("max_output_tokens", 512)
        self.temperature = inference_cfg.get("temperature", 0.0)

        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        print(f"Loading T5Gemma processor from {model_path}...")
        self.processor = AutoProcessor.from_pretrained(model_path)

        # Use Flash Attention 2 if available, fall back to SDPA
        attn_impl = "eager"
        try:
            import flash_attn  # noqa: F401
            attn_impl = "flash_attention_2"
        except ImportError:
            attn_impl = "sdpa"
            print("  flash-attn not installed, using SDPA attention.")

        print(f"Loading T5Gemma model from {model_path} (dtype={dtype}, attn={attn_impl})...")
        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            model_path,
            torch_dtype=dtype,
            device_map="auto",
            attn_implementation=attn_impl,
        )
        self.model.eval()

        # torch.compile for ~1.5-2x speedup on repeated forward passes
        print("  Applying torch.compile...")
        self.model = torch.compile(self.model)

        print(f"  T5Gemma ready on {self.device}. max_new_tokens={self.max_new_tokens}"
              f" ({attn_impl} + torch.compile)")

    def generate(self, prompt: str) -> str:
        return self.generate_batch([prompt])[0]

    def generate_batch(self, prompts: list[str]) -> list[str]:
        # T5Gemma supports batched generation via padding

        # Apply instruction tuning chat template
        formatted_prompts = []
        for p in prompts:
            # Check if processor has apply_chat_template (it usually does for instruction tuned models)
            if hasattr(self.processor, "apply_chat_template"):
                messages = [{"role": "user", "content": p}]
                formatted_p = self.processor.apply_chat_template(
                    messages,
                    tokenize=False,
                    add_generation_prompt=True
                )
                formatted_prompts.append(formatted_p)
            else:
                formatted_prompts.append(p)

        inputs = self.processor(
            text=formatted_prompts,
            return_tensors="pt",
            padding=True,
            truncation=True,
        )
        inputs = {k: v.to(self.model.device) for k, v in inputs.items()}

        gen_kwargs = {
            "max_new_tokens": self.max_new_tokens,
        }
        if self.temperature > 0:
            gen_kwargs["do_sample"] = True
            gen_kwargs["temperature"] = self.temperature
        else:
            gen_kwargs["do_sample"] = False

        with torch.no_grad():
            output_ids = self.model.generate(**inputs, **gen_kwargs)

        responses = self.processor.batch_decode(output_ids, skip_special_tokens=True)
        return [r.strip() for r in responses]

    def health_check(self) -> bool:
        return self.model is not None and self.processor is not None
