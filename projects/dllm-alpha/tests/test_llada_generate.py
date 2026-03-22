"""Unit tests for llada_generate.py — tensor plumbing, no GPU required."""

import sys
import types
from pathlib import Path

import numpy as np
import pytest
import torch

# Import directly from file to avoid backends/__init__.py (which pulls in
# transformers and other heavy deps not available in test environments).
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "backends"))
from llada_generate import (  # noqa: E402
    add_gumbel_noise,
    generate,
    get_num_transfer_tokens,
)

MASK_ID = 126336
VOCAB_SIZE = 126337  # mask_id + 1


class FakeModel:
    """Minimal mock that returns random logits with the right shape."""

    def __init__(self, vocab_size: int = VOCAB_SIZE, device: str = "cpu"):
        self.vocab_size = vocab_size
        self._device = device
        self.last_attention_mask = None  # Track last attention_mask passed

    @property
    def device(self) -> str:
        return self._device

    def __call__(self, x: torch.Tensor, attention_mask=None):
        self.last_attention_mask = attention_mask
        logits = torch.randn(x.shape[0], x.shape[1], self.vocab_size)
        return types.SimpleNamespace(logits=logits)


# ---------------------------------------------------------------------------
# get_num_transfer_tokens
# ---------------------------------------------------------------------------

class TestGetNumTransferTokens:
    def test_sums_to_mask_count(self):
        mask_index = torch.tensor([[True, True, False, True, True]])  # 4 masks
        result = get_num_transfer_tokens(mask_index, steps=2)
        assert result.sum().item() == 4

    def test_sums_to_mask_count_batch(self):
        mask_index = torch.tensor([
            [True, True, False, True],   # 3 masks
            [True, True, True, True],    # 4 masks
        ])
        result = get_num_transfer_tokens(mask_index, steps=2)
        assert result[0].sum().item() == 3
        assert result[1].sum().item() == 4

    def test_even_distribution(self):
        mask_index = torch.tensor([[True] * 10])
        result = get_num_transfer_tokens(mask_index, steps=5)
        assert result.shape == (1, 5)
        assert (result == 2).all()

    def test_remainder_spread_across_first_steps(self):
        mask_index = torch.tensor([[True] * 7])
        result = get_num_transfer_tokens(mask_index, steps=3)
        # 7 // 3 = 2 base, remainder 1 → first step gets +1
        assert result[0].tolist() == [3, 2, 2]


# ---------------------------------------------------------------------------
# add_gumbel_noise
# ---------------------------------------------------------------------------

class TestAddGumbelNoise:
    def test_zero_temperature_returns_input(self):
        logits = torch.randn(2, 5)
        out = add_gumbel_noise(logits, temperature=0)
        assert torch.equal(out, logits)

    def test_nonzero_temperature_preserves_shape(self):
        logits = torch.randn(2, 10, 50)
        out = add_gumbel_noise(logits, temperature=1.0)
        assert out.shape == logits.shape


# ---------------------------------------------------------------------------
# generate — output shapes
# ---------------------------------------------------------------------------

class TestGenerateShapes:
    @pytest.mark.parametrize("batch_size", [1, 4])
    def test_output_shape(self, batch_size):
        prompt_len, gen_length = 8, 16
        prompt = torch.randint(0, 1000, (batch_size, prompt_len))
        model = FakeModel()
        out = generate(
            model, prompt,
            steps=16, gen_length=gen_length, block_length=gen_length,
            temperature=0., cfg_scale=0., remasking="random", mask_id=MASK_ID,
        )
        assert out.shape == (batch_size, prompt_len + gen_length)

    @pytest.mark.parametrize("batch_size", [1, 4])
    def test_prompt_preserved(self, batch_size):
        prompt_len, gen_length = 8, 16
        prompt = torch.randint(0, 1000, (batch_size, prompt_len))
        model = FakeModel()
        out = generate(
            model, prompt,
            steps=16, gen_length=gen_length, block_length=gen_length,
            temperature=0., cfg_scale=0., remasking="random", mask_id=MASK_ID,
        )
        assert torch.equal(out[:, :prompt_len], prompt)

    def test_no_mask_tokens_in_output(self):
        prompt = torch.randint(0, 1000, (2, 8))
        model = FakeModel()
        out = generate(
            model, prompt,
            steps=16, gen_length=16, block_length=16,
            temperature=0., cfg_scale=0., remasking="random", mask_id=MASK_ID,
        )
        assert (out != MASK_ID).all()


# ---------------------------------------------------------------------------
# generate — cfg_scale (classifier-free guidance)
# ---------------------------------------------------------------------------

