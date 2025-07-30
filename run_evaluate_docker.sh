#!/bin/bash

# Script to run MMTU evaluate.py in Docker
# Usage: ./run_evaluate.sh <result_file> [additional_args...]

set -e

# Check if at least one argument is provided
if [ $# -lt 1 ]; then
    echo "Usage: $0 <result_file> [additional_args...]"
    echo "Example: $0 results/my_results.jsonl --debug --n_jobs 4"
    echo "Available options:"
    echo "  --n_jobs N     Number of parallel jobs (default: -1 for all CPUs)"
    echo "  --debug        Enable debug mode (saves debug files)"
    echo "  --viz          Enable visualization mode"
    exit 1
fi

RESULT_FILE="$1"
shift  # Remove the first argument, keep the rest

# Check if result file exists
if [ ! -f "$RESULT_FILE" ]; then
    echo "Error: Result file '$RESULT_FILE' does not exist"
    exit 1
fi

echo "Building Docker image for MMTU evaluate..."
docker build -f Dockerfile.evaluate -t mmtu-evaluate .

echo "Running evaluation on '$RESULT_FILE'..."
echo "Additional arguments: $@"

# Run the Docker container with volume mount
docker run --rm \
    -v "$(pwd)":/app \
    -w /app \
    -e MMTU_HOME=/app \
    mmtu-evaluate \
    "$RESULT_FILE" \
    "$@"

echo "Evaluation completed. Results saved in ./results/ directory."
