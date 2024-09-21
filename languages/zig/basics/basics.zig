// referenced "zig.guide" (https://zig.guide/)

// `@import` built-in function takes in a file, and gives as a struct type
// all declarations labelled as `pub` (public) ends up in the given struct type
// `@import("std")` gives access to the standard library,
// other imports takes in a file path, or a package name
@import("std")

// value assignment has syntax: `(const|var) identifier[: type] = value`
// variables are written in snake_case
const constant: i32 = 5;
var variable: u32 = 5000;
// @as performs an explicit type coercion
const inferred_constant = @as(i32, 5);
// undefined value, may be used as long as type annotation is provided
const a: i32 = undefined;

// hex, octal and binary integer literals are supported
// integer widening is allowed, if the casted type can fit all value
const decimal_int: i32 = 98222;
const hex_int: u8 = 0xff;
const octal_int: u16 = 0o755;
const binary_int: u8 = 0b1111_0000; // underscores for visual seperator

// floats support multiple kinds of literals
const floating_point: f64 = 123.0E+77;
const another_float: f64 = 123.0;
const yet_another: f64 = 123.0e+77;

// arrays are denoted by `[N]T`,
// where `N` is the element number, and `T` is the type
const a = [5]u8{ 'h', 'e', 'l', 'l', 'o' };
// for `N`, `_` can be specified to infer size of array
const b = [_]u8{ 'w', 'o', 'r', 'l', 'd' };
// the size of the array can be given from the `len` field
const length = a.len;

// if statements only accept bool values,
// unlike other languages, there are no values that implicitly coerce to bool
const flag = true;
if (flag) {
  // ...
} else {
  // ...
}
// as expression
var x: u16 = 0;
x += if (flag) 1 else 2;

// while loop has three parts: condition, block, and continue expression
// there are `inline` loops that unroll and processes on compile time
var i: u8 = 0;
while (i < 10) : (i += 1) {
  // ...
}

// for loops use arrays to iterate over
const strings = [_]u8{ 'a', 'b', 'c' };
for (string, 0..) |character, index| {
  // ...
}
// loops can be given labels, allowing breaking and continuing to outer loops
var count: usize = 0; // usize is equivalent to @sizeOf(*u8)
outer: for ([_]i32{ 1, 2, 3, 4, 5, 6, 7, 8 }) |_| {
  for ([_]i32{ 1, 2, 3, 4, 5 }) |_| {
    count += 1;
    continue :outer;
  }
} // => count = 8

// all function arguments are immutable
// functions are written in camelCase
fn addFive(x: u32) u32 {
  return x + 5;
}

// defer is used to execute a statement while exiting the current block
var x: i16 = 5;
{
  defer x += 2;
}

// blocks can be given labels, which are used to yield values
const count = blk: {
  var sum: u32 = 0;
  var i: u32 = 0;
  while (i < 10) : (i += 1) sum += i;
  break :blk sum;
} // => count = 45

// all switch branches must coerce to the type being switched upon,
// and all possible values must have an associated branch
var x: i8 = 10;
switch (x) {
  -1...1 => {
    // ...
  },
  10, 100 => {
    // ...
  },
  else => {},
}
// as expression
x = switch (x) {
  -1...1 => // ...
}

// normal pointers follows the syntax `*T`, and cannot have 0 or null as value,
// pointer having multiple elements follows the syntax `[*]T`
// referencing is done with `&var`, and dereferencing is done with `var.*`
fn increment(num: *u8) void {
  num.* += 1;
};
var x: u8 = 1;
increment(&x) // => x = 2
// const pointers cannot be used to modify the referenced data
const x: u8 = 1;
var y = &x; // cannot assign `y.* += 1;`

// slices are created from an array with syntax `x[n..m]`,
// for slicing until the end the syntax is `x[n..]`
// slices have the same attributes as pointers, meaning there are const slices
const array = [_]u8{ 1, 2, 3, 4, 5 };
const slice = array[0..3]; // slice = { 1, 2, 3 }

// sentinel termination, terminates array, slices and many pointers by a value,
// using the syntax `[N:t]T`, `[:t]T` or `[*:t]T`, where `t` is value of `T`
const terminated [3:0]u8{ 3, 2, 1 }; // last element is followed by a 0 byte

