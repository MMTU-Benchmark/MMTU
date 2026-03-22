"""Inference backend registry."""

from backends.base import InferenceBackend
from backends.llada_backend import LLaDABackend
from backends.qwen_backend import QwenBackend

BACKENDS = {
    "llada": LLaDABackend,
    "qwen": QwenBackend,
}


def get_backend(name: str) -> type[InferenceBackend]:
    """Look up a backend class by name."""
    if name not in BACKENDS:
        available = ", ".join(sorted(BACKENDS))
        raise ValueError(f"Unknown backend '{name}'. Available: {available}")
    return BACKENDS[name]
