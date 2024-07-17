# reference: https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues

# also implemented by `import queue`, with `queue.Queue()` for instantiation
# usage with `.put()` and `.get()`
from collections import deque

class Queue:
    def __init__(self):
        # appending and popping items from the beginning of the list is slow,
        # as all other elements needs to be shifted on process
        # deque() provides fast append and pop from both ends
        self.data = deque([])

    def put(self, value):
        self.data.append(value)

    def get(self):
        return self.data.popleft()


def main():
    queue = Queue()

    queue.put(3)
    queue.put(5)
    queue.put(2)

    print(queue.get())


if __name__ == "__main__":
    main()
