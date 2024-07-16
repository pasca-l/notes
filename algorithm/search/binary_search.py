import random

def binary_search(data, value):
    # initialize boundary to search from
    left = 0
    right = len(data) - 1

    while left <= right:
        # find center of search area
        mid = (left + right) // 2

        # move boundary according to mid value comparison
        if data[mid] < value:
            left = mid + 1
        elif data[mid] > value:
            right = mid - 1

        # equivalent to data[mid] == value
        else:
            return mid

    return None


def main():
    data = [random.randint(0, 100) for _ in range(10)]
    # data must be sorted beforehand
    data.sort()
    value = random.randint(0, 100)
    print(f"Finding {value} from {data}.")

    if binary_search(data, value) == None:
        print("Value not found in data.")
    else:
        print("Value found in data.")


if __name__ == "__main__":
    main()
