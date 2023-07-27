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

// to allow the constraint to include the original type definition,
// ~ needs to be added infront of the type
// eg. without ~, "CustomInt" to a type parameter of "Number" raises an error,
//     but with ~, as "CutomInt" is originally "int" type, the error resolves
type Number interface {
	~int | int32 | int64 | float32 | float64
}

func PrintNumber[T Number](n T) {
	fmt.Println(n)
}

// generic types can implement generic data structures,
// however method for these structures can not hold type parameters
// eg. singly-linked list holding any type of value
type List[T any] struct {
	next *List[T]
	val  T
}

// generic types can also be used for type definitions
type Vector[T any] []T
type VectorInt = Vector[int]

func main() {
	si := []int{10, 20, 15, -10}
	ss := []string{"foo", "bar", "baz"}
	fmt.Println(Index(si, 15), Index(ss, "hello"))

	type CustomInt int
	var x CustomInt = 1
	PrintNumber[CustomInt](x)
}
