FROM vllm/vllm-openai:latest

# System tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    screen vim grep htop curl net-tools procps \
    && rm -rf /var/lib/apt/lists/*

# MMTU Python dependencies
RUN pip install --no-cache-dir \
    pandas tabulate tiktoken tqdm xlsxwriter tenacity datasets openai azure-ai-inference \
    && ln -sf "$(which python3)" /usr/local/bin/python

# MMTU code — install outside /workspace (RunPod mounts a volume there)
COPY . /opt/MMTU

COPY projects/qwen-base-line/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT []
CMD ["/entrypoint.sh"]
