# solves for the greatest common divisor between two natural numbers
def euclidian_algorithm(a, b):
    r = a % b

    while r != 0:
        a, b = b, r
        r = a % b

    return b


def main():
    a, b = 1274, 975

    print(f"Find greatest common divisor (GCD) between: {a}, {b}")
    gcd = euclidian_algorithm(a, b)
    print(f"GCD: {gcd}")


if __name__ == "__main__":
    main()
