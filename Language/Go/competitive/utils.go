package main

import (
	"sort"
	"strconv"
	"strings"
)

// Math utility functions

// Min returns the minimum of two integers
func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// Max returns the maximum of two integers
func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// MinInt64 returns the minimum of two int64s
func MinInt64(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

// MaxInt64 returns the maximum of two int64s
func MaxInt64(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

// Abs returns the absolute value of an integer
func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// AbsInt64 returns the absolute value of an int64
func AbsInt64(x int64) int64 {
	if x < 0 {
		return -x
	}
	return x
}

// GCD returns the greatest common divisor of two integers
func GCD(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

// LCM returns the least common multiple of two integers
func LCM(a, b int) int {
	return a / GCD(a, b) * b
}

// Pow returns base^exp using fast exponentiation
func Pow(base, exp int) int {
	result := 1
	for exp > 0 {
		if exp%2 == 1 {
			result *= base
		}
		base *= base
		exp /= 2
	}
	return result
}

// PowMod returns (base^exp) % mod using fast exponentiation
func PowMod(base, exp, mod int) int {
	result := 1
	base %= mod
	for exp > 0 {
		if exp%2 == 1 {
			result = (result * base) % mod
		}
		base = (base * base) % mod
		exp /= 2
	}
	return result
}

// Array/Slice utility functions

// ReverseInts reverses an integer slice in place
func ReverseInts(arr []int) {
	for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
		arr[i], arr[j] = arr[j], arr[i]
	}
}

// ReverseStrings reverses a string slice in place
func ReverseStrings(arr []string) {
	for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
		arr[i], arr[j] = arr[j], arr[i]
	}
}

// SumInts returns the sum of all integers in a slice
func SumInts(arr []int) int {
	sum := 0
	for _, v := range arr {
		sum += v
	}
	return sum
}

// SumInt64s returns the sum of all int64s in a slice
func SumInt64s(arr []int64) int64 {
	var sum int64
	for _, v := range arr {
		sum += v
	}
	return sum
}

// MaxInSlice returns the maximum value in an integer slice
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

// MinInSlice returns the minimum value in an integer slice
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

// UniqueInts returns unique integers from a slice (preserves order)
func UniqueInts(arr []int) []int {
	seen := make(map[int]bool)
	result := make([]int, 0)
	for _, v := range arr {
		if !seen[v] {
			seen[v] = true
			result = append(result, v)
		}
	}
	return result
}

// String utility functions

// ReverseString reverses a string
func ReverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

// IsPalindrome checks if a string is a palindrome
func IsPalindrome(s string) bool {
	runes := []rune(strings.ToLower(s))
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		if runes[i] != runes[j] {
			return false
		}
	}
	return true
}

// Parsing utility functions

// ParseInts parses a space-separated string of integers
func ParseInts(s string) []int {
	parts := strings.Fields(s)
	result := make([]int, len(parts))
	for i, part := range parts {
		n, err := strconv.Atoi(part)
		if err != nil {
			panic(err)
		}
		result[i] = n
	}
	return result
}

// JoinInts joins integers with a separator
func JoinInts(arr []int, sep string) string {
	strs := make([]string, len(arr))
	for i, v := range arr {
		strs[i] = strconv.Itoa(v)
	}
	return strings.Join(strs, sep)
}

// Search utility functions

// BinarySearch performs binary search on a sorted slice
// Returns the index if found, -1 if not found
func BinarySearch(arr []int, target int) int {
	left, right := 0, len(arr)-1
	for left <= right {
		mid := left + (right-left)/2
		if arr[mid] == target {
			return mid
		} else if arr[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return -1
}

// LowerBound returns the first index where arr[i] >= target
func LowerBound(arr []int, target int) int {
	return sort.Search(len(arr), func(i int) bool {
		return arr[i] >= target
	})
}

// UpperBound returns the first index where arr[i] > target
func UpperBound(arr []int, target int) int {
	return sort.Search(len(arr), func(i int) bool {
		return arr[i] > target
	})
}

// Combinatorics utility functions

// Factorial returns n! (be careful with large numbers)
func Factorial(n int) int {
	if n <= 1 {
		return 1
	}
	result := 1
	for i := 2; i <= n; i++ {
		result *= i
	}
	return result
}

// Combination returns C(n, r) = n! / (r! * (n-r)!)
func Combination(n, r int) int {
	if r > n || r < 0 {
		return 0
	}
	if r == 0 || r == n {
		return 1
	}
	if r > n-r {
		r = n - r // Take advantage of symmetry
	}

	result := 1
	for i := 0; i < r; i++ {
		result = result * (n - i) / (i + 1)
	}
	return result
}

// Permutation returns P(n, r) = n! / (n-r)!
func Permutation(n, r int) int {
	if r > n || r < 0 {
		return 0
	}
	result := 1
	for i := 0; i < r; i++ {
		result *= (n - i)
	}
	return result
}

// Grid/2D array utility functions

// Directions for 4-directional movement (up, right, down, left)
var Directions4 = [][2]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}

// Directions for 8-directional movement (including diagonals)
var Directions8 = [][2]int{{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}}

// IsValidPosition checks if a position is within grid bounds
func IsValidPosition(row, col, rows, cols int) bool {
	return row >= 0 && row < rows && col >= 0 && col < cols
}

// Make2DIntSlice creates a 2D integer slice with given dimensions
func Make2DIntSlice(rows, cols int) [][]int {
	result := make([][]int, rows)
	for i := range result {
		result[i] = make([]int, cols)
	}
	return result
}

// Make2DBoolSlice creates a 2D boolean slice with given dimensions
func Make2DBoolSlice(rows, cols int) [][]bool {
	result := make([][]bool, rows)
	for i := range result {
		result[i] = make([]bool, cols)
	}
	return result
}
