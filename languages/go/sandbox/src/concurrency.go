// referenced "A Tour of Go" (https://go.dev/tour/concurrency/1)

package main

import (
	"fmt"
	"sync"
)

func sum(s []int, c chan int) {
	sum := 0
	for _, v := range s {
		sum += v
	}
	c <- sum
}

// `select` statement lets goroutine wait on multiple communication operation,
// which blocks until one of the `case` can run, and then executes,
// if multiple cases are ready, one at random is chosen,
// and `default` is run if no other cases are ready
func fibonacci(num, quit chan int) {
	x, y := 0, 1
	for {
		select {
		case num <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("quit")
			return
		default:
		}
	}
}

// Mutual exclusion, conventional name mutex, is a concept,
// which ensures only one goroutine to access a variable at a time
type MutexCounter struct {
	mu sync.Mutex
	v  int
}

// `sync.Mutex` package provides 2 methods,
// - Lock(), allow only one goroutine to access at a time
// - Unlock(), restore state, use `defer` to ensure mutex unlock
func (c *MutexCounter) Increment() {
	c.mu.Lock()
	c.v++
	c.mu.Unlock()
}

func (c *MutexCounter) Value() int {
	c.mu.Lock()
	defer c.mu.Unlock()
	return c.v
}

func main() {
	// goroutine is a lightweight thread managed by Go runtime
	// `go f(x)` starts a new goroutine running `f(x)`,
	// where `f`, `x` are evaluated in the current goroutine,
	// but the execution happens in the new goroutine
	// goroutines run in the same address space,
	// so access to shared memory must be synchronized
	go fmt.Println("hello")
	fmt.Println("world")

	// channels are typed conduit through which values can be sent or received,
	// using `<-` channel operator, which data flows in the arrow direction
	// channels must be created before using
	c := make(chan int)
	s := []int{7, 2, 8, -9, 4, 0}
	go sum(s[:len(s)/2], c)
	go sum(s[len(s)/2:], c)
	// by default, sends and receives block until the other side is ready,
	// allowing goroutines to synchronize without explicit controls
	x, y := <-c, <-c
	fmt.Println(x, y, x+y)

	// channels can be buffered, by setting the capacity of the channel,
	// block happens on receiving when buffer is empty, and sending when filled
	cbuf := make(chan int, 2)
	cbuf <- 1
	cbuf <- 2
	// closing the channel is necessary for receivers, such as `range` loop,
	// that needs to be told there are no more values coming
	// channels should be closed at the sender side, else will cause a panic
	close(cbuf)
	v, ok := <-cbuf
	fmt.Println(v, ok)
	for v := range cbuf {
		fmt.Println(v)
	}

	num := make(chan int)
	quit := make(chan int)
	go func() {
		for i := 0; i < 5; i++ {
			fmt.Println(<-num)
		}
		quit <- 0
	}()
	fibonacci(num, quit)

	mc := MutexCounter{v: 0}
	for i := 0; i < 1000; i++ {
		go mc.Increment()
	}
	fmt.Println(mc.Value())
}
