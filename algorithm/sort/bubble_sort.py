import random

# bubbles up the largest value to the end by switching positions
# - can be improved by stopping early, if no swap has happened
def bubble_sort(data):
    for i in range(len(data)):

        # until the end of the unsorted data
        for j in range(len(data) - i - 1):
            # swaps the position of the data, according to its value
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    return data


def main():
    data = [random.randint(0, 100) for _ in range(10)]

    print(f"Before sort: {data}")
    data = bubble_sort(data)
    print(f"After sort: {data}")


if __name__ == "__main__":
    main()
