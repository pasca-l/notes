// referenced "A Tour of Go" (https://go.dev/tour/methods/1)

package main

import (
	"fmt"
	"image"
	"image/color"
	"io"
	"os"
	"strings"
	"time"
)

// Stringer, defined by `fmt` package, is a type to describe itself as string
/*
type Stringer interface {
	String() string
}
*/

type Vector struct {
	X, Y float64
}

func (v *Vector) String() string {
	return fmt.Sprintf("vector with x:%v, y:%v", v.X, v.Y)
}

// built-in error type, `fmt` package looks for this interface
/*
type error interface {
	Error() string
}
*/

type CustomError struct {
	When time.Time
	What string
}

func (e *CustomError) Error() string {
	return fmt.Sprintf("error at: %v, with content: %s", e.When, e.What)
}

func run() (string, error) {
	return "running", &CustomError{time.Now(), "error"}
}

// `io.Reader` wrapping another `io.Reader` can be used to modify the stream
// eg. applying ROT13 substitution cipher to all alphabetical characters
type Rot13Reader struct {
	r io.Reader
}

func (rot13 *Rot13Reader) Read(b []byte) (int, error) {
	n, err := rot13.r.Read(b)
	for i, v := range b {
		switch {
		case v >= 'A' && v < 'N', v >= 'a' && v < 'n':
			b[i] += 13
		case v >= 'N' && v <= 'Z', v >= 'n' && v <= 'z':
			b[i] -= 13
		}
	}
	return n, err
}

// Image, defined by `image` package,
// - `Rectangle` is a type defined in `image` package
// - `color.Model` is an interface defined in `image/color` package
// - `color.Color` is an interface defined in `image/color` package
/*
type Image interface {
	ColorModel() color.Model
	Bounds() Rectangle
	At(x, y int) color.Color
}
*/

// eg. implementation of Image (without using interface)
type Image struct{}

func (i Image) ColorModel() color.Model {
	return color.RGBAModel
}

func (i Image) Bounds() image.Rectangle {
	return image.Rect(0, 0, 256, 256)
}

func (i Image) At(x, y int) color.Color {
	return color.RGBA{uint8(x), uint8(y), 255, 255}
}

func main() {
	v := &Vector{1, 2}
	fmt.Println(v)

	if _, err := run(); err != nil {
		fmt.Println(err)
	}

	// `io` package specifies the `Reader` interface,
	// which represents the read end of a stream of data (files, networks, etc.)
	// `Read` method populates the given slice with data
	r := strings.NewReader("Hello, Reader!")
	b := make([]byte, 8)
	for {
		n, err := r.Read(b) // `func (T) Read(b []byte) (n int, err error)`
		fmt.Printf("n = %v, err = %v, b = %v, b[:n] = %q\n", n, err, b, b[:n])

		// `io.EOF` error is given when the stream ends
		if err == io.EOF {
			break
		}
	}

	cipher := strings.NewReader("Lbh penpxrq gur pbqr!\n")
	rot13r := Rot13Reader{cipher}
	io.Copy(os.Stdout, &rot13r)
}
