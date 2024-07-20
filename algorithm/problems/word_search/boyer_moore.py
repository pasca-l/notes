# fixes problem with brute force, which slides by only one letter on unmatch,
# - KMP (Knuth–Morris–Pratt) algorithm is theoretically faster
def boyer_moore(text, pattern):
    # create a list of letters to skip beforehand
    skip = {}
    for i in range(len(pattern) - 1):
        skip[pattern[i]] = len(pattern) - i - 1

    i = len(pattern) - 1
    while i < len(text):
        match = True

        for j in range(len(pattern)):
            # checks match from the end
            if text[i-j] != pattern[len(pattern)-j-1]:
                match = False
                break

        if match:
            return i - len(pattern) + 1

        # skip text according to previously calculated letter counts
        if text[i] in skip:
            i += skip[text[i]]
        else:
            i += len(pattern)

    return None


def main():
    text = list("HELLO WORLD!")
    pattern = list("WORLD")

    index = boyer_moore(text, pattern)
    print(f"Found pattern at index: {index}")


if __name__ == "__main__":
    main()
