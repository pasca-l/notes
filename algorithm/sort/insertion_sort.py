import random

# inserts a value from the unordered list into the already ordered list
# - cannot be improved by binary-searching the value to the right position,
#   as copying and moving the data consumes more time
# - cannot be improved by linked-list to quickly insert value in position,
#   however binary-search cannot be used for linked-list
def insertion_sort(data):
    for i in range(len(data)):
        temp = data[i]

        # get the end of the sorted data
        j = i - 1
        while (j >= 0) and (data[j] > temp):
            # copy and move the data until insertion, from the end
            # if done from front, the value needed gets overwritten before
            data[j+1] = data[j]
            j -= 1

        # temp gets inserted
        data[j+1] = temp

    return data


def main():
    data = [random.randint(0, 100) for _ in range(10)]

    print(f"Before sort: {data}")
    data = insertion_sort(data)
    print(f"After sort: {data}")


if __name__ == "__main__":
    main()
