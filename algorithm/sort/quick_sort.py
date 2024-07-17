import random

# picks a random pivot, and classifies into bigger and smaller elements
def quick_sort(data):
    if len(data) <= 1:
        return data

    # let pivot be the leading element
    pivot = data[0]
    left, right, same = [], [], 0

    for i in data:
        if i < pivot:
            # with the above condition, the left array can be written as,
            # left = [i for i in data[1:] if i <= pivot]
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            same += 1

    # recursively process until number of elements is 1
    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] * same + right


def main():
    data = [random.randint(0, 100) for _ in range(10)]

    print(f"Before sort: {data}")
    data = quick_sort(data)
    print(f"After sort: {data}")


if __name__ == "__main__":
    main()
