def reverse_polish_notation(expression):
    stack = []

    for i in expression.split(" "):
        if i == "+":
            b, a = stack.pop(), stack.pop()
            stack.append(a + b)
        elif i == "-":
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)
        elif i == "*":
            b, a = stack.pop(), stack.pop()
            stack.append(a * b)
        elif i == "/":
            b, a = stack.pop(), stack.pop()
            stack.append(a // b)
        else:
            stack.append(int(i))

    return stack[0]


def main():
    expression = "4 6 2 + * 3 1 - 5 * -"

    print(f"Expression to calculate: {expression}")
    result = reverse_polish_notation(expression)
    print(f"Calculated result: {result}")


if __name__ == "__main__":
    main()
