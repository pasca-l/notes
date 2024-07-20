class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)

        # if it is the first data to append
        if self.is_empty():
            self.head = new_node
            return

        # go to the last node
        current = self.head
        while current.next:
            current = current.next

        # append the new node to the end
        current.next = new_node

    def remove(self, data):
        if self.is_empty():
            return

        # if the data to be removed is found at the beginning
        if self.head.data == data:
            self.head = self.head.next

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        # if the data to be removed is found, and not at end
        if current.next:
            current.next = current.next.next

    def display(self):
        elements = []
        current = self.head

        while current:
            elements.append(current.data)
            current = current.next

        print(" -> ".join(map(str, elements)))


def main():
    linked_list = LinkedList()

    linked_list.append(3)
    linked_list.append(5)
    linked_list.append(2)

    linked_list.display()


if __name__ == "__main__":
    main()
