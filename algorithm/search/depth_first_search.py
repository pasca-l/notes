import random

# there are three types of order in which depth first search can take:
# preorder, inorder, and postorder (the code below is preorder)
def depth_first_search(tree, value):
    search_indices = [0]
    def search_index(pos):
        for i in tree[pos]["child"]:
            search_indices.append(i)
            search_index(i)

    # go throught the tree in the order of search indices
    for i in search_indices:
        if tree[i]["value"] == value:
            return i
    return None


def main():
    # data in a tree structure where each index holds the indices of its child
    tree_structure = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
                      [13, 14], [], [], [], [], [], [], [], []]
    tree = [
        {"child": i, "value": random.randint(0, 100)} for i in tree_structure
    ]
    value = random.randint(0, 100)
    print(f"Finding {value} from {[i['value'] for i in tree]}.")

    if depth_first_search(tree, value) == None:
        print("Value not found in data.")
    else:
        print("Value found in data.")


if __name__ == "__main__":
    main()
