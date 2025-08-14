package main

import (
	"errors"
	"fmt"
	"strconv"
)

// Basic Error Handling Examples
func main() {
	fmt.Println("=== Go Error Handling ===")

	// Basic error handling
	demonstrateBasicErrors()

	// Creating custom errors
	demonstrateCustomErrors()

	// Error wrapping and unwrapping
	demonstrateErrorWrapping()

	// Multiple return values with errors
	demonstrateMultipleReturns()

	// Error handling patterns
	demonstrateErrorPatterns()
}

func demonstrateBasicErrors() {
	fmt.Println("\n--- Basic Error Handling ---")

	// Function that can return an error
	result, err := divide(10, 2)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
	} else {
		fmt.Printf("10 / 2 = %.2f\n", result)
	}

	// Error case
	result, err = divide(10, 0)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
	} else {
		fmt.Printf("10 / 0 = %.2f\n", result)
	}

	// Standard library function with error
	num, err := strconv.Atoi("123")
	if err != nil {
		fmt.Printf("Conversion error: %v\n", err)
	} else {
		fmt.Printf("Converted number: %d\n", num)
	}

	// Invalid conversion
	num, err = strconv.Atoi("abc")
	if err != nil {
		fmt.Printf("Conversion error: %v\n", err)
	} else {
		fmt.Printf("Converted number: %d\n", num)
	}
}

func divide(a, b float64) (float64, error) {
	if b == 0 {
		return 0, errors.New("division by zero")
	}
	return a / b, nil
}

// Custom error types
type ValidationError struct {
	Field   string
	Value   interface{}
	Message string
}

func (ve ValidationError) Error() string {
	return fmt.Sprintf("validation error for field '%s' with value '%v': %s",
		ve.Field, ve.Value, ve.Message)
}

type MathError struct {
	Operation string
	Operands  []float64
	Reason    string
}

func (me MathError) Error() string {
	return fmt.Sprintf("math error in %s operation with operands %v: %s",
		me.Operation, me.Operands, me.Reason)
}

func demonstrateCustomErrors() {
	fmt.Println("\n--- Custom Errors ---")

	// Validation error
	err := validateAge(-5)
	if err != nil {
		fmt.Printf("Validation failed: %v\n", err)

		// Type assertion to access custom error fields
		if ve, ok := err.(ValidationError); ok {
			fmt.Printf("  Field: %s\n", ve.Field)
			fmt.Printf("  Value: %v\n", ve.Value)
			fmt.Printf("  Message: %s\n", ve.Message)
		}
	}

	// Math error
	result, err := sqrt(-16)
	if err != nil {
		fmt.Printf("Math operation failed: %v\n", err)

		if me, ok := err.(MathError); ok {
			fmt.Printf("  Operation: %s\n", me.Operation)
			fmt.Printf("  Operands: %v\n", me.Operands)
		}
	} else {
		fmt.Printf("Square root result: %.2f\n", result)
	}

	// Successful case
	result, err = sqrt(16)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
	} else {
		fmt.Printf("Square root of 16: %.2f\n", result)
	}
}

func validateAge(age int) error {
	if age < 0 {
		return ValidationError{
			Field:   "age",
			Value:   age,
			Message: "age cannot be negative",
		}
	}
	if age > 150 {
		return ValidationError{
			Field:   "age",
			Value:   age,
			Message: "age seems unrealistic",
		}
	}
	return nil
}

func sqrt(x float64) (float64, error) {
	if x < 0 {
		return 0, MathError{
			Operation: "sqrt",
			Operands:  []float64{x},
			Reason:    "cannot calculate square root of negative number",
		}
	}

	// Simple Newton's method approximation
	if x == 0 {
		return 0, nil
	}

	guess := x / 2
	for i := 0; i < 10; i++ {
		guess = (guess + x/guess) / 2
	}

	return guess, nil
}

func demonstrateErrorWrapping() {
	fmt.Println("\n--- Error Wrapping ---")

	// Error wrapping with fmt.Errorf
	err := processFile("nonexistent.txt")
	if err != nil {
		fmt.Printf("Process failed: %v\n", err)

		// Unwrap to get the original error
		originalErr := errors.Unwrap(err)
		if originalErr != nil {
			fmt.Printf("Original error: %v\n", originalErr)
		}

		// Check if error is of specific type using errors.Is
		if errors.Is(err, ErrFileNotFound) {
			fmt.Println("This is a file not found error")
		}

		// Check if error wraps a specific type using errors.As
		var validationErr ValidationError
		if errors.As(err, &validationErr) {
			fmt.Printf("Contains validation error: %s\n", validationErr.Field)
		}
	}
}

var ErrFileNotFound = errors.New("file not found")

func processFile(filename string) error {
	// Simulate file reading
	err := readFile(filename)
	if err != nil {
		return fmt.Errorf("failed to process file %s: %w", filename, err)
	}
	return nil
}

func readFile(filename string) error {
	// Simulate file not found
	if filename == "nonexistent.txt" {
		return fmt.Errorf("cannot read file: %w", ErrFileNotFound)
	}
	return nil
}