// enum allows to define types with a restricted set of named values
const Direction = enum { north, south, east, west };
// values can be overriden, with the next values continuing from the last value
const Value = enum(u32) {
  hundred = 100,
  thousand = 1000,
  million = 1000000,
  next, // => next = 1000001
};
// methods can also be given, that can be called with dot syntax
const Suit = enum {
  clubs,
  spades,
  diamonds,
  hearts,
  pub fn isClubs(self: Suit) bool {
    return self == Suit.clubs;
  }
};
Suit.clubs.isClubs(); // => == Suit.isClubs(.clubs)
// variable declarations can also be give, acting as namespaced globals,
// which the values are unrelated and unattached to instances of the enum type
const Mode = enum {
  var count: u32 = 0;
  on,
  off,
};
Mode.count += 1; // => Mode.count == 1

// structs allow to define types that can store fixed set of named fields
// there is no guarantees about the in-memory order of the fields
// struct fields cannot be implicitly uninitialised, so may be given defaults
const Vec3 = struct { x: f32, y: f32, z: f32 = 0 };
const vec = Vec3{
  .x = 0,
  .y = 100,
};
// struct can be given functions and declarations,
// and has the unique property that when given a pointer to a struct,
// one level of dereferencing is done automatically when accessing the fields
const Stuff = struct {
  x: i32,
  y: i32,
  fn swap(self: *Stuff) void {
    const tmp = self.x;
    self.x = self.y;
    self.y = tmp;
  }
}
var thing = Stuff{ .x = 10, .y = 20 };
thing.swap() // thing.x = 20, thing.y = 10

// unions allow for type definition that store one value from the possibilities
const Result = union {
  int: i64,
  float: f64,
  bool: bool,
};
var result = Result{ .int = 1234 };
result.float = 12.34; // => error: access of inactive union field
// tagged unions uses enum to detect which field is active.
const Tag = enum { a, b, c };
// instead of `union(Tag)`, `union(enum)` can be used for inferrence
const Tagged = union(Tag) { a: u8, b: f32, c: bool };
var value = Tagged{ .b = 1.5 };
switch (value) {
  .a => |*byte| byte.* += 1,
  .b => |*float| float.* *= 2,
  .c => |*b| b.* = !b.*,
} // => value.b = 3

// optionals use the syntax `?T`, and stores `null` or value of type `T`
// `orelse` expression can be used for assignment when the optional is null
const a: ?f32 = null;
const fallback_value: f32 = 0;
const b = a orelse fallback_value; // b => 0
// `.?` is shorthand for `orelse unreachable`, if the value cannot be null
if (b != null) {
  const value = b.?;
}

// `opaque` types have unknown size and alignment,
// and used to maintain type safety with pointers to types without information
const Window = opaque {};
extern fn show_window(*Window) callconv(.C) void;
var main_window: *Window = undefined;
show_window(main_window);

// struct type may be omitted from struct literals
const fullyAnonymous = .{
  .int = @as(u32, 1234),
  .float = @as(f64, 12.34),
  .b = true,
  .s = "hi",
}
// anonymous structs without filed names can be created, and refered as tuples
const tuple = .{
  @as(u32, 1234),
  @as(f64, 12.34),
  true,
  "hi",
}
tuple[0] // = 1234
tuple.@"0" // `@""` can be used to access field, equivalent to above

// error set, is like an enum, where each error is a value, not an exception
const FileOpenError = error{
  AccessDenied,
  OutOfMemory,
  FileNotFound,
}
// error sets coerce to their supersets
const AllocationError = error{OutOfMemory}
const err: FileOpenError = AllocationError.OutOfMemory;
// error set type and other type can be combined with `!` to form a union type
// when using a catch, `|err|`syntax receives the value of the error
var problems: u32 = 0;
fn failingFunc() error{Oops}!void {
  // `errdefer` executes defer when returned with an error
  errdefer problems += 1;
  return error.Oops;
}
failingFunc() catch |err| {
  // ...
}
// error sets can be merged
const C = FileOpenError || AllocationError

// `unreachable` is an assertion to the compiler for an impossible branch
fn asciiToUpper(x: u8) u8 {
  return switch (x) {
    'a'...'z' => x + 'A' - 'a',
    'A'...'Z' => x,
    else => unreachable,
  };
}
