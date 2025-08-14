# Go Basics

This directory contains fundamental Go language examples covering core syntax and concepts.

## Files Overview

### `variables.go`
- Variable declarations and initialization
- Type inference with `:=`
- Multiple variable declarations
- Zero values
- Constants
- Type conversions

### `functions.go`
- Basic function syntax
- Multiple return values
- Named return values
- Variadic functions
- Functions as variables
- Anonymous functions and closures
- Higher-order functions

### `control_flow.go`
- If statements (basic, with else, with initialization)
- Switch statements (basic, multiple values, expressions, type switch)
- For loops (basic, while-style, infinite with break/continue)
- Range loops (slices, maps, strings)
- Defer, panic, and recover

### `data_structures.go`
- Arrays (declaration, initialization, iteration)
- Slices (creation, append, slicing, copy, 2D slices)
- Maps (creation, operations, iteration)
- Structs (creation, literals, anonymous structs, methods)
- Pointers (basic usage, struct pointers, new function)

## Running the Examples

To run any example:

```bash
cd Language/Go/fundamentals/basics
go run variables.go
go run functions.go
go run control_flow.go
go run data_structures.go
```

## Key Go Concepts Demonstrated

1. **Type Safety**: Go is statically typed with compile-time type checking
2. **Zero Values**: All types have sensible zero values
3. **Multiple Return Values**: Functions can return multiple values
4. **Pointers**: Direct memory access with automatic dereferencing for structs
5. **Slices vs Arrays**: Dynamic vs fixed-size collections
6. **Maps**: Built-in hash table implementation
7. **Structs**: Custom types with methods
8. **Defer**: Cleanup and resource management
9. **Panic/Recover**: Error handling for exceptional cases

## Next Steps

After mastering these basics, explore:
- `../concurrency/` - Goroutines and channels
- `../interfaces/` - Interface patterns
- `../error-handling/` - Idiomatic error handling