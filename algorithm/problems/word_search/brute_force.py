# finds pattern within a text by sliding the pattern by one letter until match
def brute_force(text, pattern):
    for i in range(len(text)):
        match = True

        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                match = False
                break

        if match:
            return i

    return None


def main():
    text = list("HELLO WORLD!")
    pattern = list("WORLD")

    index = brute_force(text, pattern)
    print(f"Found pattern at index: {index}")


if __name__ == "__main__":
    main()
