package main

import (
	"fmt"
	"io"
	"strings"
)

// Interface Patterns and Best Practices
func main() {
	fmt.Println("=== Interface Patterns ===")

	// Strategy pattern
	demonstrateStrategyPattern()

	// Adapter pattern
	demonstrateAdapterPattern()

	// Decorator pattern
	demonstrateDecoratorPattern()

	// Interface composition
	demonstrateInterfaceComposition()

	// Standard library interfaces
	demonstrateStandardInterfaces()
}

// Strategy Pattern
type SortStrategy interface {
	Sort([]int) []int
}

type BubbleSort struct{}

func (bs BubbleSort) Sort(data []int) []int {
	result := make([]int, len(data))
	copy(result, data)

	n := len(result)
	for i := 0; i < n-1; i++ {
		for j := 0; j < n-i-1; j++ {
			if result[j] > result[j+1] {
				result[j], result[j+1] = result[j+1], result[j]
			}
		}
	}
	return result
}

type QuickSort struct{}

func (qs QuickSort) Sort(data []int) []int {
	result := make([]int, len(data))
	copy(result, data)
	quickSort(result, 0, len(result)-1)
	return result
}

func quickSort(arr []int, low, high int) {
	if low < high {
		pi := partition(arr, low, high)
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)
	}
}

func partition(arr []int, low, high int) int {
	pivot := arr[high]
	i := low - 1

	for j := low; j < high; j++ {
		if arr[j] < pivot {
			i++
			arr[i], arr[j] = arr[j], arr[i]
		}
	}
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i + 1
}

type Sorter struct {
	strategy SortStrategy
}

func (s *Sorter) SetStrategy(strategy SortStrategy) {
	s.strategy = strategy
}

func (s *Sorter) Sort(data []int) []int {
	return s.strategy.Sort(data)
}

func demonstrateStrategyPattern() {
	fmt.Println("\n--- Strategy Pattern ---")

	data := []int{64, 34, 25, 12, 22, 11, 90}
	fmt.Printf("Original data: %v\n", data)

	sorter := &Sorter{}

	// Use bubble sort strategy
	sorter.SetStrategy(BubbleSort{})
	result1 := sorter.Sort(data)
	fmt.Printf("Bubble sort result: %v\n", result1)

	// Use quick sort strategy
	sorter.SetStrategy(QuickSort{})
	result2 := sorter.Sort(data)
	fmt.Printf("Quick sort result: %v\n", result2)
}

// Adapter Pattern
type LegacyPrinter struct{}

func (lp LegacyPrinter) OldPrint(text string) {
	fmt.Printf("[LEGACY] %s\n", text)
}

type ModernPrinter interface {
	Print(text string)
}

type PrinterAdapter struct {
	legacyPrinter LegacyPrinter
}

func (pa PrinterAdapter) Print(text string) {
	pa.legacyPrinter.OldPrint(text)
}

type StandardPrinter struct{}

func (sp StandardPrinter) Print(text string) {
	fmt.Printf("[MODERN] %s\n", text)
}

func demonstrateAdapterPattern() {
	fmt.Println("\n--- Adapter Pattern ---")

	// Modern printer
	var printer ModernPrinter = StandardPrinter{}
	printer.Print("Hello from modern printer")

	// Legacy printer through adapter
	adapter := PrinterAdapter{legacyPrinter: LegacyPrinter{}}
	printer = adapter
	printer.Print("Hello from legacy printer via adapter")

	// Use both in same context
	printers := []ModernPrinter{
		StandardPrinter{},
		PrinterAdapter{legacyPrinter: LegacyPrinter{}},
	}

	for i, p := range printers {
		p.Print(fmt.Sprintf("Message %d", i+1))
	}
}

// Decorator Pattern
type Coffee interface {
	Cost() float64
	Description() string
}

type SimpleCoffee struct{}

func (sc SimpleCoffee) Cost() float64 {
	return 2.0
}

func (sc SimpleCoffee) Description() string {
	return "Simple coffee"
}

type MilkDecorator struct {
	coffee Coffee
}

func (md MilkDecorator) Cost() float64 {
	return md.coffee.Cost() + 0.5
}

func (md MilkDecorator) Description() string {
	return md.coffee.Description() + ", milk"
}

type SugarDecorator struct {
	coffee Coffee
}

func (sd SugarDecorator) Cost() float64 {
	return sd.coffee.Cost() + 0.2
}

func (sd SugarDecorator) Description() string {
	return sd.coffee.Description() + ", sugar"
}

type WhipDecorator struct {
	coffee Coffee
}

func (wd WhipDecorator) Cost() float64 {
	return wd.coffee.Cost() + 0.7
}

