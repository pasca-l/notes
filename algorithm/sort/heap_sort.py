# also implemented by `import heapq`, with `heapq.heapify(list)`,
# usage with `heapq.heappop(list)` for getting heap sorted data
import random

# sorts the heap structure
def heap_sort(data):
    data = create_heap_struct(data)

    for i in range(len(data), 0, -1):
        # maximum value at root is switched to the end as sorted
        data[i-1], data[0] = data[0], data[i-1]
        j = 0

        while (
            # there is a left child, and its value is bigger
            (2*j+1 < i-1) and (data[j] < data[2*j+1]) \
            # there is a right child, and its value is bigger
            or ((2*j+2 < i-1) and (data[j] < data[2*j+2]))
        ):
            # if the left child is bigger than the right child
            if (2*j+2 == i-1) or (data[2*j+1] > data[2*j+2]):
                # exchange values with the left child, and move to it
                data[j], data[2*j+1] = data[2*j+1], data[j]
                j = 2*j+1
            # the other way around
            else:
                data[j], data[2*j+2] = data[2*j+2], data[j]
                j = 2*j+2

    return data


# makes data into heap structure (max heap)
# converting heap structure into a list format is done as following:
# - from parent index i, the two child index are, 2i+1 (left) and 2i+2 (right)
# - from child index j, the parent index is (j-1)//2
def create_heap_struct(data):
    for i in range(len(data)):
        j = i

        # comparing the current and the parent value,
        # so that parent value is larger, than that of its child
        while (j > 0) and (data[(j-1)//2] < data[j]):
            # exchange value with the parent
            data[(j-1)//2], data[j] = data[j], data[(j-1)//2]
            # move to parent
            j = (j - 1) // 2

    return data


def main():
    data = [random.randint(0, 100) for _ in range(10)]

    print(f"Before sort: {data}")
    data = heap_sort(data)
    print(f"After sort: {data}")


if __name__ == "__main__":
    main()
