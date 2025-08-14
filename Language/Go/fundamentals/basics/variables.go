package main

import "fmt"

// Variables and Types Examples
func main() {
	fmt.Println("=== Go Variables and Types ===")

	// Variable declarations
	var name string = "Go Programming"
	var age int = 15
	var isActive bool = true

	// Short variable declaration (type inference)
	language := "Go"
	version := 1.21

	// Multiple variable declarations
	var (
		x int = 10
		y int = 20
		z int = 30
	)

	// Multiple assignment
	a, b := 100, 200

	// Zero values
	var defaultInt int       // 0
	var defaultString string // ""
	var defaultBool bool     // false

	fmt.Printf("Name: %s, Age: %d, Active: %t\n", name, age, isActive)
	fmt.Printf("Language: %s, Version: %.2f\n", language, version)
	fmt.Printf("Coordinates: x=%d, y=%d, z=%d\n", x, y, z)
	fmt.Printf("Values: a=%d, b=%d\n", a, b)
	fmt.Printf("Zero values: int=%d, string='%s', bool=%t\n", defaultInt, defaultString, defaultBool)

	// Constants
	const pi = 3.14159
	const greeting = "Hello, World!"

	fmt.Printf("Pi: %.5f, Greeting: %s\n", pi, greeting)

	// Type conversion
	var intVal int = 42
	var floatVal float64 = float64(intVal)
	var stringVal string = fmt.Sprintf("%d", intVal)

	fmt.Printf("Conversions: int=%d, float=%.2f, string=%s\n", intVal, floatVal, stringVal)
}
