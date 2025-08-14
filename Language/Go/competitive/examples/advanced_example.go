// Advanced Example: Multiple test cases with various utility functions
// Problem: For each test case, given an array, output:
// 1. Sum of all elements
// 2. Maximum element
// 3. Whether the array is sorted
// 4. GCD of all elements

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

// Fast I/O components
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

func IsSorted(arr []int) bool {
	for i := 1; i < len(arr); i++ {
		if arr[i] < arr[i-1] {
			return false
		}
	}
	return true
}

func GCD(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func GCDArray(arr []int) int {
	if len(arr) == 0 {
		return 0
	}
	result := arr[0]
	for i := 1; i < len(arr); i++ {
		result = GCD(result, arr[i])
		if result == 1 {
			break // Early termination
		}
	}
	return result
}

func main() {
	scanner := NewScanner()
	writer := NewWriter()
	defer writer.Flush()

	solve(scanner, writer)
}

func solve(scanner *Scanner, writer *Writer) {
	t := scanner.Int() // Number of test cases

	for testCase := 1; testCase <= t; testCase++ {
		n := scanner.Int()
		arr := scanner.Ints(n)

		// Calculate statistics
		sum := SumInts(arr)
		maxVal := MaxInSlice(arr)
		sorted := IsSorted(arr)
		gcd := GCDArray(arr)

		// Output results for this test case
		writer.Printf("Case %d:\n", testCase)
		writer.Printf("  Sum: %d\n", sum)
		writer.Printf("  Max: %d\n", maxVal)
		writer.Printf("  Sorted: %t\n", sorted)
		writer.Printf("  GCD: %d\n", gcd)

		// Bonus: show sorted version if not already sorted
		if !sorted {
			sortedArr := make([]int, len(arr))
			copy(sortedArr, arr)
			sort.Ints(sortedArr)
			writer.Printf("  Sorted version: %v\n", sortedArr)
		}

		if testCase < t {
			writer.Println() // Empty line between test cases
		}
	}
}

/*
Sample Input:
3
4
3 1 4 2
3
1 2 3
5
6 9 12 15 18

Sample Output:
Case 1:
  Sum: 10
  Max: 4
  Sorted: false
  GCD: 1
  Sorted version: [1 2 3 4]

Case 2:
  Sum: 6
  Max: 3
  Sorted: true
  GCD: 1

Case 3:
  Sum: 60
  Max: 18
  Sorted: true
  GCD: 3

Explanation:
This example demonstrates:
- Multiple test case handling
- Array processing with utility functions
- Mathematical operations (GCD)
- Conditional output formatting
- Memory-efficient array copying
*/
