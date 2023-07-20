// referenced "A Tour of Go" (https://go.dev/tour/generics/1)

package main

import (
	"fmt"
)

// generic functions can work on multiple types using type parameters,
// which fulfills the constraint defined by an interface
// eg. below, `T` is the type parameter, and `comparable` is the interface
func Index[T comparable](s []T, x T) int {
	for i, v := range s {
		// v, x are both type T with comparable, so `==` can be used
		if v == x {
			return i
		}
	}
	return -1
}

// generic types can implement generic data structures
// eg. singly-linked list holding any type of value
type List[T any] struct {
	next *List[T]
	val  T
}

func main() {
	si := []int{10, 20, 15, -10}
	ss := []string{"foo", "bar", "baz"}
	fmt.Println(Index(si, 15), Index(ss, "hello"))
}
