// referenced "A Tour of Go" (https://go.dev/tour/basics/1)

// every Go program is made up of packages, and starts running in package `main`
package main

// packages can be imported using multiple import statement,
// but can also be written as "factored" import statement, with parenthesis
import (
	"fmt"
	"math"
	"runtime"
)

// variables are declared with a `var` statement,
// and can be declared at package level or at function level,
// which can also be written as "factored" blocks
var (
	python, c bool
	z         complex128
	text      string
	pointer   *int
	slice     []int
	m         map[string]int
)

// constants are declared with a `const` statement,
// and can not be declared by the `:=` syntax
const (
	// names are exported if it begins with a capital letter,
	// and unexported names are not accessible from outside the package
	// eg. math.pi is undefined and cannot be accessed
	pi = math.Pi
)

// `struct` is a collection of fields
type Vector struct {
	X int
	Y int
}

// functions can take in zero or more arguments, and can output multiple values,
// with types coming after variable names
func add(x int, y int) int {
	return x + y
}

// functions can be passed into other functions
func decorate(fn func(int, int) int) (string, int) {
	return "Hello world!", fn(2, 3)
}

// functions can be closures, which is a function value that references
// variables from outside its body, and "bound" to its own variables
// in other words, function that returns an inner function
func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}

	// closures can also be used to implement generators, by internal update
	/*
		return func() int {
			sum++
			return sum
		}
	*/
}

func main() {
	// if initializer is present for declaration, the type can be omitted
	var a = 1
	// inside a function, `:=` short assignment statement can be used for
	// variable declaration with implicit type
	b := 2
	fmt.Println(add(a, b))
	fmt.Println(decorate(add))

	// without any initializer, zero values are given to the variables
	// zero values for slices, maps are `nil`
	fmt.Println(python, z, text, pointer, slice, m)

	// `for` loop is the only looping construct available,
	// init and post statements are optional, condition given from elsewhere,
	// which acts as the "while" looping construct
	for i := 0; i < 3; i++ {
		fmt.Println(i)

		// `if` statement,
		// which variables declared can be used including `else` block
		if j := 1; j < 1 {
			break
		}

		// `defer` statement defers the execution of a function until
		// the surrounding function returns,
		// deferred function calls are pushed onto a stack
		defer fmt.Println(i)
	}
	// `for` loop can reference a slice or map with `range`,
	// which returns the index and value for each iteration
	pow := []int{1, 2, 4, 8}
	for i, v := range pow {
		fmt.Println(i, v)
	}

	// labeled statement may be the target of goto, break or continue
Loop:
	for {
		for {
			break Loop
		}
	}

	// `switch` statement,
	// which runs only on the selected case, so `break` is unnecessary
	// without condition, this can be used for long if-then-else chains
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X")
	case "linux":
		fmt.Println("Linux")
	default:
		fmt.Printf("%s\n", os)
	}

	// pointers can be used for "dereferencing" or "indirecting",
	// but has no pointer arithmetics
	var p *int
	p = &a
	*p = 10         // set 'a' through pointer p
	fmt.Println(*p) // read 'a' through pointer p

	// struct field can be accessed with a dot,
	// or through a struct pointer
	v := Vector{Y: 2, X: 1}
	fmt.Println(v.X)

	// arrays must declare the length, so cannot be resized,
	// type of values can be a `struct`
	array := [5]int{10, 20, 30, 40, 50}

	// slices are dynamically-sized, and views into the elemtents of an array,
	// changing the elements of the slice modifies the corresponding elements
	// of its underlying array
	var s1 []int = array[1:3]
	var s2 []int = array[0:2]
	s1[0] = 100
	fmt.Println(array, s1, s2)
	// slices can be declared without the underlying array,
	// zeroed array is auto-created, and then builds a slice that references it
	s := []int{100, 200, 300, 400, 500}
	// slices have the following properties:
	// - "length": number of elements it contains
	// - "capacity": number of elements in the underlying array,
	//               counting from the first element in the slice
	fmt.Println(
		len(s), cap(s),
		make([]int, 1, 5), // `make([]T, len, cap)` to create slices
		append(s, 600),    // `append([]T, ...T)` to append elements
	)

	// maps are like structs, but keys are required
	m := make(map[string]int) // `make(map[T]T, cap)` to create maps
	m["one"] = 1
	elem, ok := m["one"] // test if a key is present with two-value assignment
	fmt.Println(m, elem, ok)

	// using function closures
	neg := adder()
	for i := 0; i < 5; i++ {
		fmt.Println(neg(-2 * i))
	}

	// panic built-in function stops the ordinary flow of control
	// recover built-in function regains control of panicking goroutine
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("recovered from:", r)
		}
	}()
	panic("panicking!!")
}
