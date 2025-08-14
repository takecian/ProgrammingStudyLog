# Go Fundamentals

This directory contains comprehensive examples and tutorials for learning Go language fundamentals. Each subdirectory focuses on a specific aspect of Go programming with practical examples and detailed explanations.

## Directory Structure

### `basics/`
Core Go language syntax and concepts:
- **Variables and Types** - Variable declarations, type inference, constants, type conversions
- **Functions** - Function syntax, multiple returns, variadic functions, closures, higher-order functions
- **Control Flow** - If statements, switch statements, for loops, range loops, defer/panic/recover
- **Data Structures** - Arrays, slices, maps, structs, pointers

### `concurrency/`
Go's concurrency features and patterns:
- **Goroutines** - Lightweight threads, synchronization with WaitGroup, race conditions, mutexes
- **Channels** - Communication between goroutines, buffered channels, select statements, channel patterns
- **Advanced Patterns** - Context for cancellation, rate limiting, producer-consumer, pub-sub, semaphores

### `interfaces/`
Interface concepts and design patterns:
- **Basic Interfaces** - Interface definition, satisfaction, empty interface, type assertions, type switches
- **Interface Patterns** - Strategy, adapter, decorator patterns, interface composition, standard library interfaces

### `error-handling/`
Comprehensive error handling in Go:
- **Basic Errors** - Error interface, custom errors, error wrapping, multiple returns, common patterns
- **Advanced Errors** - Sentinel errors, behavioral interfaces, context-aware errors, concurrent error handling, panic/recover

## Learning Path

### Beginner (Start Here)
1. **basics/variables.go** - Learn Go syntax and type system
2. **basics/functions.go** - Understand function definitions and usage
3. **basics/control_flow.go** - Master control structures
4. **basics/data_structures.go** - Work with Go's built-in data types

### Intermediate
1. **interfaces/basic_interfaces.go** - Understand Go's interface system
2. **error-handling/basic_errors.go** - Learn idiomatic error handling
3. **concurrency/goroutines.go** - Introduction to concurrent programming
4. **concurrency/channels.go** - Master channel-based communication

### Advanced
1. **interfaces/interface_patterns.go** - Design patterns with interfaces
2. **error-handling/advanced_errors.go** - Advanced error handling techniques
3. **concurrency/patterns.go** - Complex concurrency patterns
4. **Integration** - Combine concepts in real projects

## Running the Examples

Each subdirectory contains runnable Go programs. To execute any example:

```bash
# Navigate to the fundamentals directory
cd Language/Go/fundamentals

# Run a specific example
go run basics/variables.go
go run concurrency/goroutines.go
go run interfaces/basic_interfaces.go
go run error-handling/basic_errors.go

# Or navigate to a specific subdirectory
cd basics
go run variables.go
```

## Key Go Concepts Covered

### Language Features
- **Static Typing** with type inference
- **Garbage Collection** for memory management
- **Composition over Inheritance** design philosophy
- **Explicit Error Handling** with multiple return values
- **Built-in Concurrency** with goroutines and channels

### Design Principles
- **Simplicity** - Simple, readable syntax
- **Orthogonality** - Features work well together
- **Composition** - Build complex behavior from simple parts
- **Explicit** - No hidden behavior or magic
- **Concurrent** - Built for concurrent programming

### Best Practices
- Use interfaces to define behavior
- Handle errors explicitly
- Prefer composition over embedding
- Keep interfaces small and focused
- Use channels for communication between goroutines
- Write clear, readable code

## Go Idioms and Conventions

### Naming
- Use camelCase for variables and functions
- Use PascalCase for exported identifiers
- Use short, descriptive names
- Prefer `i` over `index` for loop variables

### Error Handling
```go
if err != nil {
    return err
}
```

### Interface Design
- Accept interfaces, return structs
- Keep interfaces small (1-3 methods)
- Define interfaces at point of use

### Concurrency
- Don't communicate by sharing memory; share memory by communicating
- Use channels for synchronization
- Always handle channel closing

## Common Patterns

### Constructor Pattern
```go
func NewPerson(name string, age int) *Person {
    return &Person{
        Name: name,
        Age:  age,
    }
}
```

### Options Pattern
```go
type Option func(*Config)

func WithTimeout(timeout time.Duration) Option {
    return func(c *Config) {
        c.Timeout = timeout
    }
}
```

### Builder Pattern
```go
type QueryBuilder struct {
    query string
}

func (qb *QueryBuilder) Select(fields string) *QueryBuilder {
    qb.query += "SELECT " + fields
    return qb
}
```

## Testing Your Understanding

After working through the examples, try these exercises:

1. **Create a simple calculator** using functions and error handling
2. **Implement a concurrent web scraper** using goroutines and channels
3. **Design a plugin system** using interfaces
4. **Build a retry mechanism** with context and error handling
5. **Create a rate limiter** using channels and time

## Next Steps

After mastering the fundamentals:

1. **Explore the standard library** - `io`, `net/http`, `encoding/json`, etc.
2. **Build real projects** - CLI tools, web services, APIs
3. **Learn testing** - Unit tests, benchmarks, table-driven tests
4. **Study advanced topics** - Reflection, unsafe, cgo
5. **Contribute to open source** - Practice with real Go codebases

## Resources

- [Official Go Documentation](https://golang.org/doc/)
- [Effective Go](https://golang.org/doc/effective_go.html)
- [Go Code Review Comments](https://github.com/golang/go/wiki/CodeReviewComments)
- [Go Proverbs](https://go-proverbs.github.io/)
- [The Go Programming Language](https://www.gopl.io/) (book)

## Getting Help

- [Go Forum](https://forum.golangbridge.org/)
- [Go Slack](https://gophers.slack.com/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/go)
- [Reddit r/golang](https://www.reddit.com/r/golang/)

Happy learning Go! 🚀