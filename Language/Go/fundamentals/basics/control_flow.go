package main

import "fmt"

// Control Flow Examples
func main() {
	fmt.Println("=== Go Control Flow ===")

	// If statements
	demonstrateIf()

	// Switch statements
	demonstrateSwitch()

	// For loops
	demonstrateLoops()

	// Range loops
	demonstrateRange()

	// Defer, panic, recover
	demonstrateDefer()
}

func demonstrateIf() {
	fmt.Println("\n--- If Statements ---")

	x := 10

	// Basic if
	if x > 5 {
		fmt.Printf("%d is greater than 5\n", x)
	}

	// If with else
	if x%2 == 0 {
		fmt.Printf("%d is even\n", x)
	} else {
		fmt.Printf("%d is odd\n", x)
	}

	// If with initialization
	if y := x * 2; y > 15 {
		fmt.Printf("y = %d is greater than 15\n", y)
	}

	// Multiple conditions
	age := 25
	if age >= 18 && age < 65 {
		fmt.Println("Working age")
	} else if age < 18 {
		fmt.Println("Minor")
	} else {
		fmt.Println("Senior")
	}
}

func demonstrateSwitch() {
	fmt.Println("\n--- Switch Statements ---")

	// Basic switch
	day := 3
	switch day {
	case 1:
		fmt.Println("Monday")
	case 2:
		fmt.Println("Tuesday")
	case 3:
		fmt.Println("Wednesday")
	case 4:
		fmt.Println("Thursday")
	case 5:
		fmt.Println("Friday")
	default:
		fmt.Println("Weekend")
	}

	// Switch with multiple values
	grade := 'B'
	switch grade {
	case 'A', 'a':
		fmt.Println("Excellent")
	case 'B', 'b':
		fmt.Println("Good")
	case 'C', 'c':
		fmt.Println("Average")
	default:
		fmt.Println("Below average")
	}

	// Switch with expressions
	score := 85
	switch {
	case score >= 90:
		fmt.Println("Grade: A")
	case score >= 80:
		fmt.Println("Grade: B")
	case score >= 70:
		fmt.Println("Grade: C")
	default:
		fmt.Println("Grade: F")
	}

	// Type switch
	var value interface{} = "hello"
	switch v := value.(type) {
	case string:
		fmt.Printf("String: %s\n", v)
	case int:
		fmt.Printf("Integer: %d\n", v)
	case bool:
		fmt.Printf("Boolean: %t\n", v)
	default:
		fmt.Printf("Unknown type: %T\n", v)
	}
}

func demonstrateLoops() {
	fmt.Println("\n--- For Loops ---")

	// Basic for loop
	fmt.Print("Basic for: ")
	for i := 0; i < 5; i++ {
		fmt.Printf("%d ", i)
	}
	fmt.Println()

	// While-style loop
	fmt.Print("While-style: ")
	j := 0
	for j < 5 {
		fmt.Printf("%d ", j)
		j++
	}
	fmt.Println()

	// Infinite loop with break
	fmt.Print("With break: ")
	k := 0
	for {
		if k >= 5 {
			break
		}
		fmt.Printf("%d ", k)
		k++
	}
	fmt.Println()

	// Continue example
	fmt.Print("With continue (even numbers): ")
	for i := 0; i < 10; i++ {
		if i%2 != 0 {
			continue
		}
		fmt.Printf("%d ", i)
	}
	fmt.Println()
}

func demonstrateRange() {
	fmt.Println("\n--- Range Loops ---")

	// Range over slice
	numbers := []int{10, 20, 30, 40, 50}
	fmt.Print("Slice values: ")
	for _, value := range numbers {
		fmt.Printf("%d ", value)
	}
	fmt.Println()

	fmt.Print("Slice with index: ")
	for index, value := range numbers {
		fmt.Printf("[%d]=%d ", index, value)
	}
	fmt.Println()

	// Range over map
	colors := map[string]string{
		"red":   "#FF0000",
		"green": "#00FF00",
		"blue":  "#0000FF",
	}
	fmt.Println("Map iteration:")
	for key, value := range colors {
		fmt.Printf("  %s: %s\n", key, value)
	}

	// Range over string
	text := "Hello"
	fmt.Print("String characters: ")
	for i, char := range text {
		fmt.Printf("[%d]=%c ", i, char)
	}
	fmt.Println()
}

func demonstrateDefer() {
	fmt.Println("\n--- Defer, Panic, Recover ---")

	// Defer example
	fmt.Println("Defer example:")
	defer fmt.Println("This will be printed last")
	fmt.Println("This will be printed first")
	fmt.Println("This will be printed second")

	// Multiple defers (LIFO order)
	fmt.Println("Multiple defers:")
	for i := 0; i < 3; i++ {
		defer fmt.Printf("Defer %d\n", i)
	}
	fmt.Println("After defer loop")

	// Panic and recover example
	fmt.Println("Panic and recover example:")
	safeFunction()
	fmt.Println("Program continues after panic recovery")
}

func safeFunction() {
	defer func() {
		if r := recover(); r != nil {
			fmt.Printf("Recovered from panic: %v\n", r)
		}
	}()

	fmt.Println("About to panic...")
	panic("Something went wrong!")
	fmt.Println("This line will not be executed")
}
