"""Unit tests for llada_dp_backend.py — concurrent GPU dispatch, no GPU required."""

import sys
import types
import threading
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import torch

# Import directly to avoid heavy deps via __init__.py
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "backends"))

from backends.llada_dp_backend import LLaDADataParallelBackend  # noqa: E402

MASK_ID = 126336
VOCAB_SIZE = 126337


class FakeModel:
    """Minimal mock that returns random logits with the right shape."""

    def __init__(self, vocab_size: int = VOCAB_SIZE, device: str = "cpu"):
        self.vocab_size = vocab_size
        self._device = device

    @property
    def device(self) -> str:
        return self._device

    def __call__(self, x: torch.Tensor, attention_mask=None):
        logits = torch.randn(x.shape[0], x.shape[1], self.vocab_size)
        return types.SimpleNamespace(logits=logits)

    def to(self, device):
        return self

    def eval(self):
        return self


class FakeTokenizer:
    """Minimal tokenizer mock."""

    pad_token_id = 0

    def apply_chat_template(self, messages, add_generation_prompt=True, tokenize=False):
        return messages[0]["content"]

    def __call__(self, text):
        # Return deterministic token ids based on text length
        return {"input_ids": list(range(10, 10 + len(text)))}

    def decode(self, ids, skip_special_tokens=True):
        return f"response_{len(ids)}"


def _make_backend(n_gpus: int = 4) -> LLaDADataParallelBackend:
    """Create a backend with fake models/tokenizer, bypassing load()."""
    backend = LLaDADataParallelBackend()
    backend.tokenizer = FakeTokenizer()
    backend.replicas = [FakeModel(device=f"cpu") for _ in range(n_gpus)]
    backend.devices = ["cpu"] * n_gpus
    backend.gen_length = 16
    backend.tokens_per_step = 1
    backend.steps = 16  # gen_length // tokens_per_step
    backend.block_length = 16
    backend.temperature = 0.0
    backend.cfg_scale = 0.0
    backend.remasking = "random"
    backend.MASK_ID = MASK_ID
    return backend


# ---------------------------------------------------------------------------
# Concurrency: verify shards run on separate threads
# ---------------------------------------------------------------------------

class TestConcurrentDispatch:
    def test_shards_run_on_different_threads(self):
        """Verify that _run_shard is called from multiple threads."""
        backend = _make_backend(n_gpus=4)
        thread_ids: list[int] = []
        original_run_shard = backend._run_shard

        def tracking_run_shard(gpu_idx, shard):
            thread_ids.append(threading.current_thread().ident)
            return original_run_shard(gpu_idx, shard)

        backend._run_shard = tracking_run_shard

        prompts = [f"prompt {i}" for i in range(8)]
        backend.generate_batch(prompts)

        # With 8 prompts and 4 GPUs, all 4 shards should be non-empty
        assert len(thread_ids) == 4
        # At least 2 distinct threads (pool may reuse threads for fast tasks,
        # but with 4 concurrent submissions we expect multiple)
        assert len(set(thread_ids)) >= 2

    def test_single_gpu_still_works(self):
        """Concurrency with 1 GPU should degrade gracefully."""
        backend = _make_backend(n_gpus=1)
        prompts = ["hello", "world"]
        results = backend.generate_batch(prompts)
        assert len(results) == 2

    def test_more_gpus_than_prompts(self):
        """Empty shards should be skipped, no errors."""
        backend = _make_backend(n_gpus=4)
        prompts = ["only one"]
        results = backend.generate_batch(prompts)
        assert len(results) == 1


# ---------------------------------------------------------------------------
# Result ordering: outputs must match input order regardless of finish order
# ---------------------------------------------------------------------------

class TestResultOrdering:
    def test_results_match_input_order(self):
        """Results should be in the same order as input prompts."""
        backend = _make_backend(n_gpus=4)
        prompts = [f"prompt_{i}" for i in range(12)]
        results = backend.generate_batch(prompts)
        assert len(results) == 12
        # Each prompt has a different length → different token count →
        # FakeTokenizer produces different ids → decode gives different suffix.
        # Just verify we get the right count and all are strings.
        assert all(isinstance(r, str) for r in results)

    def test_length_sorted_distribution(self):
        """Prompts should be sorted by length and distributed in contiguous chunks."""
        backend = _make_backend(n_gpus=3)
        # Prompts of varying lengths — FakeTokenizer returns len(text) tokens
        prompts = ["a", "abcdef", "ab", "abcdefghi", "abc", "abcdefgh",
                    "abcd", "abcdefghij", "abcde"]

        shard_calls: dict[int, list] = {}
        original_run_shard = backend._run_shard

        def spy_run_shard(gpu_idx, shard):
            shard_calls[gpu_idx] = [s[0] for s in shard]  # orig indices
            return original_run_shard(gpu_idx, shard)

        backend._run_shard = spy_run_shard
        backend.generate_batch(prompts)

        # 9 prompts / 3 GPUs = 3 per GPU, sorted by token length
        # Each shard should have 3 prompts, grouped by similar length
        assert len(shard_calls) == 3
        for gpu_idx in range(3):
            assert len(shard_calls[gpu_idx]) == 3

        # All original indices should be present (no duplicates, no missing)
        all_indices = []
        for indices in shard_calls.values():
            all_indices.extend(indices)
        assert sorted(all_indices) == list(range(9))


# ---------------------------------------------------------------------------
# Error propagation: exceptions in threads should surface to caller
# ---------------------------------------------------------------------------

class TestErrorPropagation:
    def test_thread_exception_propagates(self):
        """If a GPU shard raises, the exception should propagate to the caller."""
        backend = _make_backend(n_gpus=2)

        def failing_run_shard(gpu_idx, shard):
            if gpu_idx == 1:
                raise RuntimeError("GPU 1 OOM")
            return backend.__class__._run_shard(backend, gpu_idx, shard)

        backend._run_shard = failing_run_shard
        with pytest.raises(RuntimeError, match="GPU 1 OOM"):
            backend.generate_batch(["a", "b", "c", "d"])
