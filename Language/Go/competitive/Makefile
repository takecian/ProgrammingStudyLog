# Makefile for competitive programming in Go

.PHONY: help build run test clean examples

# Default target
help:
	@echo "Available targets:"
	@echo "  build FILE=<source.go> [OUT=<output>] - Build a Go source file"
	@echo "  run FILE=<source.go> [INPUT=<input.txt>] - Build and run a Go source file"
	@echo "  test FILE=<source.go> INPUT=<input.txt> EXPECTED=<expected.txt> - Test a solution"
	@echo "  examples - Build all example solutions"
	@echo "  clean - Remove all built binaries"
	@echo ""
	@echo "Examples:"
	@echo "  make build FILE=solution.go"
	@echo "  make run FILE=solution.go INPUT=input.txt"
	@echo "  make test FILE=solution.go INPUT=input.txt EXPECTED=expected.txt"

# Build a single file
build:
ifndef FILE
	@echo "Error: FILE parameter is required"
	@echo "Usage: make build FILE=<source.go> [OUT=<output>]"
	@exit 1
endif
	@echo "Building $(FILE)..."
	@go build -o $(or $(OUT),$(basename $(FILE) .go)) $(FILE)
	@echo "Build successful: $(or $(OUT),$(basename $(FILE) .go))"

# Run a solution
run:
ifndef FILE
	@echo "Error: FILE parameter is required"
	@echo "Usage: make run FILE=<source.go> [INPUT=<input.txt>]"
	@exit 1
endif
	@echo "Building and running $(FILE)..."
	@go build -o $(basename $(FILE) .go) $(FILE)
ifdef INPUT
	@./$(basename $(FILE) .go) < $(INPUT)
else
	@./$(basename $(FILE) .go)
endif
	@rm -f $(basename $(FILE) .go)

# Test a solution
test:
ifndef FILE
	@echo "Error: FILE parameter is required"
	@exit 1
endif
ifndef INPUT
	@echo "Error: INPUT parameter is required"
	@exit 1
endif
ifndef EXPECTED
	@echo "Error: EXPECTED parameter is required"
	@exit 1
endif
	@echo "Testing $(FILE)..."
	@go build -o $(basename $(FILE) .go) $(FILE)
	@ACTUAL=$$(./$(basename $(FILE) .go) < $(INPUT) 2>/dev/null); \
	EXPECTED_CONTENT=$$(cat $(EXPECTED)); \
	if [ "$$ACTUAL" = "$$EXPECTED_CONTENT" ]; then \
		echo "✅ Test PASSED"; \
		echo "Expected: $$EXPECTED_CONTENT"; \
		echo "Actual:   $$ACTUAL"; \
	else \
		echo "❌ Test FAILED"; \
		echo "Expected: $$EXPECTED_CONTENT"; \
		echo "Actual:   $$ACTUAL"; \
	fi
	@rm -f $(basename $(FILE) .go)

# Build all examples
examples:
	@echo "Building example solutions..."
	@for file in examples/*.go; do \
		if [ -f "$$file" ]; then \
			echo "Building $$file..."; \
			go build -o "examples/$$(basename $$file .go)" "$$file"; \
		fi \
	done
	@echo "All examples built successfully"

# Clean all binaries
clean:
	@echo "Cleaning up binaries..."
	@find . -name "*.exe" -delete 2>/dev/null || true
	@find . -type f -executable -not -name "*.sh" -not -name "*.go" -delete 2>/dev/null || true
	@echo "Cleanup complete"

# Quick template copy
template:
	@if [ -z "$(NAME)" ]; then \
		echo "Error: NAME parameter is required"; \
		echo "Usage: make template NAME=<filename>"; \
		exit 1; \
	fi
	@cp template.go $(NAME).go
	@echo "Template copied to $(NAME).go"
	@echo "Edit the solve() function to implement your solution"