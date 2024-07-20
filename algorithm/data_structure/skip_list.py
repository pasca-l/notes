import random

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.forward = [] # list of forward pointers


class SkipList:
    def __init__(self, max_level=16, p=0.5):
        self.max_level = 16
        self.p = p
        self.head = Node(None, None)
        self.head.forward = [None] * max_level
        self.level = 0

    def random_level(self):
        level = 0
        while random.random() < self.p and level < self.max_level - 1:
            level += 1
        return level

    def insert(self, key, value):
        update = [None] * self.max_level
        current = self.head

        # from top level, finding position to insert the value according to key
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        # forward reference to the next position at level 0
        current = current.forward[0]

        # insertion happens at the end of the list,
        # or between update[0] and current node
        if current is None or current.key != key:
            level = self.random_level()

            # add headers for levels above
            if level > self.level:
                for i in range(self.level + 1, level + 1):
                    update[i] = self.head
                self.level = level

            new_node = Node(key, value)
            for i in range(level + 1):
                new_node.forward.append(update[i].forward[i])
                update[i].forward[i] = new_node

    def delete(self, key):
        update = [None] * self.max_level
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]

        if current and current.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and self.head.forward[self.level] is None:
                self.level -= 1

    def search(self, key):
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        current = current.forward[0]

        if current and current.key == key:
            return current.value

        return None

    def display(self):
        for level in range(self.level, -1, -1):
            print(f"Level {level}: ", end="")

            node = self.head.forward[level]
            while node:
                print(f"({node.key}, {node.value}) ", end="")
                node = node.forward[level]

            # print for new line
            print("")


def main():
    skip_list = SkipList()

    skip_list.insert(3, "three")
    skip_list.insert(5, "five")
    skip_list.insert(2, "two")

    skip_list.display()


if __name__ == "__main__":
    main()
