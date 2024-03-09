// referenced "A Tour of Go" (https://go.dev/tour/methods/1)

package main

import (
	"fmt"
	"math"
)

type Vector struct {
	X, Y float64
}

// as there is no classes, methods can be defined on types, in the same package
// methods are functions with a special receiver argument,
// which the receiver appears between `func` keyword and method name
func (v Vector) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

// methods can be declared with pointer receivers,
// which can modify the value to which the receiver points
func (v *Vector) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

// with a value receiver, the method operates on a copied original value,
// and is more efficient to avoid copying the value for each method call
func (v Vector) ScaleValueReceiver(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

type CustomFloat float64

// methods can also be declared on non-struct types as well
func (f CustomFloat) Abs() float64 {
	if f < 0 {
		return float64(-f)
	}
	return float64(f)
}

// interface type is defined as a set of method signatures
// types implements the interface but no `implement` keyword is needed,
// which allows decoupling of interface definition from its implementation
// interface that specifies zero methods are called empty interface,
// which is used by code that handles values of unknown type
type Abser interface {
	Abs() float64
}

// functions receiving interfaces allow to conduct method declared on any type
func ShowAbs(a Abser) {
	// interface values can be thought of as a tuple of concrete value and type
	// if the concrete value is nil, methods will be called with a nil receiver,
	// without triggering a null pointer exception like in other languages
	// interface value that holds nil concrete value is itself non-nil,
	// but no concrete type too (nil interface) will cause run-time error
	fmt.Printf("interface: (%v, %T)\n", a, a)

	// type switch is like regular switch statement, but is switched by type
	// `type` keyword is used with the same syntax as the type assertion
	switch a.(type) {
	case Vector:
		fmt.Printf("Abs() result (length of vector): %f\n", a.Abs())
	case CustomFloat:
		fmt.Printf("Abs() result (unsigned value): %f\n", a.Abs())
	default:
		fmt.Println("Unknown type given")
	}
}

func main() {
	v := Vector{3, 4}
	fmt.Println(v.Abs())

	// methods with receivers can be given either a value or a pointer,
	// which gets interpreted as the appropriate receiver
	// this cannot be done with functions, which the receiver is specified
	// eg. v.PointerReceiver() is interpreted as (&v).PointerReceiver()
	//     p.ValueReceiver() is interpreted as (*p).ValueReceiver()
	v.Scale(10)
	fmt.Println(v.Abs())

	v.ScaleValueReceiver(10)
	fmt.Println(v.Abs())

	// eg. Vector implements Abs(), which is necessary for the Abser interface,
	//     so can be assigned to the variable
	var a1 Abser = v
	ShowAbs(a1)
	var a2 Abser = CustomFloat(-2)
	ShowAbs(a2)

	// type assertion asserts the interface value holding the concrete type,
	// and assigning the underlying value to the variable
	// if the assertion fails, the statement triggers a panic
	// two-value assignment can test this, returning zero value if panic occurs
	t, ok := a1.(CustomFloat)
	fmt.Println(t, ok)
}