class TestGenerateCFG:
    @pytest.mark.parametrize("batch_size", [1, 4])
    def test_cfg_output_shape(self, batch_size):
        prompt_len, gen_length = 8, 16
        prompt = torch.randint(0, 1000, (batch_size, prompt_len))
        model = FakeModel()
        out = generate(
            model, prompt,
            steps=16, gen_length=gen_length, block_length=gen_length,
            temperature=0., cfg_scale=1.0, remasking="random", mask_id=MASK_ID,
        )
        assert out.shape == (batch_size, prompt_len + gen_length)


# ---------------------------------------------------------------------------
# generate — remasking strategies
# ---------------------------------------------------------------------------

class TestRemaskingStrategies:
    @pytest.mark.parametrize("strategy", [
        "low_confidence", "random", "gaussian", "beta", "chi_squared",
    ])
    def test_all_strategies_run(self, strategy):
        prompt = torch.randint(0, 1000, (2, 8))
        model = FakeModel()
        out = generate(
            model, prompt,
            steps=8, gen_length=8, block_length=8,
            temperature=0., cfg_scale=0., remasking=strategy, mask_id=MASK_ID,
        )
        assert out.shape == (2, 16)

    def test_unknown_strategy_raises(self):
        prompt = torch.randint(0, 1000, (1, 8))
        model = FakeModel()
        with pytest.raises(NotImplementedError):
            generate(
                model, prompt,
                steps=8, gen_length=8, block_length=8,
                temperature=0., cfg_scale=0., remasking="unknown", mask_id=MASK_ID,
            )


# ---------------------------------------------------------------------------
# generate — semi-autoregressive (multiple blocks)
# ---------------------------------------------------------------------------

class TestSemiAutoregressive:
    def test_multi_block_output_shape(self):
        prompt = torch.randint(0, 1000, (2, 8))
        model = FakeModel()
        out = generate(
            model, prompt,
            steps=8, gen_length=16, block_length=8,  # 2 blocks
            temperature=0., cfg_scale=0., remasking="random", mask_id=MASK_ID,
        )
        assert out.shape == (2, 24)


# ---------------------------------------------------------------------------
# generate — attention mask
# ---------------------------------------------------------------------------

class TestAttentionMask:
    def test_attention_mask_extended_to_gen_length(self):
        """attention_mask should be extended with 1s for generation positions."""
        prompt_len, gen_length = 8, 16
        prompt = torch.randint(0, 1000, (2, prompt_len))
        # Simulate left-padding: first 3 positions are padding (0)
        attention_mask = torch.ones(2, prompt_len, dtype=torch.long)
        attention_mask[:, :3] = 0

        model = FakeModel()
        out = generate(
            model, prompt,
            steps=16, gen_length=gen_length, block_length=gen_length,
            temperature=0., cfg_scale=0., remasking="random", mask_id=MASK_ID,
            attention_mask=attention_mask,
        )
        # Model should have received mask of length prompt_len + gen_length
        last_mask = model.last_attention_mask
        assert last_mask.shape == (2, prompt_len + gen_length)
        # Padding positions should still be 0
        assert (last_mask[:, :3] == 0).all()
        # Generation positions should all be 1
        assert (last_mask[:, prompt_len:] == 1).all()

    def test_attention_mask_passed_to_model(self):
        """When attention_mask is provided, model receives it."""
        prompt = torch.randint(0, 1000, (1, 4))
        attention_mask = torch.ones(1, 4, dtype=torch.long)
        model = FakeModel()
        generate(
            model, prompt,
            steps=4, gen_length=4, block_length=4,
            temperature=0., cfg_scale=0., remasking="random", mask_id=MASK_ID,
            attention_mask=attention_mask,
        )
        assert model.last_attention_mask is not None

    def test_no_attention_mask_means_none(self):
        """When no attention_mask given, model receives None (backward compat)."""
        prompt = torch.randint(0, 1000, (1, 4))
        model = FakeModel()
        generate(
            model, prompt,
            steps=4, gen_length=4, block_length=4,
            temperature=0., cfg_scale=0., remasking="random", mask_id=MASK_ID,
        )
        assert model.last_attention_mask is None

    def test_cfg_doubles_attention_mask(self):
        """With CFG, attention_mask should be doubled along batch dim."""
        prompt = torch.randint(0, 1000, (2, 4))
        attention_mask = torch.ones(2, 4, dtype=torch.long)
        attention_mask[:, 0] = 0  # 1 pad position

        model = FakeModel()
        generate(
            model, prompt,
            steps=4, gen_length=4, block_length=4,
            temperature=0., cfg_scale=1.0, remasking="random", mask_id=MASK_ID,
            attention_mask=attention_mask,
        )
        # CFG concatenates [x, un_x] → mask should be [mask, mask] → batch=4
        last_mask = model.last_attention_mask
        assert last_mask.shape[0] == 4  # 2 * batch_size
        assert last_mask.shape[1] == 4 + 4  # prompt_len + gen_length
