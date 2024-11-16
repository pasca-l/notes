// referenced "Common Programming Concepts" (https://doc.rust-lang.org/book/ch03-00-common-programming-concepts.html)

// by default, variables are immutable
let x = 5;
println!("Value of x: {x}")
// x = 3; -> error: cannot assign twice to immutable variable

// shadowing can be done by redefining values with the same name
// with shadowing, the type of value can be changed
let x = "3";

// however mutable variables can be declared using `mut`
let mut y = 3;
y = 6;
println!("Value of y: {}", y)

// constants are declared with `const`, which does not allow `mut`
// the type of constant variables must be annotated
// values computed at runtime cannot be set to constants
const THREE_MINUTES_IN_SECONDS: u32 = 3 * 60;

// Rust has scalar types and compound types
// scalar types include: integers, floats, booleans, and characters
// compound types include: tuples and arrays

// tuples are group of values with any types
// tuple with empty value is called a 'unit'
let tup: (i32, f64, bool, char) = (400, 8.2, true, 'c');
// getting individual values can be done by pattern matching
let (w, x, y, z) = tup;
// or, by accessing elements directly
let el = tup.0;

// arrays must have elements of the same type
// arrays are useful when data should be on stack instead of heap
let arr: [i32; 5] = [1, 2, 3, 4, 5];
// arrays with the same element can be written in shorthand
let same_arr = [3; 5]; // -> same as [3, 3, 3, 3, 3]
// elements are accessed by indexing
let el = arr[0];

// functions are defined using `fn` keyword
// each parameter types must be declared
// return values also need to have types declared after `->`
fn some_function(x: i32) -> i32 {
    // a new scope block with curly brackeds is an expression
    let y = {
        let x = 3;
        // if adding a semicollon, it becomes a statement
        x + 1
    }
}

// if expression is given the `if` keyword, followed by the condition
// the condition block is sometimes called arms
let number = 3;
// Rust does not automatically convert values to boolean types
// eg. if number, would result in error
if number < 5 {
    println!("number is less than 5");
} else if number == 5 {
    println!("number is 5");
} else {
    println!("number is greater than 5");
}
// because if is an expression, it can be used for statements,
// and each arms must have the same value types
let condition = true;
let number = if condition { 5 } else { 6 };

// there are three kinds of loops: `loop`, `while`, and `for`
// `loop` can give back values on break,
let mut counter = 0;
let result = loop {
    counter += 1;
    if counter == 10 {
        break counter * 2;
    }
}
// and can have labels, which must begin with a single quote
'outer_loop: loop {
    loop {
        if false {
            break;
        }
        if true {
            break 'outer_loop;
        }
    }
}

// `while` handles conditions for loops
let mut counter = 3;
while counter != 0 {
    number -= 1;
}

// `for` loops over the elements of a collection
let a = [10, 20, 30, 40];
for el in a {
    println!("value of element in a: {}", el)
}
