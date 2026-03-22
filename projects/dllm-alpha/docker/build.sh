#!/bin/bash
set -e

# Build and optionally push the dllm-alpha Docker image.
#
# Usage:
#   bash projects/dllm-alpha/docker/build.sh                              # build only
#   bash projects/dllm-alpha/docker/build.sh --registry docker.io/user    # build + tag
#   bash projects/dllm-alpha/docker/build.sh --registry docker.io/user --push  # build + push
#
# Requirements: x86_64 Linux with Docker. No GPU needed (GPU only at runtime).

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
MMTU_ROOT="$(cd "$PROJECT_DIR/../.." && pwd)"

IMAGE="dllm-alpha"
TAG="latest"
REGISTRY=""
PUSH=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --registry)
            REGISTRY="$2"
            shift 2 ;;
        --push)
            PUSH=true
            shift ;;
        --tag)
            TAG="$2"
            shift 2 ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: $0 [--registry REG] [--push] [--tag TAG]"
            exit 1 ;;
    esac
done

cd "$MMTU_ROOT"

echo "=== Building ${IMAGE}:${TAG} ==="
docker build -t "${IMAGE}:${TAG}" \
    -f projects/dllm-alpha/docker/Dockerfile .

if [ -n "$REGISTRY" ]; then
    REMOTE="${REGISTRY}/${IMAGE}:${TAG}"
    docker tag "${IMAGE}:${TAG}" "$REMOTE"
    echo "Tagged: ${REMOTE}"
    if [ "$PUSH" = true ]; then
        echo "Pushing ${REMOTE}..."
        docker push "$REMOTE"
    fi
fi

echo ""
echo "Done! Local image: ${IMAGE}:${TAG}"
