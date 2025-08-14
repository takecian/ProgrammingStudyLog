package main

import (
	"fmt"
	"runtime"
	"sync"
	"time"
)

// Goroutines Examples
func main() {
	fmt.Println("=== Go Goroutines ===")

	// Basic goroutine
	demonstrateBasicGoroutine()

	// Multiple goroutines
	demonstrateMultipleGoroutines()

	// Goroutines with WaitGroup
	demonstrateWaitGroup()

	// Goroutines with shared data (race condition)
	demonstrateRaceCondition()

	// Goroutines with mutex
	demonstrateMutex()

	// Worker pool pattern
	demonstrateWorkerPool()
}

func demonstrateBasicGoroutine() {
	fmt.Println("\n--- Basic Goroutine ---")

	// Without goroutine (sequential)
	fmt.Println("Sequential execution:")
	sayHello("Alice")
	sayHello("Bob")

	// With goroutine (concurrent)
	fmt.Println("Concurrent execution:")
	go sayHello("Charlie")
	go sayHello("Diana")

	// Wait a bit to let goroutines finish
	time.Sleep(100 * time.Millisecond)
	fmt.Println("Main function continues...")
}

func sayHello(name string) {
	for i := 0; i < 3; i++ {
		fmt.Printf("Hello, %s! (%d)\n", name, i+1)
		time.Sleep(10 * time.Millisecond)
	}
}

func demonstrateMultipleGoroutines() {
	fmt.Println("\n--- Multiple Goroutines ---")

	fmt.Printf("Number of CPUs: %d\n", runtime.NumCPU())
	fmt.Printf("Number of goroutines before: %d\n", runtime.NumGoroutine())

	// Launch multiple goroutines
	for i := 0; i < 5; i++ {
		go func(id int) {
			fmt.Printf("Goroutine %d is running\n", id)
			time.Sleep(50 * time.Millisecond)
			fmt.Printf("Goroutine %d is done\n", id)
		}(i)
	}

	time.Sleep(10 * time.Millisecond)
	fmt.Printf("Number of goroutines after launch: %d\n", runtime.NumGoroutine())

	time.Sleep(100 * time.Millisecond)
	fmt.Printf("Number of goroutines after completion: %d\n", runtime.NumGoroutine())
}

func demonstrateWaitGroup() {
	fmt.Println("\n--- WaitGroup ---")

	var wg sync.WaitGroup

	// Add the number of goroutines to wait for
	wg.Add(3)

	go worker("Worker 1", &wg)
	go worker("Worker 2", &wg)
	go worker("Worker 3", &wg)

	fmt.Println("Waiting for workers to complete...")
	wg.Wait() // Block until all goroutines call Done()
	fmt.Println("All workers completed!")
}

func worker(name string, wg *sync.WaitGroup) {
	defer wg.Done() // Decrement counter when function returns

	fmt.Printf("%s starting work\n", name)
	time.Sleep(time.Duration(50+len(name)*10) * time.Millisecond)
	fmt.Printf("%s finished work\n", name)
}

func demonstrateRaceCondition() {
	fmt.Println("\n--- Race Condition (Unsafe) ---")

	var counter int
	var wg sync.WaitGroup

	// Launch multiple goroutines that increment counter
	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			counter++ // Race condition: multiple goroutines accessing shared variable
		}()
	}

	wg.Wait()
	fmt.Printf("Final counter value (should be 1000, but likely isn't): %d\n", counter)
}

func demonstrateMutex() {
	fmt.Println("\n--- Mutex (Safe) ---")

	var counter int
	var mu sync.Mutex
	var wg sync.WaitGroup

	// Launch multiple goroutines that safely increment counter
	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			mu.Lock()   // Acquire lock
			counter++   // Safe access to shared variable
			mu.Unlock() // Release lock
		}()
	}

	wg.Wait()
	fmt.Printf("Final counter value (should be 1000): %d\n", counter)
}

func demonstrateWorkerPool() {
	fmt.Println("\n--- Worker Pool Pattern ---")

	const numWorkers = 3
	const numJobs = 10

	jobs := make(chan int, numJobs)
	results := make(chan int, numJobs)

	// Start workers
	var wg sync.WaitGroup
	for w := 1; w <= numWorkers; w++ {
		wg.Add(1)
		go poolWorker(w, jobs, results, &wg)
	}

	// Send jobs
	for j := 1; j <= numJobs; j++ {
		jobs <- j
	}
	close(jobs)

	// Wait for workers to finish
	go func() {
		wg.Wait()
		close(results)
	}()

	// Collect results
	fmt.Println("Results:")
	for result := range results {
		fmt.Printf("Job result: %d\n", result)
	}
}

func poolWorker(id int, jobs <-chan int, results chan<- int, wg *sync.WaitGroup) {
	defer wg.Done()

	for job := range jobs {
		fmt.Printf("Worker %d processing job %d\n", id, job)
		time.Sleep(100 * time.Millisecond) // Simulate work
		results <- job * 2                 // Send result
	}
	fmt.Printf("Worker %d finished\n", id)
}
