# Go Interfaces

This directory contains examples of Go interfaces, from basic usage to advanced patterns and best practices.

## Files Overview

### `basic_interfaces.go`
- Basic interface definition and implementation
- Interface satisfaction (implicit implementation)
- Empty interface (`interface{}`) usage
- Type assertions with safety checks
- Type switches for runtime type checking
- Multiple interface embedding

### `interface_patterns.go`
- Strategy pattern implementation
- Adapter pattern for legacy code integration
- Decorator pattern for extending functionality
- Interface composition and embedding
- Standard library interface usage (io.Reader, io.Writer, Stringer, error)
- Interface nil gotchas and proper handling

## Running the Examples

To run any example:

```bash
cd Language/Go/fundamentals/interfaces
go run basic_interfaces.go
go run interface_patterns.go
```

## Key Interface Concepts

### Interface Definition
```go
type Shape interface {
    Area() float64
    Perimeter() float64
}
```

### Implicit Implementation
- No explicit "implements" keyword
- Types automatically satisfy interfaces by implementing required methods
- Duck typing: "If it walks like a duck and quacks like a duck, it's a duck"

### Empty Interface
- `interface{}` can hold any value
- Similar to `Object` in other languages
- Requires type assertions to access underlying value

### Interface Composition
- Interfaces can embed other interfaces
- Creates more complex contracts from simple ones
- Promotes interface segregation principle

## Design Patterns with Interfaces

### 1. Strategy Pattern
- Define family of algorithms as interfaces
- Make them interchangeable at runtime
- Encapsulate algorithm implementation details

### 2. Adapter Pattern
- Make incompatible interfaces work together
- Wrap legacy code with modern interfaces
- Enable code reuse without modification

### 3. Decorator Pattern
- Add behavior to objects dynamically
- Compose functionality through interface wrapping
- Alternative to inheritance for extending behavior

## Best Practices

### Interface Design
1. **Keep interfaces small** - Prefer many small interfaces over few large ones
2. **Accept interfaces, return structs** - Functions should accept interfaces but return concrete types
3. **Define interfaces at point of use** - Don't define interfaces until you need them
4. **Use composition over inheritance** - Embed interfaces to create complex contracts

### Type Assertions
1. **Always use the comma ok idiom** - `value, ok := interface.(Type)`
2. **Prefer type switches for multiple types** - More readable than multiple assertions
3. **Handle the false case** - Always check if assertion succeeded

### Common Pitfalls
1. **Interface nil gotcha** - Interface with nil pointer is not nil interface
2. **Over-engineering** - Don't create interfaces for single implementations
3. **Premature abstraction** - Start with concrete types, extract interfaces when needed

## Standard Library Interfaces

### Essential Interfaces
- `io.Reader` - Read data from a source
- `io.Writer` - Write data to a destination
- `io.Closer` - Close resources
- `fmt.Stringer` - String representation
- `error` - Error handling
- `sort.Interface` - Custom sorting

### Interface Composition Examples
- `io.ReadWriter` - Combines Reader and Writer
- `io.ReadCloser` - Combines Reader and Closer
- `io.WriteCloser` - Combines Writer and Closer
- `io.ReadWriteCloser` - Combines all three

## Performance Considerations

- Interface calls have slight overhead due to dynamic dispatch
- Empty interface requires boxing/unboxing
- Type assertions have runtime cost
- Use concrete types when performance is critical
- Profile before optimizing interface usage

## Testing with Interfaces

Interfaces make testing easier by allowing:
- Mock implementations for dependencies
- Dependency injection patterns
- Isolated unit testing
- Behavior verification over implementation details

## Next Steps

After mastering interfaces, explore:
- `../error-handling/` - Error handling patterns with interfaces
- `../concurrency/` - Interfaces in concurrent programming
- `../../libs/` - Real-world interface usage in algorithms