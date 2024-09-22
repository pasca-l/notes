# referenced "Nim Tutorial (Part 1)" (https://nim-lang.org/docs/tut1.html)

# comments can be written with a single `#`
#[
    for multi-line comments, the comment is put between `#[` and `]#`,
    #[
        and can also be nested
    ]#
]#
var variable: int ## documentation comment starts with `##`

# variables can be declared with indentation after the `var` keyword
var x, y: int
var
    x, y: int
    a, b, c: string
# multiple variables can be assigned with a single value
x, y = 3 # x = 3, y = 3

# constants value must be able to be evaluated by at compile time
# indentation after the `const` keyword can also be used for declaration
const
    x = 1
    y = x + 1 # computations are also possible

# `let` statement declares a single assignment to a symbol (not re-assignable)
# different to `const`, `let` variable is not evaluated at compile time
let input = readLine(stdin)
# `const input = readLine(stdin)` -> `Error: constant expression expected`

# if statement branches the control flow
if input == "":
    echo "no input"
elif input == "hi":
    echo "hello"
else:
    echo "got input: ", input, "!"

# case statement also branches the control flow
from std/strutils import parseInt
case parseInt(input)
of 1..7:
    echo "number is in the range 1-7"
of 0, 8:
    echo "number is either 0 or 8"
# every possible value given for the case needs to be covered
else:
    discard # do nothing statement

# while statement is a simple looping construct
while input == "":
    echo "enter something again!"
    input = readLine(stdin)

# for statement constructs loop over elements provided by an iterator
for i in countup(1, 10):
    echo i
# can be also done with a `..` iterator
var s = "some string"
for i in 0 ..< s.len: # `..<` shortcut gives a one less, same as 0 .. s.len-1
# or using `for idx, i in s[0 .. ^1]`, where ^1 is the last element
    echo i
# other iterators are such as `item`, `mitem`, `pairs`, and `mpairs`

# when statement is useful for writing platform-specific code
# the compiler only produces code only for the condition that evaluates to true
when system.hostOS == "windows":
    echo "running on Windows!"
elif system.hostOS == "linux":
    echo "running on Linux!"
elif system.hostOS == "macosx":
    echo "running on Mac OS X!"
else:
    echo "unknown operating system"

# identifiers are only visible within the block that it has been declared
block thisblock: # block statement explicitly opens new block
    echo "entered block"
    while true:
        echo "while loop"
        break thisblock # leaves the loop, and the block
    echo "does not print" # as the block is escaped, this is not printed
echo "outside the block"

# there are simple statements such as assignments, procedure calls, or return,
# and complex statements such as if, when, for, while
# complex statements can contain other statements and must be indented
if x:
    x = false
    y = false
# expressions can contain indentation at certain places for readability
if thisIsALongCondition() and
    thisIsAnotherLongCondition(1,
        2, 3, 4):
    x = true

# procedures are defined with the `proc` keyword
# this is differentiated with methods and functions in other languages
# there is an implicit `result` variable declared as the return value
proc sumTillNegative(x: varargs[int]): int =
    for i in x:
        if i < 0:
            return
        result = result + i

echo sumTillNegative() # echoes 0
echo sumTillNegative(3, 4, -1, 6) # echoes 7

# procedures that does not have any `return` and does not use `result` variable,
# returns the value of its last expression
proc helloWorld(): string =
    "Hello, World!" # this expression is returned

# parameters are immutable in the procedure body,
# so if a mutable variable is needed, `var` needs to be used
proc divmod(a, b, res: int; remainder: var int) = # `var` used for argument
    var res = a div b # shadowing the parameter
    remainder = a mod b

var
    x, y: int
divmod(a=8, b=5, x, y) # modifies only the `var` parameters
echo x # x = 0, where res = 1
echo y # y = 3

# procedures that return a value just for its side effect must return `discard`
# the return value can be ignored implicitly using `discardable` pragma
proc p(x, y: int): int {.discardable.} =
    return x + y
p(3, 4) # without `discard`, the expression must be used somewhere

# procedures have the ability to be overloaded,
# where the compiler chooses the most appropriate proc on a call
proc toString(x: int): string =
    result =
        if x < 0: "negative"
        elif x > 0: "positive"
        else: "zero"

proc toString(x: bool): string =
    result =
        if x: "true"
        else: "false"

toString(13) # calls toString(x: int)
toString(true) # calls toString(x: bool)

# a user defined operator can be overloaded using proc
# the parser lets infix notation and prefix notation only (no postfix)
# the newly defined operator is enclosed with backticks "`"
proc `$` (x: myDataType): string =
    # ...

# iterators can be called only from loops, yielding values
iterator countingup(a, b: int): int =
    var res = a
    while res <= b:
        yield res
        inc(res)
for i in countingup(1, 3): echo i

# modules are written in its own file, and can be imported and exported
# only top-level symbols that are marked with `*` are exported
var
    x*, y: int # x is exported, but not y

# imports are done with `import` statement
import mymodule
import mymodule except y # excluding some symbols
from mymodule as m import x, z # importing some symbols, with aliasing

# `include` statement can be used to split up large modules into files
include fileA, fileB, fileC
