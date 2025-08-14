# Go Error Handling

This directory contains comprehensive examples of Go's error handling patterns, from basic error handling to advanced patterns and best practices.

## Files Overview

### `basic_errors.go`
- Basic error handling with multiple return values
- Creating custom error types
- Error wrapping and unwrapping with `fmt.Errorf` and `%w`
- Using `errors.Is` and `errors.As` for error checking
- Multiple return values with errors
- Common error handling patterns (early return, error accumulation, retry)

### `advanced_errors.go`
- Sentinel errors for specific error conditions
- Error types with behavior (Temporary, Timeout interfaces)
- Context-aware error handling with cancellation and timeouts
- Concurrent error handling and aggregation
- Panic and recover mechanisms
- Converting panics to errors

## Running the Examples

To run any example:

```bash
cd Language/Go/fundamentals/error-handling
go run basic_errors.go
go run advanced_errors.go
```

## Key Error Handling Concepts

### The Error Interface
```go
type error interface {
    Error() string
}
```

### Multiple Return Values
Go's idiomatic error handling uses multiple return values:
```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("division by zero")
    }
    return a / b, nil
}
```

### Error Checking Pattern
```go
result, err := someFunction()
if err != nil {
    // handle error
    return err
}
// use result
```

## Error Types and Patterns

### 1. Simple Errors
- `errors.New("message")` - Create simple error
- `fmt.Errorf("format %s", value)` - Formatted error

### 2. Custom Error Types
```go
type ValidationError struct {
    Field   string
    Value   interface{}
    Message string
}

func (ve ValidationError) Error() string {
    return fmt.Sprintf("validation error: %s", ve.Message)
}
```

### 3. Sentinel Errors
Predefined error values for specific conditions:
```go
var ErrNotFound = errors.New("not found")
var ErrInvalidInput = errors.New("invalid input")
```

### 4. Error Wrapping
Add context while preserving original error:
```go
return fmt.Errorf("failed to process file %s: %w", filename, err)
```

### 5. Error Unwrapping
```go
// Check if error is specific type
if errors.Is(err, ErrNotFound) {
    // handle not found
}

// Extract specific error type
var validationErr ValidationError
if errors.As(err, &validationErr) {
    // use validationErr
}
```

## Advanced Patterns

### Behavioral Interfaces
Define error behavior through interfaces:
```go
type TemporaryError interface {
    error
    Temporary() bool
}

type TimeoutError interface {
    error
    Timeout() bool
}
```

### Context-Aware Errors
Handle cancellation and timeouts:
```go
func operation(ctx context.Context) error {
    select {
    case <-time.After(time.Second):
        return nil
    case <-ctx.Done():
        return ctx.Err() // context.Canceled or context.DeadlineExceeded
    }
}
```

### Concurrent Error Handling
Aggregate errors from multiple goroutines:
```go
errors := make(chan error, numWorkers)
for i := 0; i < numWorkers; i++ {
    go func() {
        errors <- worker()
    }()
}

var allErrors []error
for i := 0; i < numWorkers; i++ {
    if err := <-errors; err != nil {
        allErrors = append(allErrors, err)
    }
}
```

## Best Practices

### Error Handling
1. **Always check errors** - Don't ignore returned errors
2. **Handle errors at the right level** - Don't pass errors up unnecessarily
3. **Add context when wrapping** - Use `fmt.Errorf` with `%w` verb
4. **Use sentinel errors for expected conditions** - Define package-level error variables
5. **Create custom error types for complex cases** - When you need additional information

### Error Design
1. **Error messages should be lowercase** - Unless starting with proper noun
2. **Don't use punctuation in error messages** - Keep them simple
3. **Error messages should be actionable** - Help users understand what went wrong
4. **Use error wrapping to preserve context** - Don't lose the original error
5. **Consider error behavior interfaces** - For errors that need special handling

### Performance Considerations
- Error creation has some overhead
- Error wrapping creates additional allocations
- Use error pools for high-frequency errors if needed
- Consider error codes for performance-critical paths

## Common Patterns

### Early Return
```go
func processData(data []byte) error {
    if len(data) == 0 {
        return errors.New("empty data")
    }
    
    if err := validate(data); err != nil {
        return fmt.Errorf("validation failed: %w", err)
    }
    
    // continue processing
    return nil
}
```

### Error Accumulation
```go
func validateAll(items []Item) []error {
    var errors []error
    for _, item := range items {
        if err := validate(item); err != nil {
            errors = append(errors, err)
        }
    }
    return errors
}
```

### Retry Pattern
```go
func retryOperation(maxRetries int) error {
    var lastErr error
    for i := 0; i < maxRetries; i++ {
        if err := operation(); err != nil {
            lastErr = err
            continue
        }
        return nil
    }
    return fmt.Errorf("failed after %d retries: %w", maxRetries, lastErr)
}
```

## Panic and Recover

### When to Use Panic
- Unrecoverable errors (programming bugs)
- Library initialization failures
- Impossible conditions

### When to Use Recover
- Library boundaries (convert panic to error)
- Server applications (prevent crashes)
- Testing frameworks

### Panic/Recover Pattern
```go
func safeFunction() (err error) {
    defer func() {
        if r := recover(); r != nil {
            err = fmt.Errorf("panic recovered: %v", r)
        }
    }()
    
    riskyOperation()
    return nil
}
```

## Testing Error Handling

```go
func TestErrorHandling(t *testing.T) {
    _, err := divide(10, 0)
    if err == nil {
        t.Error("expected error for division by zero")
    }
    
    if !errors.Is(err, ErrDivisionByZero) {
        t.Errorf("expected ErrDivisionByZero, got %v", err)
    }
}
```

## Next Steps

After mastering error handling, explore:
- `../concurrency/` - Error handling in concurrent programs
- `../interfaces/` - Error interfaces and patterns
- `../../libs/` - Real-world error handling in algorithms and data structures