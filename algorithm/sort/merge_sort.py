import random

# merges disassembled short lists into longer sorted list
def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2

    # recursively divide into smaller lists
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while (i < len(left)) and (j < len(right)):
        # merge the given two list elements in order
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # append all remaining values
    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])

    return result


def main():
    data = [random.randint(0, 100) for _ in range(10)]

    print(f"Before sort: {data}")
    data = merge_sort(data)
    print(f"After sort: {data}")


if __name__ == "__main__":
    main()
