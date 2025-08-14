package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// Scanner provides fast input operations for competitive programming
type Scanner struct {
	*bufio.Scanner
}

// NewScanner creates a new scanner with optimized buffer size for competitive programming
func NewScanner() *Scanner {
	scanner := bufio.NewScanner(os.Stdin)
	// Set large buffer for handling big inputs efficiently
	scanner.Buffer(make([]byte, 1000000), 1000000)
	scanner.Split(bufio.ScanWords)
	return &Scanner{scanner}
}

// Int reads and returns the next integer
func (s *Scanner) Int() int {
	s.Scan()
	n, err := strconv.Atoi(s.Text())
	if err != nil {
		panic(err)
	}
	return n
}

// Int64 reads and returns the next int64
func (s *Scanner) Int64() int64 {
	s.Scan()
	n, err := strconv.ParseInt(s.Text(), 10, 64)
	if err != nil {
		panic(err)
	}
	return n
}

// Float64 reads and returns the next float64
func (s *Scanner) Float64() float64 {
	s.Scan()
	f, err := strconv.ParseFloat(s.Text(), 64)
	if err != nil {
		panic(err)
	}
	return f
}

// String reads and returns the next string
func (s *Scanner) String() string {
	s.Scan()
	return s.Text()
}

// Ints reads n integers and returns them as a slice
func (s *Scanner) Ints(n int) []int {
	result := make([]int, n)
	for i := 0; i < n; i++ {
		result[i] = s.Int()
	}
	return result
}

// Int64s reads n int64s and returns them as a slice
func (s *Scanner) Int64s(n int) []int64 {
	result := make([]int64, n)
	for i := 0; i < n; i++ {
		result[i] = s.Int64()
	}
	return result
}

// Strings reads n strings and returns them as a slice
func (s *Scanner) Strings(n int) []string {
	result := make([]string, n)
	for i := 0; i < n; i++ {
		result[i] = s.String()
	}
	return result
}

// Line reads an entire line (useful for string problems)
func (s *Scanner) Line() string {
	s.Scanner.Split(bufio.ScanLines)
	s.Scan()
	line := s.Text()
	s.Scanner.Split(bufio.ScanWords) // Reset to word scanning
	return line
}

// Writer provides fast output operations
type Writer struct {
	*bufio.Writer
}

// NewWriter creates a new buffered writer for fast output
func NewWriter() *Writer {
	return &Writer{bufio.NewWriter(os.Stdout)}
}

// Printf writes formatted output
func (w *Writer) Printf(format string, args ...interface{}) {
	fmt.Fprintf(w.Writer, format, args...)
}

// Println writes a line with newline
func (w *Writer) Println(args ...interface{}) {
	fmt.Fprintln(w.Writer, args...)
}

// Print writes without newline
func (w *Writer) Print(args ...interface{}) {
	fmt.Fprint(w.Writer, args...)
}

// Flush flushes the buffer (call this at the end of main)
func (w *Writer) Flush() {
	w.Writer.Flush()
}

// Template main function - replace this with your solution
func main() {
	scanner := NewScanner()
	writer := NewWriter()
	defer writer.Flush()

	// Example usage:
	// n := scanner.Int()
	// arr := scanner.Ints(n)
	// writer.Println("Result:", result)

	// Your solution code here
	solve(scanner, writer)
}

// solve function - implement your solution logic here
func solve(scanner *Scanner, writer *Writer) {
	// Example: Read two integers and output their sum
	a := scanner.Int()
	b := scanner.Int()
	writer.Println(a + b)
}
