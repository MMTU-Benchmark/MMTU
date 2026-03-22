#!/bin/bash
set -e
#
# One-shot script to build and push the mmtu-qwen-baseline Docker image
# from a fresh EC2 instance (Amazon Linux 2023 or Ubuntu 22.04).
#
# Usage:
#   1. Launch EC2: t3.medium, 30GB gp3, default VPC
#   2. SSH in:     ssh -i key.pem ec2-user@<ip>   (or ubuntu@<ip>)
#   3. Copy this script to the instance and edit the config below
#   4. Run:        bash ec2-build-guide.sh
#   5. Terminate the instance when done
#

# ──────────────────────────────────────────────
# Config — fill these in before running
# ──────────────────────────────────────────────
DOCKERHUB_USER=""          # e.g. "akumch"
GITHUB_REPO_URL=""         # e.g. "https://github.com/junos-ai-org/MMTU.git"
BRANCH="main"              # branch to build from

# ──────────────────────────────────────────────
# Validation
# ──────────────────────────────────────────────
if [ -z "$DOCKERHUB_USER" ] || [ -z "$GITHUB_REPO_URL" ]; then
    echo "ERROR: Edit this script and fill in DOCKERHUB_USER and GITHUB_REPO_URL."
    exit 1
fi

# ──────────────────────────────────────────────
# Install Docker + git
# ──────────────────────────────────────────────
echo "=== Installing Docker and git ==="
if command -v apt-get &>/dev/null; then
    # Ubuntu / Debian
    sudo apt-get update
    sudo apt-get install -y docker.io git
    sudo systemctl start docker
elif command -v yum &>/dev/null; then
    # Amazon Linux 2023 / AL2
    sudo yum install -y docker git
    sudo systemctl start docker
else
    echo "ERROR: Unsupported OS. Use Amazon Linux 2023 or Ubuntu 22.04."
    exit 1
fi

sudo usermod -aG docker "$USER"
echo "  Docker installed."

# ──────────────────────────────────────────────
# Clone repo
# ──────────────────────────────────────────────
echo ""
echo "=== Cloning ${GITHUB_REPO_URL} (branch: ${BRANCH}) ==="
WORK_DIR="/tmp/MMTU"
rm -rf "$WORK_DIR"
git clone --branch "$BRANCH" "$GITHUB_REPO_URL" "$WORK_DIR"

# ──────────────────────────────────────────────
# Build and push (via sg to pick up docker group)
# ──────────────────────────────────────────────
echo ""
echo "=== Logging into Docker Hub as ${DOCKERHUB_USER} ==="
echo "  (you will be prompted for your password or access token)"

sg docker -c "
    set -e
    docker login -u '${DOCKERHUB_USER}'
    echo ''
    echo '=== Building image ==='
    cd '${WORK_DIR}'
    bash projects/qwen-base-line/docker/build.sh \
        --registry 'docker.io/${DOCKERHUB_USER}' --push
"

echo ""
echo "============================================"
echo "  Done!"
echo "  Image: docker.io/${DOCKERHUB_USER}/mmtu-qwen-baseline:latest"
echo ""
echo "  Next: create a RunPod GPU pod with this image."
echo "  Don't forget to TERMINATE this EC2 instance!"
echo "============================================"
