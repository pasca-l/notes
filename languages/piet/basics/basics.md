# Piet basics <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->

## Overview
Piet is one of an esoteric programming language, which the program code is in the form of abstract art. It is one of a stack-oriented programming language.

> Piet is a programming language in which programs look like abstract paintings. The language is named after Piet Mondrian, who pioneered the field of geometric abstract art.

## Language concepts
Piet uses 20 distinct colors, 18 of the colors are related cyclically in the order of hue and lightness, and 2 of the colors (white and black) do not fall in either cycle. (Additional colors can be used depending on interpreter implementation.)

- Hue cycle: red -> yellow -> green -> cyan -> blue -> magenta -> red -> ...
- Lightness cycle: light -> normal -> dark -> light -> ...

| | | | | | |
| --- | --- | --- | --- | --- | --- |
| #FFC0C0 (light red) | #FFFFC0 (light yellow) | #C0FFC0 (light green) | #C0FFFF (light cyan) | #C0C0FF (light blue) | #FFC0FF (light magenta) |
| #FF0000 (red) | #FFFF00 (yellow) | #00FF00 (green) | #00FFFF (cyan) | #0000FF (blue) | #FF00FF (magenta) |
| #C00000 (dark red) | #C0C000 (dark yellow) | #00C000 (dark green) | #00C0C0 (dark cyan) | #0000C0 (dark blue) | #C000C0 (dark magenta) |
| #FFFFFF (white) | | | #000000 (black) | | |

Piet recognises codes at pixel scale, but for viewing purpose, pixels can be enlarged into "codels", meaning the block of color equivalent to a single pixel of code. The basic unit of Piet code is color block, which is a contiguous block of any number of codels of one color, bounded by blocks of other colors or by the edge of the program graphic (blocks diagonally adjacent are not contiguous).

## Program execution
Piet language interpreter begins executing a program in the color block which includes the upper left codel of the program. The interpreter maintains a Direction Pointer (DP), initially pointing to the right (and may point either left, right, up or down). The interpreter also maintains a Codel Chooser (CC), initially pointing to the left (and may point either left or right).

> As the program is executed, the interpreter traverses the color blocks with the following rules:
> 1. The interpreter finds the edge of the current color block which is furthest in the direction of the DP.
> 2. The interpreter finds the codel of the current color block on that edge which is futhest in the direction of the CC of the DP's direction of travel.
> 3. The interpreter travels from that codel into the color block containing the codel immediately in the direction of the DP.

## Syntax elements
Each non-black, non-white color block in Piet program represents an integer equal to the number of codels in that block.

Black color blocks and edges of the program restrict program flow. If the interpreter attempts to move into a black block or off an edge, it is stopped and CC is toggled. The interpreter then attempts to move from its current block again. If it fails, the DP is moved clockwise one step. These attemps are repeated for maximum eight times, until the interpreter cannot leave its current color block, and the program terminates.

White color blocks are "free" zones, which the interpreter can pass unhindered. The interpreter slides through the white codels in the direction of the DP until it reaches a non-white color block.

Commands are defined by the transition of color, and the number of steps along the hue cycle and lightness cycle in each transition determines the command to be executed (no command is executed when transition happens via slide across a white color block).

| | 0 lightness | 1 lightness | 2 lightness |
| --- | --- | --- | --- |
| 0 hue | - | push | pop |
| 1 hue | add | subtract | multiply |
| 2 hue | divide | mod | not |
| 3 hue | greater | pointer | switch |
| 4 hue | duplicate | roll | STDIN (number) |
| 5 hue | STDIN (char) | STDOUT (number) | STDOUT (char) |

| commands | description |
| --- | --- |
| push | pushes the value of the color block just exited on to the stack |
| pop | pops the top value off the stack, and discards it |
| add | pops the top two values off the stack, adds them, and pushes the result back |
| subtract | pops the top two values off the stack, subtracts the top value from the second top value, and pushes the result back |
| multiply | pops the top two values off the stack, multiplies them, and pushes the result back |
| divide | pops the top two values off the stack, divides the second top value by the top value, and pushes the result back |
| mod | likewise with divide, calculates the modulo |
| not | replaces the top value of the stack with 0 if it is non-zero, and 1 if zero |
| greater | pops the top two values off the stack, and pushes 1 if the second top value is greater than the top value, otherwise 0 |
| pointer | pops the top value off the stack, and rotates the DP clockwise that many times |
| switch | pops the top value off the stack, and toggles the CC that many times |
| duplicate | pushes a copy of the top value onto the stack |
| roll | pops the two values off the stack, the top value defines the number of roll, and the second top value is the depth which the remaining top value gets pushed into |
| in | reads value from STDIN as either a number or character |
| out | pops the top value off the stack and prints it to STDOUT as either a number or character |

## Reference
- [Blog with diagrams](https://ymos-hobby-programing.hatenablog.com/entry/2021/09/01/233312)
