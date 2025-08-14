package main

import "fmt"

// Functions Examples
func main() {
	fmt.Println("=== Go Functions ===")

	// Basic function call
	result := add(5, 3)
	fmt.Printf("add(5, 3) = %d\n", result)

	// Multiple return values
	sum, product := calculate(4, 6)
	fmt.Printf("calculate(4, 6) = sum: %d, product: %d\n", sum, product)

	// Named return values
	area, perimeter := rectangleStats(5, 3)
	fmt.Printf("Rectangle (5x3): area=%d, perimeter=%d\n", area, perimeter)

	// Variadic functions
	total := sum(1, 2, 3, 4, 5)
	fmt.Printf("sum(1, 2, 3, 4, 5) = %d\n", total)

	// Function as variable
	operation := multiply
	fmt.Printf("operation(7, 8) = %d\n", operation(7, 8))

	// Anonymous function
	square := func(x int) int {
		return x * x
	}
	fmt.Printf("square(9) = %d\n", square(9))

	// Closure example
	counter := makeCounter()
	fmt.Printf("Counter: %d\n", counter()) // 1
	fmt.Printf("Counter: %d\n", counter()) // 2
	fmt.Printf("Counter: %d\n", counter()) // 3

	// Higher-order function
	numbers := []int{1, 2, 3, 4, 5}
	doubled := mapInts(numbers, func(x int) int { return x * 2 })
	fmt.Printf("Original: %v, Doubled: %v\n", numbers, doubled)
}

// Basic function
func add(a, b int) int {
	return a + b
}

// Multiple return values
func calculate(a, b int) (int, int) {
	return a + b, a * b
}

// Named return values
func rectangleStats(length, width int) (area, perimeter int) {
	area = length * width
	perimeter = 2 * (length + width)
	return // naked return
}

// Variadic function
func sum(numbers ...int) int {
	total := 0
	for _, num := range numbers {
		total += num
	}
	return total
}

// Function for assignment
func multiply(a, b int) int {
	return a * b
}

// Closure example
func makeCounter() func() int {
	count := 0
	return func() int {
		count++
		return count
	}
}

// Higher-order function
func mapInts(slice []int, fn func(int) int) []int {
	result := make([]int, len(slice))
	for i, v := range slice {
		result[i] = fn(v)
	}
	return result
}
