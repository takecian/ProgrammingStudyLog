package main

import (
	"context"
	"fmt"
	"math/rand"
	"sync"
	"time"
)

// Advanced Concurrency Patterns
func main() {
	fmt.Println("=== Advanced Concurrency Patterns ===")

	// Context for cancellation
	demonstrateContext()

	// Rate limiting
	demonstrateRateLimiting()

	// Producer-Consumer
	demonstrateProducerConsumer()

	// Publish-Subscribe
	demonstratePubSub()

	// Semaphore pattern
	demonstrateSemaphore()
}

func demonstrateContext() {
	fmt.Println("\n--- Context for Cancellation ---")

	// Context with timeout
	ctx, cancel := context.WithTimeout(context.Background(), 200*time.Millisecond)
	defer cancel()

	done := make(chan bool)

	go func() {
		select {
		case <-time.After(300 * time.Millisecond):
			fmt.Println("Work completed")
			done <- true
		case <-ctx.Done():
			fmt.Printf("Work cancelled: %v\n", ctx.Err())
			done <- true
		}
	}()

	<-done

	// Context with manual cancellation
	fmt.Println("Manual cancellation:")
	ctx2, cancel2 := context.WithCancel(context.Background())

	go func() {
		for i := 1; i <= 10; i++ {
			select {
			case <-ctx2.Done():
				fmt.Printf("Worker stopped at iteration %d: %v\n", i, ctx2.Err())
				return
			default:
				fmt.Printf("Working... %d\n", i)
				time.Sleep(50 * time.Millisecond)
			}
		}
	}()

	time.Sleep(150 * time.Millisecond)
	cancel2() // Cancel the work
	time.Sleep(100 * time.Millisecond)
}

func demonstrateRateLimiting() {
	fmt.Println("\n--- Rate Limiting ---")

	// Simple rate limiter using ticker
	requests := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		requests <- i
	}
	close(requests)

	limiter := time.Tick(200 * time.Millisecond)

	fmt.Println("Processing requests with rate limiting:")
	for req := range requests {
		<-limiter // Wait for rate limiter
		fmt.Printf("Processing request %d at %s\n", req, time.Now().Format("15:04:05.000"))
	}

	// Bursty rate limiter
	fmt.Println("Bursty rate limiter:")
	burstLimiter := make(chan time.Time, 3)

	// Fill up the bucket
	for i := 0; i < 3; i++ {
		burstLimiter <- time.Now()
	}

	// Refill bucket every 200ms
	go func() {
		for t := range time.Tick(200 * time.Millisecond) {
			select {
			case burstLimiter <- t:
			default:
			}
		}
	}()

	burstyRequests := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		burstyRequests <- i
	}
	close(burstyRequests)

	for req := range burstyRequests {
		<-burstLimiter
		fmt.Printf("Bursty request %d at %s\n", req, time.Now().Format("15:04:05.000"))
	}
}

func demonstrateProducerConsumer() {
	fmt.Println("\n--- Producer-Consumer Pattern ---")

	buffer := make(chan int, 3) // Bounded buffer
	var wg sync.WaitGroup

	// Producer
	wg.Add(1)
	go func() {
		defer wg.Done()
		defer close(buffer)

		for i := 1; i <= 10; i++ {
			fmt.Printf("Producing %d\n", i)
			buffer <- i
			time.Sleep(50 * time.Millisecond)
		}
		fmt.Println("Producer finished")
	}()

	// Multiple consumers
	for c := 1; c <= 2; c++ {
		wg.Add(1)
		go func(consumerID int) {
			defer wg.Done()

			for item := range buffer {
				fmt.Printf("Consumer %d consuming %d\n", consumerID, item)
				time.Sleep(time.Duration(rand.Intn(100)+50) * time.Millisecond)
			}
			fmt.Printf("Consumer %d finished\n", consumerID)
		}(c)
	}

	wg.Wait()
}

func demonstratePubSub() {
	fmt.Println("\n--- Publish-Subscribe Pattern ---")

	broker := NewBroker()
	broker.Start()
	defer broker.Stop()

	// Create subscribers
	sub1 := broker.Subscribe("news")
	sub2 := broker.Subscribe("news")
	sub3 := broker.Subscribe("sports")

	// Publisher goroutine
	go func() {
		messages := []Message{
			{"news", "Breaking: Go 1.22 released!"},
			{"sports", "World Cup final tonight"},
			{"news", "New programming language announced"},
			{"sports", "Olympic games begin"},
		}

		for _, msg := range messages {
			broker.Publish(msg)
			time.Sleep(100 * time.Millisecond)
		}
	}()

	// Subscriber goroutines
	go func() {
		for msg := range sub1 {
			fmt.Printf("Subscriber 1 received: %s\n", msg.Content)
		}
	}()

	go func() {
		for msg := range sub2 {
			fmt.Printf("Subscriber 2 received: %s\n", msg.Content)
		}
	}()

	go func() {
		for msg := range sub3 {
			fmt.Printf("Sports subscriber received: %s\n", msg.Content)
		}
	}()

	time.Sleep(500 * time.Millisecond)

	// Unsubscribe
	broker.Unsubscribe("news", sub1)
	broker.Unsubscribe("news", sub2)
	broker.Unsubscribe("sports", sub3)
}

type Message struct {
	Topic   string
	Content string
}

type Broker struct {
	subscribers map[string][]chan Message
	mu          sync.RWMutex
	stop        chan bool
}

func NewBroker() *Broker {
	return &Broker{
		subscribers: make(map[string][]chan Message),
		stop:        make(chan bool),
	}
}

func (b *Broker) Start() {
	// Broker is ready to handle subscriptions and publications
}

func (b *Broker) Stop() {
	close(b.stop)
}

func (b *Broker) Subscribe(topic string) chan Message {
	b.mu.Lock()
	defer b.mu.Unlock()

	ch := make(chan Message, 10)
	b.subscribers[topic] = append(b.subscribers[topic], ch)
	return ch
}

func (b *Broker) Unsubscribe(topic string, ch chan Message) {
	b.mu.Lock()
	defer b.mu.Unlock()

	if subs, exists := b.subscribers[topic]; exists {
		for i, sub := range subs {
			if sub == ch {
				close(ch)
				b.subscribers[topic] = append(subs[:i], subs[i+1:]...)
				break
			}
		}
	}
}

func (b *Broker) Publish(msg Message) {
	b.mu.RLock()
	defer b.mu.RUnlock()

	if subs, exists := b.subscribers[msg.Topic]; exists {
		for _, sub := range subs {
			select {
			case sub <- msg:
			default:
				// Subscriber is slow, skip
			}
		}
	}
}

func demonstrateSemaphore() {
	fmt.Println("\n--- Semaphore Pattern ---")

	// Limit concurrent operations to 3
	semaphore := make(chan bool, 3)
	var wg sync.WaitGroup

	// Simulate 10 tasks that need limited concurrency
	for i := 1; i <= 10; i++ {
		wg.Add(1)
		go func(taskID int) {
			defer wg.Done()

			// Acquire semaphore
			semaphore <- true
			fmt.Printf("Task %d started\n", taskID)

			// Simulate work
			time.Sleep(time.Duration(rand.Intn(200)+100) * time.Millisecond)

			fmt.Printf("Task %d completed\n", taskID)
			// Release semaphore
			<-semaphore
		}(i)
	}

	wg.Wait()
	fmt.Println("All tasks completed")
}
