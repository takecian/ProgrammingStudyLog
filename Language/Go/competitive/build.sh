#!/bin/bash

# Build script for competitive programming solutions
# Usage: ./build.sh <source_file> [output_name]

set -e

if [ $# -eq 0 ]; then
    echo "Usage: $0 <source_file> [output_name]"
    echo "Example: $0 solution.go"
    echo "Example: $0 solution.go my_solution"
    exit 1
fi

SOURCE_FILE="$1"
OUTPUT_NAME="${2:-solution}"

# Check if source file exists
if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: Source file '$SOURCE_FILE' not found"
    exit 1
fi

# Build the Go program
echo "Building $SOURCE_FILE..."
go build -o "$OUTPUT_NAME" "$SOURCE_FILE"

if [ $? -eq 0 ]; then
    echo "Build successful: $OUTPUT_NAME"
    echo "Run with: ./$OUTPUT_NAME"
else
    echo "Build failed"
    exit 1
fi