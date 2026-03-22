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

echo ""
echo "Run experiments with:"
echo "  cd /workspace/MMTU"
echo "  python projects/qwen-llada-alpha/run.py run configs/llada-8b-smoke.yaml"
echo "  python projects/qwen-llada-alpha/run.py run configs/llada-8b-baseline.yaml"
echo ""

exec sleep infinity
