package main

import (
	"context"
	"errors"
	"fmt"
	"time"
)

// Advanced Error Handling Patterns
func main() {
	fmt.Println("=== Advanced Error Handling ===")

	// Sentinel errors
	demonstrateSentinelErrors()

	// Error types and behavior
	demonstrateErrorTypes()

	// Context-aware error handling
	demonstrateContextErrors()

	// Error handling in concurrent code
	demonstrateConcurrentErrors()

	// Panic and recover
	demonstratePanicRecover()
}

// Sentinel Errors - predefined error values
var (
	ErrInvalidInput     = errors.New("invalid input")
	ErrResourceBusy     = errors.New("resource is busy")
	ErrTimeout          = errors.New("operation timed out")
	ErrNotFound         = errors.New("resource not found")
	ErrPermissionDenied = errors.New("permission denied")
)

func demonstrateSentinelErrors() {
	fmt.Println("\n--- Sentinel Errors ---")

	// Using sentinel errors for specific conditions
	err := performOperation("invalid")
	if err != nil {
		// Check for specific error types
		switch {
		case errors.Is(err, ErrInvalidInput):
			fmt.Println("Handle invalid input error")
		case errors.Is(err, ErrResourceBusy):
			fmt.Println("Handle resource busy error")
		case errors.Is(err, ErrTimeout):
			fmt.Println("Handle timeout error")
		default:
			fmt.Printf("Handle unknown error: %v\n", err)
		}
	}

	// Successful operation
	err = performOperation("valid")
	if err != nil {
		fmt.Printf("Unexpected error: %v\n", err)
	} else {
		fmt.Println("Operation completed successfully")
	}
}

func performOperation(input string) error {
	switch input {
	case "invalid":
		return fmt.Errorf("operation failed: %w", ErrInvalidInput)
	case "busy":
		return fmt.Errorf("cannot perform operation: %w", ErrResourceBusy)
	case "timeout":
		return fmt.Errorf("operation failed: %w", ErrTimeout)
	case "valid":
		return nil
	default:
		return fmt.Errorf("unknown input: %s", input)
	}
}

// Error types with behavior
type TemporaryError interface {
	error
	Temporary() bool
}

type TimeoutError interface {
	error
	Timeout() bool
}

type NetworkError struct {
	Op        string
	Addr      string
	Err       error
	IsTemp    bool
	IsTimeout bool
}

func (ne *NetworkError) Error() string {
	return fmt.Sprintf("network error in %s to %s: %v", ne.Op, ne.Addr, ne.Err)
}

func (ne *NetworkError) Temporary() bool {
	return ne.IsTemp
}

func (ne *NetworkError) Timeout() bool {
	return ne.IsTimeout
}

func (ne *NetworkError) Unwrap() error {
	return ne.Err
}

type RetryableError struct {
	Err        error
	RetryAfter time.Duration
}

func (re *RetryableError) Error() string {
	return fmt.Sprintf("retryable error (retry after %v): %v", re.RetryAfter, re.Err)
}

func (re *RetryableError) Unwrap() error {
	return re.Err
}

func demonstrateErrorTypes() {
	fmt.Println("\n--- Error Types with Behavior ---")

	// Network error example
	netErr := &NetworkError{
		Op:        "connect",
		Addr:      "example.com:80",
		Err:       errors.New("connection refused"),
		IsTemp:    true,
		IsTimeout: false,
	}

	fmt.Printf("Network error: %v\n", netErr)

	// Check error behavior
	if tempErr, ok := netErr.(TemporaryError); ok && tempErr.Temporary() {
		fmt.Println("This is a temporary error - can retry")
	}

	if timeoutErr, ok := netErr.(TimeoutError); ok && timeoutErr.Timeout() {
		fmt.Println("This is a timeout error")
	} else {
		fmt.Println("Not a timeout error")
	}

	// Retryable error
	retryErr := &RetryableError{
		Err:        errors.New("service unavailable"),
		RetryAfter: 5 * time.Second,
	}

	fmt.Printf("Retryable error: %v\n", retryErr)
	handleRetryableError(retryErr)
}

func handleRetryableError(err error) {
	if retryErr, ok := err.(*RetryableError); ok {
		fmt.Printf("Should retry after: %v\n", retryErr.RetryAfter)
	}
}

func demonstrateContextErrors() {
	fmt.Println("\n--- Context-Aware Error Handling ---")

	// Context with timeout
	ctx, cancel := context.WithTimeout(context.Background(), 100*time.Millisecond)
	defer cancel()

	result, err := contextAwareOperation(ctx, 200*time.Millisecond)
	if err != nil {
		if errors.Is(err, context.DeadlineExceeded) {
			fmt.Println("Operation timed out")
		} else if errors.Is(err, context.Canceled) {
			fmt.Println("Operation was canceled")
		} else {
			fmt.Printf("Operation failed: %v\n", err)
		}
	} else {
		fmt.Printf("Operation result: %s\n", result)
	}

	// Context with cancellation
	ctx2, cancel2 := context.WithCancel(context.Background())

	// Cancel after 50ms
	go func() {
		time.Sleep(50 * time.Millisecond)
		cancel2()
	}()

	result, err = contextAwareOperation(ctx2, 100*time.Millisecond)
	if err != nil {
		if errors.Is(err, context.Canceled) {
			fmt.Println("Operation was canceled by user")
		} else {
			fmt.Printf("Operation failed: %v\n", err)
		}
	} else {
		fmt.Printf("Operation result: %s\n", result)
	}
}

