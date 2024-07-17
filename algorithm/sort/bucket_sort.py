import random

# prepares a bucket for each value, and counts the frequency for ordering
def bucket_sort(data):
    result = []
    # number of buckets is relevant to the range of data
    bucket = [0] * 101

    for i in data:
        bucket[i] += 1

    for i in range(len(bucket)):
        result.extend([i for _ in range(bucket[i])])

    return result


def main():
    data = [random.randint(0, 100) for _ in range(10)]

    print(f"Before sort: {data}")
    data = bucket_sort(data)
    print(f"After sort: {data}")


if __name__ == "__main__":
    main()
