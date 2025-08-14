// Example: Array processing with utility functions
// Problem: Given an array of integers, find the sum, max, min, and check if it's sorted
// This demonstrates various utility functions from utils.go

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

// Scanner and utility functions (copied from template for standalone example)
type Scanner struct {
	*bufio.Scanner
}

func NewScanner() *Scanner {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)
	scanner.Split(bufio.ScanWords)
	return &Scanner{scanner}
}

func (s *Scanner) Int() int {
	s.Scan()
	n, err := strconv.Atoi(s.Text())
	if err != nil {
		panic(err)
	}
	return n
}

func (s *Scanner) Ints(n int) []int {
	result := make([]int, n)
	for i := 0; i < n; i++ {
		result[i] = s.Int()
	}
	return result
}

type Writer struct {
	*bufio.Writer
}

func NewWriter() *Writer {
	return &Writer{bufio.NewWriter(os.Stdout)}
}

func (w *Writer) Printf(format string, args ...interface{}) {
	fmt.Fprintf(w.Writer, format, args...)
}

func (w *Writer) Println(args ...interface{}) {
	fmt.Fprintln(w.Writer, args...)
}

func (w *Writer) Flush() {
	w.Writer.Flush()
}

// Utility functions
func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func SumInts(arr []int) int {
	sum := 0
	for _, v := range arr {
		sum += v
	}
	return sum
}

func MaxInSlice(arr []int) int {
	if len(arr) == 0 {
		panic("empty slice")
	}
	max := arr[0]
	for _, v := range arr[1:] {
		if v > max {
			max = v
		}
	}
	return max
}

func MinInSlice(arr []int) int {
	if len(arr) == 0 {
		panic("empty slice")
	}
	min := arr[0]
	for _, v := range arr[1:] {
		if v < min {
			min = v
		}
	}
	return min
}

func IsSorted(arr []int) bool {
	for i := 1; i < len(arr); i++ {
		if arr[i] < arr[i-1] {
			return false
		}
	}
	return true
}

func main() {
	scanner := NewScanner()
	writer := NewWriter()
	defer writer.Flush()

	solve(scanner, writer)
}

func solve(scanner *Scanner, writer *Writer) {
	// Read array size and elements
	n := scanner.Int()
	arr := scanner.Ints(n)

	// Calculate statistics using utility functions
	sum := SumInts(arr)
	maxVal := MaxInSlice(arr)
	minVal := MinInSlice(arr)
	sorted := IsSorted(arr)

	// Output results
	writer.Printf("Array: %v\n", arr)
	writer.Printf("Sum: %d\n", sum)
	writer.Printf("Max: %d\n", maxVal)
	writer.Printf("Min: %d\n", minVal)
	writer.Printf("Is sorted: %t\n", sorted)

	// Demonstrate sorting
	sortedArr := make([]int, len(arr))
	copy(sortedArr, arr)
	sort.Ints(sortedArr)
	writer.Printf("Sorted: %v\n", sortedArr)

	// Find median
	median := sortedArr[len(sortedArr)/2]
	if len(sortedArr)%2 == 0 {
		median = (sortedArr[len(sortedArr)/2-1] + sortedArr[len(sortedArr)/2]) / 2
	}
	writer.Printf("Median: %d\n", median)
}

/*
Sample Input:
5
3 1 4 1 5

Sample Output:
Array: [3 1 4 1 5]
Sum: 14
Max: 5
Min: 1
Is sorted: false
Sorted: [1 1 3 4 5]
Median: 3

Explanation:
This example demonstrates various array processing utilities:
- Reading an array using the fast I/O template
- Computing sum, max, min using utility functions
- Checking if array is sorted
- Sorting and finding median
*/
