import random

def linear_search(data, value):
    print(f"Finding {value} from {data}.")
    for i in range(len(data)):
        if data[i] == value:
            return i
    return None


def main():
    data = [random.randint(0, 100) for _ in range(10)]
    value = random.randint(0, 100)

    if linear_search(data, value) == None:
        print("Value not found in data.")
    else:
        print("Value found in data.")


if __name__ == "__main__":
    main()
