# reference: https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks

class Stack():
    def __init__(self):
        self.data = []

    def put(self, value):
        self.data.append(value)

    def get(self):
        return self.data.pop()


def main():
    stack = Stack()

    stack.put(3)
    stack.put(5)
    stack.put(2)

    print(stack.get())


if __name__ == "__main__":
    main()
