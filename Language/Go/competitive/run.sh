#!/bin/bash

# Run script for competitive programming solutions
# Usage: ./run.sh <source_file> [input_file]

set -e

if [ $# -eq 0 ]; then
    echo "Usage: $0 <source_file> [input_file]"
    echo "Example: $0 solution.go"
    echo "Example: $0 solution.go input.txt"
    echo "Example: echo '5 3' | $0 solution.go"
    exit 1
fi

SOURCE_FILE="$1"
INPUT_FILE="$2"

# Check if source file exists
if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: Source file '$SOURCE_FILE' not found"
    exit 1
fi

# Extract filename without extension for binary name
BINARY_NAME=$(basename "$SOURCE_FILE" .go)

# Build the program
echo "Building $SOURCE_FILE..."
go build -o "$BINARY_NAME" "$SOURCE_FILE"

if [ $? -ne 0 ]; then
    echo "Build failed"
    exit 1
fi

echo "Running $BINARY_NAME..."

# Run with input file if provided, otherwise use stdin
if [ -n "$INPUT_FILE" ]; then
    if [ ! -f "$INPUT_FILE" ]; then
        echo "Error: Input file '$INPUT_FILE' not found"
        exit 1
    fi
    ./"$BINARY_NAME" < "$INPUT_FILE"
else
    ./"$BINARY_NAME"
fi

# Clean up binary
rm -f "$BINARY_NAME"