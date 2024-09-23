# referenced "Nim Tutorial (Part 2)" (https://nim-lang.org/docs/tut2.html)

# object oriented programming (OOP) is minimalistically supported
# inheritance is entirely optional,
# objects needs to inherit from `RootObj` to inherit with runtime type
# composition (has-a relation) is often prefered to inheritance (is-a relation),
# as objects are value types, and composition is as efficient as inheritance
type
    Person = ref object of RootObj # `ref` is not strictly enforced
        name*: string # with `*`, the field is accessible from other modules
        age: int # without `*`, the field is hidden from other modules

    Student = ref object of Person # Student inherits from Person
        id: int
var
    student: Student
assert(student of Student) # checking type at runtime with `of`

# mutually recursive types, types that depend on each other,
# can only be declared within a single type section
type
    Node = ref object # a reference to an object
        le, ri: Node
        sym: ref Sym

    Sym = object # a symbol
        name: string
        line: int
        code: Node

# type conversions and type casts are distinguished,
# where casting forces the compiler to interpret a bit pattern in another type,
# but conversions preserve the abstract value, allowing the compiler to complain
proc getID(x: Person): int =
    Student(x).id

# object variants can simplify object hierarchy in certain situations
type
    NodeKind = enum
        nkInt,
        nkFloat,
        nkString,
        # ...
    Node = ref object
        case kind: NodeKind
        of nkInt: intVal: int
        of nkFloat: floatVal: float
        of nkString: strVal: string
        # ...
var n = Node(kind: nkFloat, floatVal: 1.0)
n.strVal = "" # this raises `FieldDefect`, as n.kind is not appropriate

# syntax `obj.method(args)` can be used instead of `method(obj, args)`
assert(len("abc") == "abc".len) # with no args, parentheses may be omitted

# ordinary get-procedures can be called with the method call syntax,
# but a special setter syntax is needed for setting values
type
    Socket* = ref object of RootObj
        h: int # cannot be accessed from outside

proc `host=`*(s: var Socket, value: int) {.inline.} =
    # setter of host address
    s.h = value

proc host*(s: Socket): int {.inline.} =
    # getter of host address
    s.h

var s: Socket
new s
s.host = 34 # equivalent to `host=`(s, 34)

# `method` keyword is used instead of `proc` for dynamic dispatch
type
    Thing = ref object of RootObj
    Unit = ref object of Thing
        x: int

method collide(a, b: Thing) {.inline.} =
    quit "to override!"

method collide(a: Thing, b: Unit) {.inline.} =
    echo "collided Thing with Unit"

method collide(a: Unit, b: Thing) {.inline.} =
    echo "collided Unit with Thing"

var a, b: Unit
new a
new b
collide(a, b) # echoes "collided Unit with Thing", as resolution works from left

# exceptions are objects, derived from `system.Exception`,
# and has to be allocated on heap due to unknown lifetime, instead on stack
# raising an exception is done with the `raise` statement
raise newException(OSError, "request to OS failed")

# `try` statement handles exceptions
try:
    # ...
except OverflowDetect:
    echo "overflow!"
except ValueError:
    echo "value error!"
except CatchableError:
    # accessing the actual exception object or message
    let
        e = getCurrentException()
        msg = getCurrentExceptionMsg()
    echo "got exception ", repr(e), " with message ", msg
    raise # reraises the unknown exception
except:
    # if something else from the list above is raised
finally:
    # ...

# generics are written with syntax `Foo[T]`, where `T` is the generic parameter
type
    BinaryTree*[T] = ref object
        le, ri: BinaryTree[T]
        data: T
