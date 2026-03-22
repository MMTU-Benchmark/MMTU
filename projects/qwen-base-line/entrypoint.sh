#!/bin/bash
set -e

# Always deploy latest code from image (overwrite stale code on persistent volume)
echo "Deploying MMTU code to /workspace/MMTU..."
mkdir -p /workspace/MMTU
cp -r /opt/MMTU/. /workspace/MMTU/
echo "  Done."

LOG_FILE="/workspace/vllm.log"
MODEL="Qwen/Qwen2.5-7B-Instruct"
PORT=8000
MAX_MODEL_LEN="${VLLM_MAX_MODEL_LEN:-4096}"
HEALTH_URL="http://localhost:${PORT}/v1/models"
TIMEOUT=300

# Use persistent cache on /workspace (survives pod restarts with network volume)
export HF_HOME="/workspace/.cache/huggingface"

# Download model weights if not already cached
echo "Checking model weights for ${MODEL}..."
huggingface-cli download "$MODEL"
echo "  Model weights ready."

echo "Starting vLLM server for ${MODEL}..."
nohup vllm serve "$MODEL" \
    --host 0.0.0.0 \
    --port "$PORT" \
    --gpu-memory-utilization 0.9 \
    --max-model-len "$MAX_MODEL_LEN" \
    > "$LOG_FILE" 2>&1 &

VLLM_PID=$!
echo "  vLLM PID: ${VLLM_PID}, log: ${LOG_FILE}"

# Wait for vLLM to be ready
echo "Waiting for vLLM to be ready (timeout: ${TIMEOUT}s)..."
elapsed=0
while [ $elapsed -lt $TIMEOUT ]; do
    if curl -s "$HEALTH_URL" > /dev/null 2>&1; then
        echo "vLLM is ready! (took ${elapsed}s)"
        echo ""
        echo "Run experiments with:"
        echo "  cd /workspace/MMTU"
        echo "  python projects/qwen-base-line/run.py smoke"
        echo "  python projects/qwen-base-line/run.py baseline"
        echo ""
        echo "vLLM log: tail -f ${LOG_FILE}"
        exec sleep infinity
    fi
    sleep 5
    elapsed=$((elapsed + 5))
done

echo "ERROR: vLLM failed to start within ${TIMEOUT}s"
echo "Check log: cat ${LOG_FILE}"
exit 1
