#!/bin/bash

# Test script for competitive programming solutions
# Usage: ./test.sh <source_file> <input_file> <expected_output_file>

set -e

if [ $# -ne 3 ]; then
    echo "Usage: $0 <source_file> <input_file> <expected_output_file>"
    echo "Example: $0 solution.go input.txt expected.txt"
    exit 1
fi

SOURCE_FILE="$1"
INPUT_FILE="$2"
EXPECTED_FILE="$3"

# Check if files exist
for file in "$SOURCE_FILE" "$INPUT_FILE" "$EXPECTED_FILE"; do
    if [ ! -f "$file" ]; then
        echo "Error: File '$file' not found"
        exit 1
    fi
done

# Extract filename without extension for binary name
BINARY_NAME=$(basename "$SOURCE_FILE" .go)

# Build the program
echo "Building $SOURCE_FILE..."
go build -o "$BINARY_NAME" "$SOURCE_FILE"

if [ $? -ne 0 ]; then
    echo "Build failed"
    exit 1
fi

echo "Running test..."

# Run the program and capture output
ACTUAL_OUTPUT=$(./"$BINARY_NAME" < "$INPUT_FILE" 2>/dev/null)
EXPECTED_OUTPUT=$(cat "$EXPECTED_FILE")

# Compare outputs
if [ "$ACTUAL_OUTPUT" = "$EXPECTED_OUTPUT" ]; then
    echo "✅ Test PASSED"
    echo "Expected: $EXPECTED_OUTPUT"
    echo "Actual:   $ACTUAL_OUTPUT"
else
    echo "❌ Test FAILED"
    echo "Expected: $EXPECTED_OUTPUT"
    echo "Actual:   $ACTUAL_OUTPUT"
    echo ""
    echo "Diff:"
    diff <(echo "$EXPECTED_OUTPUT") <(echo "$ACTUAL_OUTPUT") || true
fi

# Clean up binary
rm -f "$BINARY_NAME"