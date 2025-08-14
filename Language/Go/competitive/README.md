# Competitive Programming in Go

This directory contains templates, utilities, and examples for competitive programming in Go. It provides fast I/O operations, common utility functions, and build scripts optimized for competitive programming contests.

## Quick Start

1. **Copy the template:**
   ```bash
   cp template.go my_solution.go
   ```

2. **Edit the solve function:**
   ```go
   func solve(scanner *Scanner, writer *Writer) {
       // Your solution code here
       n := scanner.Int()
       arr := scanner.Ints(n)
       result := processArray(arr)
       writer.Println(result)
   }
   ```

3. **Build and run:**
   ```bash
   ./run.sh my_solution.go input.txt
   # or
   make run FILE=my_solution.go INPUT=input.txt
   ```

## Files Overview

### Core Files
- `template.go` - Main template with fast I/O scanner and writer
- `utils.go` - Common utility functions for competitive programming
- `README.md` - This documentation

### Build Scripts
- `build.sh` - Build a Go source file
- `run.sh` - Build and run a Go source file with optional input
- `test.sh` - Test a solution against expected output
- `Makefile` - Make targets for build automation

### Examples
- `examples/example_solution.go` - Simple example (AtCoder ABC001 A)
- `examples/array_example.go` - Array processing with utilities

## Template Features

### Fast I/O Scanner
```go
scanner := NewScanner()

// Read single values
n := scanner.Int()           // Read integer
x := scanner.Int64()         // Read int64
f := scanner.Float64()       // Read float64
s := scanner.String()        // Read string
line := scanner.Line()       // Read entire line

// Read arrays
arr := scanner.Ints(n)       // Read n integers
arr64 := scanner.Int64s(n)   // Read n int64s
strs := scanner.Strings(n)   // Read n strings
```

### Fast Output Writer
```go
writer := NewWriter()
defer writer.Flush()  // Important: flush at end

writer.Print("Hello")           // Print without newline
writer.Println("World")         // Print with newline
writer.Printf("Value: %d\n", x) // Formatted print
```

## Utility Functions

### Math Functions
```go
Min(a, b)              // Minimum of two integers
Max(a, b)              // Maximum of two integers
Abs(x)                 // Absolute value
GCD(a, b)              // Greatest common divisor
LCM(a, b)              // Least common multiple
Pow(base, exp)         // Fast exponentiation
PowMod(base, exp, mod) // Modular exponentiation
```

### Array/Slice Functions
```go
ReverseInts(arr)       // Reverse integer slice in place
SumInts(arr)           // Sum of all integers
MaxInSlice(arr)        // Maximum value in slice
MinInSlice(arr)        // Minimum value in slice
UniqueInts(arr)        // Remove duplicates (preserves order)
```

### String Functions
```go
ReverseString(s)       // Reverse a string
IsPalindrome(s)        // Check if string is palindrome
ParseInts(s)           // Parse space-separated integers
JoinInts(arr, sep)     // Join integers with separator
```

### Search Functions
```go
BinarySearch(arr, target)  // Binary search in sorted array
LowerBound(arr, target)    // First index where arr[i] >= target
UpperBound(arr, target)    // First index where arr[i] > target
```

### Combinatorics
```go
Factorial(n)           // n! factorial
Combination(n, r)      // C(n,r) combinations
Permutation(n, r)      // P(n,r) permutations
```

### Grid/2D Utilities
```go
Directions4            // 4-directional movement vectors
Directions8            // 8-directional movement vectors
IsValidPosition(r, c, rows, cols)  // Check bounds
Make2DIntSlice(rows, cols)         // Create 2D int slice
Make2DBoolSlice(rows, cols)        // Create 2D bool slice
```

## Build and Run Options

### Using Shell Scripts
```bash
# Build only
./build.sh solution.go [output_name]

# Build and run
./run.sh solution.go [input.txt]

# Test against expected output
./test.sh solution.go input.txt expected.txt
```

### Using Makefile
```bash
# Build
make build FILE=solution.go [OUT=my_solution]

# Run
make run FILE=solution.go [INPUT=input.txt]

# Test
make test FILE=solution.go INPUT=input.txt EXPECTED=expected.txt

# Build all examples
make examples

# Clean binaries
make clean

# Copy template
make template NAME=my_solution
```

### Direct Go Commands
```bash
# Build and run
go run solution.go < input.txt

# Build binary
go build -o solution solution.go
./solution < input.txt
```

## Performance Tips

1. **Use the provided Scanner and Writer** - They're optimized for competitive programming with large buffers
2. **Avoid fmt.Scan* functions** - They're slower than the custom scanner
3. **Always defer writer.Flush()** - Ensures output is written
4. **Use appropriate data types** - int64 for large numbers, int for most cases
5. **Preallocate slices when size is known** - `make([]int, n)` instead of `append()`

## Common Patterns

### Reading Test Cases
```go
func solve(scanner *Scanner, writer *Writer) {
    t := scanner.Int()  // Number of test cases
    for i := 0; i < t; i++ {
        // Process each test case
        n := scanner.Int()
        arr := scanner.Ints(n)
        result := processTestCase(arr)
        writer.Println(result)
    }
}
```

### Grid Input
```go
func solve(scanner *Scanner, writer *Writer) {
    h, w := scanner.Int(), scanner.Int()
    grid := make([]string, h)
    for i := 0; i < h; i++ {
        grid[i] = scanner.String()
    }
    // Process grid...
}
```

### Multiple Outputs
```go
func solve(scanner *Scanner, writer *Writer) {
    n := scanner.Int()
    results := make([]int, n)
    for i := 0; i < n; i++ {
        results[i] = processItem(scanner.Int())
    }
    
    // Output all results
    for i, result := range results {
        if i > 0 {
            writer.Print(" ")
        }
        writer.Print(result)
    }
    writer.Println()
}
```

## Examples

See the `examples/` directory for complete working examples:
- `example_solution.go` - Simple two-number input/output
- `array_example.go` - Array processing with statistics

## Contest Platform Integration

This template works well with:
- **AtCoder** - Fast I/O handles large inputs efficiently
- **Codeforces** - Compatible with standard input/output format
- **LeetCode** - Can be adapted for function-based problems
- **Google Code Jam** - Supports multiple test case format

## Debugging Tips

1. **Add debug prints:**
   ```go
   if false {  // Set to true for debugging
       writer.Printf("Debug: n=%d, arr=%v\n", n, arr)
   }
   ```

2. **Use small test cases first**
3. **Check edge cases:** empty input, single element, maximum constraints
4. **Verify time complexity** against problem constraints

## Time Complexity Reference

- **Input/Output:** O(n) for n elements
- **Sorting:** O(n log n)
- **Binary Search:** O(log n)
- **GCD:** O(log min(a,b))
- **Most utilities:** O(1) or O(n) as documented