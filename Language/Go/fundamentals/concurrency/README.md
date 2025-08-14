# Go Concurrency

This directory contains examples of Go's concurrency features, including goroutines, channels, and advanced patterns.

## Files Overview

### `goroutines.go`
- Basic goroutine creation and execution
- Multiple goroutines with different execution patterns
- WaitGroup for synchronization
- Race conditions and mutex for safe shared access
- Worker pool pattern implementation

### `channels.go`
- Basic channel operations (send/receive)
- Buffered vs unbuffered channels
- Channel directions (send-only, receive-only)
- Select statement for multiplexing
- Channel closing and range operations
- Common channel patterns (fan-out, pipeline)

### `patterns.go`
- Context for cancellation and timeouts
- Rate limiting patterns (simple and bursty)
- Producer-Consumer pattern with bounded buffer
- Publish-Subscribe pattern implementation
- Semaphore pattern for limiting concurrency

## Running the Examples

To run any example:

```bash
cd Language/Go/fundamentals/concurrency
go run goroutines.go
go run channels.go
go run patterns.go
```

## Key Concurrency Concepts

### Goroutines
- Lightweight threads managed by Go runtime
- Started with `go` keyword
- Communicate via channels or shared memory (with synchronization)

### Channels
- Type-safe communication between goroutines
- Unbuffered channels provide synchronization
- Buffered channels allow asynchronous communication
- Can be closed to signal completion

### Synchronization Primitives
- **WaitGroup**: Wait for multiple goroutines to complete
- **Mutex**: Mutual exclusion for shared data
- **Context**: Cancellation and timeout handling

### Common Patterns

1. **Worker Pool**: Fixed number of workers processing jobs from a queue
2. **Fan-out/Fan-in**: Distribute work to multiple goroutines and collect results
3. **Pipeline**: Chain of processing stages connected by channels
4. **Producer-Consumer**: Separate data production from consumption
5. **Publish-Subscribe**: Message broadcasting to multiple subscribers
6. **Rate Limiting**: Control the rate of operations
7. **Semaphore**: Limit concurrent access to resources

## Best Practices

1. **Don't communicate by sharing memory; share memory by communicating**
2. Use channels for communication between goroutines
3. Use mutexes only when channels are not suitable
4. Always handle channel closing properly
5. Use context for cancellation and timeouts
6. Avoid goroutine leaks by ensuring proper cleanup
7. Use buffered channels judiciously to avoid blocking

## Performance Considerations

- Goroutines are cheap (2KB initial stack)
- Channel operations have some overhead
- Select statement is efficient for multiplexing
- Context switching is handled by Go runtime
- Use profiling tools to identify bottlenecks

## Next Steps

After mastering concurrency, explore:
- `../interfaces/` - Interface patterns that work well with concurrency
- `../error-handling/` - Error handling in concurrent programs
- `../../libs/` - Concurrent data structures and algorithms