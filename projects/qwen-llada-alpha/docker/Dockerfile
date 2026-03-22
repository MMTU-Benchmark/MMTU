FROM pytorch/pytorch:2.5.1-cuda12.4-cudnn9-devel

# System tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    screen vim grep htop curl net-tools procps git \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies — shared across all backends
RUN pip install --no-cache-dir \
    pandas tabulate tiktoken tqdm xlsxwriter tenacity datasets openai azure-ai-inference \
    pyyaml \
    && ln -sf "$(which python3)" /usr/local/bin/python

# LLaDA backend dependencies
RUN pip install --no-cache-dir \
    transformers==4.49.0 accelerate==0.34.2

# MMTU code — install outside /workspace (RunPod mounts a volume there)
COPY . /opt/MMTU

COPY projects/qwen-llada-alpha/docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT []
CMD ["/entrypoint.sh"]
