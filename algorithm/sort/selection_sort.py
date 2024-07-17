import random

# selects the minimum value from the unordered list and moves it to the front
def selection_sort(data):
    for i in range(len(data)):
        min = i

        # find index of minimum value
        for j in range(i + 1, len(data)):
            if data[min] > data[j]:
                min = j

        # for every loop the minumum value is set
        data[i], data[min] = data[min], data[i]

    return data


def main():
    data = [random.randint(0, 100) for _ in range(10)]

    print(f"Before sort: {data}")
    data = selection_sort(data)
    print(f"After sort: {data}")


if __name__ == "__main__":
    main()