func contextAwareOperation(ctx context.Context, duration time.Duration) (string, error) {
	// Simulate work with context checking
	select {
	case <-time.After(duration):
		return "operation completed", nil
	case <-ctx.Done():
		return "", fmt.Errorf("operation interrupted: %w", ctx.Err())
	}
}

func demonstrateConcurrentErrors() {
	fmt.Println("\n--- Concurrent Error Handling ---")

	// Error aggregation from multiple goroutines
	errors := make(chan error, 3)

	// Start multiple workers
	for i := 1; i <= 3; i++ {
		go func(id int) {
			err := workerTask(id)
			errors <- err
		}(i)
	}

	// Collect errors
	var allErrors []error
	for i := 0; i < 3; i++ {
		if err := <-errors; err != nil {
			allErrors = append(allErrors, err)
		}
	}

	if len(allErrors) > 0 {
		fmt.Printf("Found %d errors:\n", len(allErrors))
		for i, err := range allErrors {
			fmt.Printf("  %d: %v\n", i+1, err)
		}
	} else {
		fmt.Println("All workers completed successfully")
	}

	// Error handling with context and goroutines
	ctx, cancel := context.WithTimeout(context.Background(), 150*time.Millisecond)
	defer cancel()

	result, err := coordinatedWork(ctx)
	if err != nil {
		fmt.Printf("Coordinated work failed: %v\n", err)
	} else {
		fmt.Printf("Coordinated work result: %v\n", result)
	}
}

func workerTask(id int) error {
	// Simulate work that might fail
	time.Sleep(time.Duration(id*20) * time.Millisecond)

	if id == 2 {
		return fmt.Errorf("worker %d failed", id)
	}

	fmt.Printf("Worker %d completed successfully\n", id)
	return nil
}

func coordinatedWork(ctx context.Context) ([]string, error) {
	results := make(chan string, 2)
	errors := make(chan error, 2)

	// Start two workers
	go func() {
		result, err := slowWork(ctx, "task1", 100*time.Millisecond)
		if err != nil {
			errors <- err
		} else {
			results <- result
		}
	}()

	go func() {
		result, err := slowWork(ctx, "task2", 80*time.Millisecond)
		if err != nil {
			errors <- err
		} else {
			results <- result
		}
	}()

	// Collect results or errors
	var finalResults []string
	var finalError error

	for i := 0; i < 2; i++ {
		select {
		case result := <-results:
			finalResults = append(finalResults, result)
		case err := <-errors:
			if finalError == nil {
				finalError = err
			} else {
				finalError = fmt.Errorf("multiple errors: %v; %w", finalError, err)
			}
		case <-ctx.Done():
			return nil, fmt.Errorf("coordinated work canceled: %w", ctx.Err())
		}
	}

	if finalError != nil {
		return nil, finalError
	}

	return finalResults, nil
}

func slowWork(ctx context.Context, name string, duration time.Duration) (string, error) {
	select {
	case <-time.After(duration):
		return fmt.Sprintf("completed %s", name), nil
	case <-ctx.Done():
		return "", fmt.Errorf("%s canceled: %w", name, ctx.Err())
	}
}

func demonstratePanicRecover() {
	fmt.Println("\n--- Panic and Recover ---")

	// Safe function that recovers from panic
	fmt.Println("Calling safe function that might panic:")
	result := safeFunction()
	fmt.Printf("Safe function result: %s\n", result)

	// Function that panics
	fmt.Println("Calling function that will panic:")
	result = safeFunctionWithPanic()
	fmt.Printf("Function with panic result: %s\n", result)

	// Panic with custom error
	fmt.Println("Calling function with custom panic:")
	err := functionWithCustomPanic()
	if err != nil {
		fmt.Printf("Recovered error: %v\n", err)
	}

	fmt.Println("Program continues after panic recovery")
}

func safeFunction() string {
	defer func() {
		if r := recover(); r != nil {
			fmt.Printf("Recovered from panic: %v\n", r)
		}
	}()

	// This won't panic
	return "normal execution"
}

func safeFunctionWithPanic() string {
	defer func() {
		if r := recover(); r != nil {
			fmt.Printf("Recovered from panic: %v\n", r)
		}
	}()

	// This will panic
	panic("something went wrong!")

	return "this won't be reached"
}

func functionWithCustomPanic() (err error) {
	defer func() {
		if r := recover(); r != nil {
			// Convert panic to error
			switch v := r.(type) {
			case error:
				err = fmt.Errorf("panic recovered: %w", v)
			case string:
				err = fmt.Errorf("panic recovered: %s", v)
			default:
				err = fmt.Errorf("panic recovered: %v", v)
			}
		}
	}()

	// Simulate some work
	riskyOperation()

	return nil
}

func riskyOperation() {
	// Simulate a condition that causes panic
	var slice []int
	_ = slice[10] // This will panic with index out of range
}
