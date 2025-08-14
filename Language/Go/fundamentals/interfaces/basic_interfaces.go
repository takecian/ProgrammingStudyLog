package main

import (
	"fmt"
	"math"
)

// Basic Interfaces Examples
func main() {
	fmt.Println("=== Go Interfaces ===")

	// Basic interface usage
	demonstrateBasicInterface()

	// Interface satisfaction
	demonstrateInterfaceSatisfaction()

	// Empty interface
	demonstrateEmptyInterface()

	// Type assertions
	demonstrateTypeAssertions()

	// Type switches
	demonstrateTypeSwitch()
}

// Shape interface defines behavior
type Shape interface {
	Area() float64
	Perimeter() float64
}

// Rectangle implements Shape
type Rectangle struct {
	Width, Height float64
}

func (r Rectangle) Area() float64 {
	return r.Width * r.Height
}

func (r Rectangle) Perimeter() float64 {
	return 2 * (r.Width + r.Height)
}

// Circle implements Shape
type Circle struct {
	Radius float64
}

func (c Circle) Area() float64 {
	return math.Pi * c.Radius * c.Radius
}

func (c Circle) Perimeter() float64 {
	return 2 * math.Pi * c.Radius
}

// Triangle implements Shape
type Triangle struct {
	Base, Height, Side1, Side2 float64
}

func (t Triangle) Area() float64 {
	return 0.5 * t.Base * t.Height
}

func (t Triangle) Perimeter() float64 {
	return t.Base + t.Side1 + t.Side2
}

func demonstrateBasicInterface() {
	fmt.Println("\n--- Basic Interface Usage ---")

	// Create different shapes
	rect := Rectangle{Width: 5, Height: 3}
	circle := Circle{Radius: 4}
	triangle := Triangle{Base: 6, Height: 4, Side1: 5, Side2: 5}

	// Store in slice of Shape interface
	shapes := []Shape{rect, circle, triangle}

	// Process all shapes uniformly
	for i, shape := range shapes {
		fmt.Printf("Shape %d:\n", i+1)
		fmt.Printf("  Area: %.2f\n", shape.Area())
		fmt.Printf("  Perimeter: %.2f\n", shape.Perimeter())
		fmt.Printf("  Type: %T\n", shape)
	}

	// Function that accepts interface
	printShapeInfo(rect)
	printShapeInfo(circle)
}

func printShapeInfo(s Shape) {
	fmt.Printf("Shape info - Area: %.2f, Perimeter: %.2f\n", s.Area(), s.Perimeter())
}

// Multiple interfaces
type Drawable interface {
	Draw()
}

type Movable interface {
	Move(x, y float64)
}

// Combined interface
type GameObject interface {
	Drawable
	Movable
	Shape // Embedding Shape interface
}

// Player implements all required methods
type Player struct {
	Name string
	X, Y float64
	Size float64
}

func (p *Player) Draw() {
	fmt.Printf("Drawing player %s at (%.1f, %.1f)\n", p.Name, p.X, p.Y)
}

func (p *Player) Move(x, y float64) {
	p.X += x
	p.Y += y
	fmt.Printf("Player %s moved to (%.1f, %.1f)\n", p.Name, p.X, p.Y)
}

func (p Player) Area() float64 {
	return p.Size * p.Size
}

func (p Player) Perimeter() float64 {
	return 4 * p.Size
}

func demonstrateInterfaceSatisfaction() {
	fmt.Println("\n--- Interface Satisfaction ---")

	player := &Player{Name: "Hero", X: 0, Y: 0, Size: 2}

	// Player satisfies GameObject interface
	var gameObj GameObject = player
	gameObj.Draw()
	gameObj.Move(5, 3)
	fmt.Printf("Game object area: %.2f\n", gameObj.Area())

	// Player also satisfies individual interfaces
	var drawable Drawable = player
	var movable Movable = player
	var shape Shape = player

	drawable.Draw()
	movable.Move(-2, 1)
	fmt.Printf("Shape area: %.2f\n", shape.Area())
}

