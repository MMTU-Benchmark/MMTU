#!/bin/bash
set -e

# Deploy latest code from image to persistent volume
echo "Deploying MMTU code to /workspace/MMTU..."
mkdir -p /workspace/MMTU
cp -r /opt/MMTU/. /workspace/MMTU/
echo "  Done."

# Use persistent cache on /workspace (survives pod restarts with network volume)
export HF_HOME="/workspace/.cache/huggingface"

# Download model weights (default to LLaDA, overridable via env var)
MODEL="${MODEL_PATH:-GSAI-ML/LLaDA-8B-Instruct}"
echo "Checking model weights for ${MODEL}..."
huggingface-cli download "$MODEL"
echo "  Model weights ready."

# Optionally download Qwen weights
QWEN_MODEL="${QWEN_MODEL_PATH:-Qwen/Qwen2.5-7B-Instruct}"
if [ "${DOWNLOAD_QWEN:-false}" = "true" ]; then
    echo "Checking model weights for ${QWEN_MODEL}..."
    huggingface-cli download "$QWEN_MODEL"
    echo "  Qwen model weights ready."
fi

echo ""
echo "============================================================"
echo "  dllm-alpha ready"
echo "============================================================"
echo ""
echo "  cd /workspace/MMTU"
echo ""
echo "  # Experiment 1: LLaDA (data-parallel, 4 GPUs)"
echo "  python projects/dllm-alpha/run.py run configs/llada-8b-smoke.yaml"
echo ""
echo "  # Experiment 2: Qwen (start vLLM first, then run)"
echo "  python -m vllm.entrypoints.openai.api_server \\"
echo "      --model ${QWEN_MODEL} --tensor-parallel-size 4 &"
echo "  sleep 60 && python projects/dllm-alpha/run.py run configs/qwen-7b-smoke.yaml"
echo ""

exec sleep infinity