func (wd WhipDecorator) Description() string {
	return wd.coffee.Description() + ", whip"
}

func demonstrateDecoratorPattern() {
	fmt.Println("\n--- Decorator Pattern ---")

	// Simple coffee
	coffee := SimpleCoffee{}
	fmt.Printf("%s: $%.2f\n", coffee.Description(), coffee.Cost())

	// Coffee with milk
	coffeeWithMilk := MilkDecorator{coffee: coffee}
	fmt.Printf("%s: $%.2f\n", coffeeWithMilk.Description(), coffeeWithMilk.Cost())

	// Coffee with milk and sugar
	coffeeWithMilkAndSugar := SugarDecorator{coffee: coffeeWithMilk}
	fmt.Printf("%s: $%.2f\n", coffeeWithMilkAndSugar.Description(), coffeeWithMilkAndSugar.Cost())

	// Fully loaded coffee
	fullyLoaded := WhipDecorator{
		coffee: SugarDecorator{
			coffee: MilkDecorator{
				coffee: SimpleCoffee{},
			},
		},
	}
	fmt.Printf("%s: $%.2f\n", fullyLoaded.Description(), fullyLoaded.Cost())
}

// Interface Composition
type Reader interface {
	Read() string
}

type Writer interface {
	Write(data string)
}

type ReadWriter interface {
	Reader
	Writer
}

type Closer interface {
	Close() error
}

type ReadWriteCloser interface {
	ReadWriter
	Closer
}

type FileHandler struct {
	filename string
	data     string
	closed   bool
}

func (fh *FileHandler) Read() string {
	if fh.closed {
		return ""
	}
	return fh.data
}

func (fh *FileHandler) Write(data string) {
	if !fh.closed {
		fh.data += data
	}
}

func (fh *FileHandler) Close() error {
	fh.closed = true
	fmt.Printf("File %s closed\n", fh.filename)
	return nil
}

func demonstrateInterfaceComposition() {
	fmt.Println("\n--- Interface Composition ---")

	file := &FileHandler{filename: "test.txt", data: "Initial content\n"}

	// Use as Reader
	var reader Reader = file
	fmt.Printf("Read: %s", reader.Read())

	// Use as Writer
	var writer Writer = file
	writer.Write("Added content\n")

	// Use as ReadWriter
	var rw ReadWriter = file
	rw.Write("More content\n")
	fmt.Printf("Read after write: %s", rw.Read())

	// Use as ReadWriteCloser
	var rwc ReadWriteCloser = file
	rwc.Write("Final content\n")
	fmt.Printf("Final read: %s", rwc.Read())
	rwc.Close()

	// After closing
	fmt.Printf("Read after close: '%s'\n", rwc.Read())
}

func demonstrateStandardInterfaces() {
	fmt.Println("\n--- Standard Library Interfaces ---")

	// io.Reader and io.Writer
	text := "Hello, Go interfaces!"
	reader := strings.NewReader(text)

	// Read from string reader
	buffer := make([]byte, 5)
	for {
		n, err := reader.Read(buffer)
		if err == io.EOF {
			break
		}
		fmt.Printf("Read %d bytes: %s\n", n, string(buffer[:n]))
	}

	// io.Writer example
	var builder strings.Builder
	fmt.Fprintf(&builder, "Built string: %s %d", "number", 42)
	fmt.Printf("Builder result: %s\n", builder.String())

	// Stringer interface
	point := Point{X: 3, Y: 4}
	fmt.Printf("Point: %s\n", point) // Uses String() method

	// Error interface
	err := &CustomError{Message: "Something went wrong", Code: 500}
	fmt.Printf("Error: %s\n", err)

	// Demonstrate interface nil vs nil value
	demonstrateInterfaceNil()
}

type Point struct {
	X, Y int
}

func (p Point) String() string {
	return fmt.Sprintf("Point(%d, %d)", p.X, p.Y)
}

type CustomError struct {
	Message string
	Code    int
}

func (ce *CustomError) Error() string {
	return fmt.Sprintf("Error %d: %s", ce.Code, ce.Message)
}

func demonstrateInterfaceNil() {
	fmt.Println("\n--- Interface Nil Gotcha ---")

	var err error
	fmt.Printf("err == nil: %t\n", err == nil)

	var customErr *CustomError
	err = customErr
	fmt.Printf("err == nil after assignment: %t\n", err == nil)
	fmt.Printf("err is nil interface: %t\n", err == (*CustomError)(nil))

	// Proper nil check
	if err != nil {
		fmt.Printf("Error (but pointer is nil): %v\n", err)
	}

	// Better pattern
	if customErr != nil {
		fmt.Printf("Custom error: %s\n", customErr.Error())
	} else {
		fmt.Println("No custom error")
	}
}