func demonstrateEmptyInterface() {
	fmt.Println("\n--- Empty Interface ---")

	// interface{} can hold any value
	var anything interface{}

	anything = 42
	fmt.Printf("anything = %v (type: %T)\n", anything, anything)

	anything = "hello"
	fmt.Printf("anything = %v (type: %T)\n", anything, anything)

	anything = []int{1, 2, 3}
	fmt.Printf("anything = %v (type: %T)\n", anything, anything)

	anything = Rectangle{Width: 5, Height: 3}
	fmt.Printf("anything = %v (type: %T)\n", anything, anything)

	// Slice of empty interfaces
	mixed := []interface{}{
		42,
		"hello",
		true,
		Rectangle{Width: 2, Height: 3},
		Circle{Radius: 1.5},
	}

	fmt.Println("Mixed slice:")
	for i, item := range mixed {
		fmt.Printf("  [%d]: %v (type: %T)\n", i, item, item)
	}
}

func demonstrateTypeAssertions() {
	fmt.Println("\n--- Type Assertions ---")

	var shape Shape = Circle{Radius: 5}

	// Type assertion with ok idiom
	if circle, ok := shape.(Circle); ok {
		fmt.Printf("It's a circle with radius: %.2f\n", circle.Radius)
	} else {
		fmt.Println("Not a circle")
	}

	// Type assertion without ok (can panic)
	circle := shape.(Circle)
	fmt.Printf("Circle radius: %.2f\n", circle.Radius)

	// This would panic if uncommented:
	// rect := shape.(Rectangle) // panic: interface conversion

	// Safe type assertion
	if rect, ok := shape.(Rectangle); ok {
		fmt.Printf("Rectangle: %v\n", rect)
	} else {
		fmt.Println("Shape is not a rectangle")
	}

	// Type assertion with empty interface
	var anything interface{} = "hello world"

	if str, ok := anything.(string); ok {
		fmt.Printf("String value: %s (length: %d)\n", str, len(str))
	}

	if num, ok := anything.(int); ok {
		fmt.Printf("Integer value: %d\n", num)
	} else {
		fmt.Println("Not an integer")
	}
}

func demonstrateTypeSwitch() {
	fmt.Println("\n--- Type Switch ---")

	values := []interface{}{
		42,
		"hello",
		true,
		3.14,
		Rectangle{Width: 4, Height: 2},
		Circle{Radius: 3},
		[]int{1, 2, 3},
		nil,
	}

	for i, value := range values {
		fmt.Printf("Value %d: ", i)

		switch v := value.(type) {
		case nil:
			fmt.Println("nil value")
		case int:
			fmt.Printf("integer: %d\n", v)
		case string:
			fmt.Printf("string: %s (length: %d)\n", v, len(v))
		case bool:
			fmt.Printf("boolean: %t\n", v)
		case float64:
			fmt.Printf("float: %.2f\n", v)
		case Rectangle:
			fmt.Printf("rectangle: %.2f x %.2f (area: %.2f)\n", v.Width, v.Height, v.Area())
		case Circle:
			fmt.Printf("circle: radius %.2f (area: %.2f)\n", v.Radius, v.Area())
		case []int:
			fmt.Printf("int slice: %v (length: %d)\n", v, len(v))
		default:
			fmt.Printf("unknown type: %T\n", v)
		}
	}

	// Type switch with interface
	shapes := []Shape{
		Rectangle{Width: 3, Height: 4},
		Circle{Radius: 2.5},
		Triangle{Base: 6, Height: 4, Side1: 5, Side2: 5},
	}

	fmt.Println("\nShape type switch:")
	for _, shape := range shapes {
		switch s := shape.(type) {
		case Rectangle:
			fmt.Printf("Rectangle: %.1f x %.1f\n", s.Width, s.Height)
		case Circle:
			fmt.Printf("Circle: radius %.1f\n", s.Radius)
		case Triangle:
			fmt.Printf("Triangle: base %.1f, height %.1f\n", s.Base, s.Height)
		default:
			fmt.Printf("Unknown shape: %T\n", s)
		}
	}
}
