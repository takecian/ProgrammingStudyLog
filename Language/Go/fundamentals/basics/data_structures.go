package main

import "fmt"

// Data Structures Examples
func main() {
	fmt.Println("=== Go Data Structures ===")

	// Arrays
	demonstrateArrays()

	// Slices
	demonstrateSlices()

	// Maps
	demonstrateMaps()

	// Structs
	demonstrateStructs()

	// Pointers
	demonstratePointers()
}

func demonstrateArrays() {
	fmt.Println("\n--- Arrays ---")

	// Array declaration and initialization
	var numbers [5]int
	numbers[0] = 10
	numbers[1] = 20
	fmt.Printf("Array: %v\n", numbers)

	// Array literal
	fruits := [3]string{"apple", "banana", "orange"}
	fmt.Printf("Fruits: %v\n", fruits)

	// Array with inferred length
	colors := [...]string{"red", "green", "blue", "yellow"}
	fmt.Printf("Colors: %v (length: %d)\n", colors, len(colors))

	// Iterating over array
	fmt.Print("Array iteration: ")
	for i, fruit := range fruits {
		fmt.Printf("[%d]=%s ", i, fruit)
	}
	fmt.Println()
}

func demonstrateSlices() {
	fmt.Println("\n--- Slices ---")

	// Slice creation
	var numbers []int
	fmt.Printf("Empty slice: %v (len: %d, cap: %d)\n", numbers, len(numbers), cap(numbers))

	// Slice literal
	fruits := []string{"apple", "banana", "orange"}
	fmt.Printf("Fruits slice: %v\n", fruits)

	// Make function
	scores := make([]int, 3, 5) // length 3, capacity 5
	fmt.Printf("Made slice: %v (len: %d, cap: %d)\n", scores, len(scores), cap(scores))

	// Append to slice
	numbers = append(numbers, 1, 2, 3)
	fmt.Printf("After append: %v\n", numbers)

	// Slice operations
	fmt.Printf("Slice [1:3]: %v\n", fruits[1:3])
	fmt.Printf("Slice [:2]: %v\n", fruits[:2])
	fmt.Printf("Slice [1:]: %v\n", fruits[1:])

	// Copy slice
	copied := make([]string, len(fruits))
	copy(copied, fruits)
	fmt.Printf("Copied slice: %v\n", copied)

	// 2D slice
	matrix := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}
	fmt.Printf("2D slice: %v\n", matrix)
}

func demonstrateMaps() {
	fmt.Println("\n--- Maps ---")

	// Map creation
	var ages map[string]int
	ages = make(map[string]int)
	ages["Alice"] = 30
	ages["Bob"] = 25
	fmt.Printf("Ages map: %v\n", ages)

	// Map literal
	capitals := map[string]string{
		"Japan":  "Tokyo",
		"France": "Paris",
		"Italy":  "Rome",
	}
	fmt.Printf("Capitals: %v\n", capitals)

	// Map operations
	fmt.Printf("Japan's capital: %s\n", capitals["Japan"])

	// Check if key exists
	if capital, exists := capitals["Germany"]; exists {
		fmt.Printf("Germany's capital: %s\n", capital)
	} else {
		fmt.Println("Germany not found in map")
	}

	// Delete from map
	delete(capitals, "Italy")
	fmt.Printf("After deleting Italy: %v\n", capitals)

	// Iterate over map
	fmt.Println("Map iteration:")
	for country, capital := range capitals {
		fmt.Printf("  %s: %s\n", country, capital)
	}
}

// Person struct for demonstration
type Person struct {
	Name    string
	Age     int
	Email   string
	Address Address
}

type Address struct {
	Street string
	City   string
	Zip    string
}

func demonstrateStructs() {
	fmt.Println("\n--- Structs ---")

	// Struct creation
	var person1 Person
	person1.Name = "Alice"
	person1.Age = 30
	person1.Email = "alice@example.com"
	fmt.Printf("Person1: %+v\n", person1)

	// Struct literal
	person2 := Person{
		Name:  "Bob",
		Age:   25,
		Email: "bob@example.com",
		Address: Address{
			Street: "123 Main St",
			City:   "New York",
			Zip:    "10001",
		},
	}
	fmt.Printf("Person2: %+v\n", person2)

	// Struct with positional values
	person3 := Person{"Charlie", 35, "charlie@example.com", Address{}}
	fmt.Printf("Person3: %+v\n", person3)

	// Anonymous struct
	point := struct {
		X, Y int
	}{
		X: 10,
		Y: 20,
	}
	fmt.Printf("Point: %+v\n", point)

	// Struct methods (defined below)
	fmt.Printf("Person2 info: %s\n", person2.String())
	person2.HaveBirthday()
	fmt.Printf("After birthday: %s\n", person2.String())
}

// Method on Person struct
func (p Person) String() string {
	return fmt.Sprintf("%s (%d years old)", p.Name, p.Age)
}

// Method that modifies the struct (pointer receiver)
func (p *Person) HaveBirthday() {
	p.Age++
}

func demonstratePointers() {
	fmt.Println("\n--- Pointers ---")

	// Basic pointer usage
	x := 42
	p := &x // pointer to x
	fmt.Printf("x = %d, p = %p, *p = %d\n", x, p, *p)

	// Modify through pointer
	*p = 100
	fmt.Printf("After *p = 100: x = %d\n", x)

	// Pointer to struct
	person := Person{Name: "Alice", Age: 30}
	personPtr := &person
	fmt.Printf("Person: %+v\n", person)

	// Modify through pointer
	personPtr.Age = 31 // Go automatically dereferences
	fmt.Printf("After modification: %+v\n", person)

	// New function
	intPtr := new(int)
	*intPtr = 42
	fmt.Printf("New int pointer: %p, value: %d\n", intPtr, *intPtr)

	// Pointer comparison
	var ptr1, ptr2 *int
	fmt.Printf("nil pointers equal: %t\n", ptr1 == ptr2)

	a, b := 10, 10
	ptr1, ptr2 = &a, &b
	fmt.Printf("Different pointers to same value: %t\n", ptr1 == ptr2)
	fmt.Printf("Values equal: %t\n", *ptr1 == *ptr2)
}
