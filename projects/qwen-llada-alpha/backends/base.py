"""Abstract base class for inference backends."""

from abc import ABC, abstractmethod


class InferenceBackend(ABC):
    """Common interface that every model backend must implement."""

    @abstractmethod
    def load(self, config: dict) -> None:
        """Load model and tokenizer from *config* (the full experiment dict)."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Given a user prompt string, return the model's text response."""

    def generate_batch(self, prompts: list[str]) -> list[str]:
        """Generate responses for a batch of prompts. Override for GPU-batched inference."""
        return [self.generate(p) for p in prompts]

    @abstractmethod
    def health_check(self) -> bool:
        """Return True if the backend is ready to serve requests."""
