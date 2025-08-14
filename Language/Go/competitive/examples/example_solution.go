// Example: AtCoder ABC001 A -積雪深差 (Snow Depth Difference)
// Problem: Given two integers representing snow depths, output their difference
// Input: Two integers h1 and h2
// Output: h1 - h2

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

// NewScanner creates a new scanner with optimized buffer size
func NewScanner() *Scanner {
	scanner := bufio.NewScanner(os.Stdin)
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

// Writer provides fast output operations
type Writer struct {
	*bufio.Writer
}

// NewWriter creates a new buffered writer for fast output
func NewWriter() *Writer {
	return &Writer{bufio.NewWriter(os.Stdout)}
}

// Println writes a line with newline
func (w *Writer) Println(args ...interface{}) {
	fmt.Fprintln(w.Writer, args...)
}

// Flush flushes the buffer
func (w *Writer) Flush() {
	w.Writer.Flush()
}

func main() {
	scanner := NewScanner()
	writer := NewWriter()
	defer writer.Flush()

	solve(scanner, writer)
}

func solve(scanner *Scanner, writer *Writer) {
	// Read two snow depth values
	h1 := scanner.Int()
	h2 := scanner.Int()

	// Calculate and output the difference
	difference := h1 - h2
	writer.Println(difference)
}

/*
Sample Input:
100
50

Sample Output:
50

Explanation:
The difference between snow depths 100 and 50 is 50.
*/
