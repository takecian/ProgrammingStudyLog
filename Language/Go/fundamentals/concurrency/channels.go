package main

import (
	"fmt"
	"time"
)

// Channels Examples
func main() {
	fmt.Println("=== Go Channels ===")

	// Basic channels
	demonstrateBasicChannels()

	// Buffered channels
	demonstrateBufferedChannels()

	// Channel directions
	demonstrateChannelDirections()

	// Select statement
	demonstrateSelect()

	// Channel closing
	demonstrateChannelClosing()

	// Range over channels
	demonstrateChannelRange()

	// Channel patterns
	demonstrateChannelPatterns()
}

func demonstrateBasicChannels() {
	fmt.Println("\n--- Basic Channels ---")

	// Create a channel
	messages := make(chan string)

	// Send a value to channel in a goroutine
	go func() {
		messages <- "Hello from goroutine!"
	}()

	// Receive value from channel
	msg := <-messages
	fmt.Printf("Received: %s\n", msg)

	// Synchronous communication example
	done := make(chan bool)

	go func() {
		fmt.Println("Working...")
		time.Sleep(100 * time.Millisecond)
		fmt.Println("Work done!")
		done <- true
	}()

	fmt.Println("Waiting for work to complete...")
	<-done // Block until we receive a value
	fmt.Println("All done!")
}

func demonstrateBufferedChannels() {
	fmt.Println("\n--- Buffered Channels ---")

	// Buffered channel can hold values without a receiver
	messages := make(chan string, 2)

	// Send values without blocking
	messages <- "First message"
	messages <- "Second message"

	fmt.Printf("Channel length: %d, capacity: %d\n", len(messages), cap(messages))

	// Receive values
	fmt.Printf("Received: %s\n", <-messages)
	fmt.Printf("Received: %s\n", <-messages)

	// Demonstrate blocking behavior
	numbers := make(chan int, 3)

	go func() {
		for i := 1; i <= 5; i++ {
			fmt.Printf("Sending %d\n", i)
			numbers <- i
			if i > 3 {
				fmt.Printf("Blocked after sending %d\n", i)
			}
		}
		close(numbers)
	}()

	time.Sleep(50 * time.Millisecond)
	fmt.Println("Starting to receive...")

	for num := range numbers {
		fmt.Printf("Received %d\n", num)
		time.Sleep(20 * time.Millisecond)
	}
}

func demonstrateChannelDirections() {
	fmt.Println("\n--- Channel Directions ---")

	messages := make(chan string, 1)

	// Use channels with specific directions
	go sender(messages)
	receiver(messages)
}

// Send-only channel parameter
func sender(ch chan<- string) {
	ch <- "Hello from sender!"
}

// Receive-only channel parameter
func receiver(ch <-chan string) {
	msg := <-ch
	fmt.Printf("Receiver got: %s\n", msg)
}

func demonstrateSelect() {
	fmt.Println("\n--- Select Statement ---")

	ch1 := make(chan string)
	ch2 := make(chan string)

	// Send to channels with different delays
	go func() {
		time.Sleep(100 * time.Millisecond)
		ch1 <- "Message from channel 1"
	}()

	go func() {
		time.Sleep(50 * time.Millisecond)
		ch2 <- "Message from channel 2"
	}()

	// Select waits for the first available channel
	for i := 0; i < 2; i++ {
		select {
		case msg1 := <-ch1:
			fmt.Printf("Received from ch1: %s\n", msg1)
		case msg2 := <-ch2:
			fmt.Printf("Received from ch2: %s\n", msg2)
		}
	}

	// Select with timeout
	fmt.Println("Select with timeout:")
	timeout := time.After(200 * time.Millisecond)

	select {
	case <-time.After(300 * time.Millisecond):
		fmt.Println("This won't be reached")
	case <-timeout:
		fmt.Println("Timeout reached!")
	}

	// Non-blocking select with default
	fmt.Println("Non-blocking select:")
	messages := make(chan string)

	select {
	case msg := <-messages:
		fmt.Printf("Received: %s\n", msg)
	default:
		fmt.Println("No message available")
	}
}

func demonstrateChannelClosing() {
	fmt.Println("\n--- Channel Closing ---")

	jobs := make(chan int, 5)
	done := make(chan bool)

	// Worker goroutine
	go func() {
		for {
			job, more := <-jobs
			if more {
				fmt.Printf("Processing job %d\n", job)
				time.Sleep(20 * time.Millisecond)
			} else {
				fmt.Println("All jobs processed")
				done <- true
				return
			}
		}
	}()

	// Send jobs
	for j := 1; j <= 3; j++ {
		jobs <- j
		fmt.Printf("Sent job %d\n", j)
	}

	close(jobs) // Close channel to signal no more values
	fmt.Println("Closed jobs channel")

	<-done // Wait for worker to finish
}

func demonstrateChannelRange() {
	fmt.Println("\n--- Range over Channels ---")

	queue := make(chan string, 2)
	queue <- "First"
	queue <- "Second"
	close(queue)

	// Range automatically receives until channel is closed
	fmt.Println("Range over closed channel:")
	for item := range queue {
		fmt.Printf("Item: %s\n", item)
	}

	// Range with producer goroutine
	fmt.Println("Range with producer:")
	numbers := make(chan int)

	go func() {
		for i := 1; i <= 5; i++ {
			numbers <- i
			time.Sleep(50 * time.Millisecond)
		}
		close(numbers)
	}()

	for num := range numbers {
		fmt.Printf("Number: %d\n", num)
	}
}

func demonstrateChannelPatterns() {
	fmt.Println("\n--- Channel Patterns ---")

	// Fan-out pattern
	fmt.Println("Fan-out pattern:")
	input := make(chan int)
	output1 := make(chan int)
	output2 := make(chan int)

	// Fan-out: one input to multiple outputs
	go func() {
		for val := range input {
			output1 <- val
			output2 <- val
		}
		close(output1)
		close(output2)
	}()

	// Send some values
	go func() {
		for i := 1; i <= 3; i++ {
			input <- i
		}
		close(input)
	}()

	// Receive from both outputs
	go func() {
		for val := range output1 {
			fmt.Printf("Output1: %d\n", val)
		}
	}()

	for val := range output2 {
		fmt.Printf("Output2: %d\n", val)
	}

	time.Sleep(100 * time.Millisecond)

	// Pipeline pattern
	fmt.Println("Pipeline pattern:")
	pipeline := createPipeline()

	// Send values through pipeline
	go func() {
		for i := 1; i <= 5; i++ {
			pipeline.input <- i
		}
		close(pipeline.input)
	}()

	// Receive processed values
	for result := range pipeline.output {
		fmt.Printf("Pipeline result: %d\n", result)
	}
}

type Pipeline struct {
	input  chan int
	output chan int
}

func createPipeline() Pipeline {
	input := make(chan int)
	middle := make(chan int)
	output := make(chan int)

	// Stage 1: multiply by 2
	go func() {
		for val := range input {
			middle <- val * 2
		}
		close(middle)
	}()

	// Stage 2: add 1
	go func() {
		for val := range middle {
			output <- val + 1
		}
		close(output)
	}()

	return Pipeline{input: input, output: output}
}