func demonstrateMultipleReturns() {
	fmt.Println("\n--- Multiple Return Values ---")

	// Function with multiple return values and error
	name, age, err := parsePersonInfo("John,25")
	if err != nil {
		fmt.Printf("Parse error: %v\n", err)
	} else {
		fmt.Printf("Parsed: name=%s, age=%d\n", name, age)
	}

	// Invalid format
	name, age, err = parsePersonInfo("invalid")
	if err != nil {
		fmt.Printf("Parse error: %v\n", err)
	} else {
		fmt.Printf("Parsed: name=%s, age=%d\n", name, age)
	}

	// Function that can fail at multiple points
	result, err := complexCalculation(10, 5, 2)
	if err != nil {
		fmt.Printf("Calculation error: %v\n", err)
	} else {
		fmt.Printf("Calculation result: %.2f\n", result)
	}
}

func parsePersonInfo(info string) (string, int, error) {
	parts := make([]string, 0)
	current := ""

	// Simple split by comma
	for _, char := range info {
		if char == ',' {
			parts = append(parts, current)
			current = ""
		} else {
			current += string(char)
		}
	}
	if current != "" {
		parts = append(parts, current)
	}

	if len(parts) != 2 {
		return "", 0, ValidationError{
			Field:   "info",
			Value:   info,
			Message: "expected format: 'name,age'",
		}
	}

	name := parts[0]
	if name == "" {
		return "", 0, ValidationError{
			Field:   "name",
			Value:   name,
			Message: "name cannot be empty",
		}
	}

	age, err := strconv.Atoi(parts[1])
	if err != nil {
		return "", 0, fmt.Errorf("invalid age format: %w", err)
	}

	if err := validateAge(age); err != nil {
		return "", 0, fmt.Errorf("age validation failed: %w", err)
	}

	return name, age, nil
}

func complexCalculation(a, b, c float64) (float64, error) {
	// Step 1: Division
	step1, err := divide(a, b)
	if err != nil {
		return 0, fmt.Errorf("step 1 failed: %w", err)
	}

	// Step 2: Square root
	step2, err := sqrt(step1)
	if err != nil {
		return 0, fmt.Errorf("step 2 failed: %w", err)
	}

	// Step 3: Another division
	result, err := divide(step2, c)
	if err != nil {
		return 0, fmt.Errorf("step 3 failed: %w", err)
	}

	return result, nil
}

func demonstrateErrorPatterns() {
	fmt.Println("\n--- Error Handling Patterns ---")

	// Early return pattern
	fmt.Println("Early return pattern:")
	err := processData("valid_data")
	if err != nil {
		fmt.Printf("Process failed: %v\n", err)
	} else {
		fmt.Println("Process completed successfully")
	}

	// Error accumulation pattern
	fmt.Println("Error accumulation pattern:")
	errors := validateUser("", -5, "invalid-email")
	if len(errors) > 0 {
		fmt.Println("Validation errors:")
		for i, err := range errors {
			fmt.Printf("  %d: %v\n", i+1, err)
		}
	}

	// Retry pattern
	fmt.Println("Retry pattern:")
	result, err := retryOperation(3)
	if err != nil {
		fmt.Printf("Operation failed after retries: %v\n", err)
	} else {
		fmt.Printf("Operation succeeded: %s\n", result)
	}
}

func processData(data string) error {
	if data == "" {
		return errors.New("data cannot be empty")
	}

	if len(data) < 5 {
		return errors.New("data too short")
	}

	// More processing...
	return nil
}

func validateUser(name string, age int, email string) []error {
	var errors []error

	if name == "" {
		errors = append(errors, ValidationError{
			Field:   "name",
			Value:   name,
			Message: "name is required",
		})
	}

	if err := validateAge(age); err != nil {
		errors = append(errors, err)
	}

	if email == "" {
		errors = append(errors, ValidationError{
			Field:   "email",
			Value:   email,
			Message: "email is required",
		})
	} else if !isValidEmail(email) {
		errors = append(errors, ValidationError{
			Field:   "email",
			Value:   email,
			Message: "invalid email format",
		})
	}

	return errors
}

func isValidEmail(email string) bool {
	// Simple email validation
	return len(email) > 0 &&
		len(email) > 5 &&
		email[0] != '@' &&
		email[len(email)-1] != '@'
}

func retryOperation(maxRetries int) (string, error) {
	var lastErr error

	for i := 0; i < maxRetries; i++ {
		result, err := unreliableOperation(i)
		if err == nil {
			return result, nil
		}

		lastErr = err
		fmt.Printf("Attempt %d failed: %v\n", i+1, err)

		if i < maxRetries-1 {
			fmt.Printf("Retrying in 100ms...\n")
			// In real code, you might want to add actual delay
		}
	}

	return "", fmt.Errorf("operation failed after %d attempts: %w", maxRetries, lastErr)
}

func unreliableOperation(attempt int) (string, error) {
	// Simulate an operation that fails first few times
	if attempt < 2 {
		return "", errors.New("temporary failure")
	}
	return "success", nil
}
