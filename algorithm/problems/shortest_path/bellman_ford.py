# updates weight of edges until no more optimization happens
# - can be used for negative weights, under condition of no closed walks
def bellman_ford(edges, num_vertices):
    # initialize cost to every verticies as infinity
    cost = [float("inf") for _ in range(num_vertices)]
    cost[0] = 0

    # keeps track of whether the cost has updated
    changed = True
    while changed:
        changed = False

        for edge in edges:
            # check whether the cost can be minimized
            if cost[edge["end"]] > cost[edge["start"]] + edge["cost"]:
                cost[edge["end"]] = cost[edge["start"]] + edge["cost"]
                changed = True

    return cost


def main():
    edges = [
        {"start": 0, "end": 1, "cost": 4},
        {"start": 0, "end": 2, "cost": 3},
        {"start": 1, "end": 2, "cost": 1},
        {"start": 1, "end": 3, "cost": 1},
        {"start": 1, "end": 4, "cost": 5},
        {"start": 2, "end": 5, "cost": 2},
        {"start": 3, "end": 4, "cost": 3},
        {"start": 4, "end": 6, "cost": 2},
        {"start": 5, "end": 4, "cost": 1},
        {"start": 5, "end": 6, "cost": 4},
    ]
    num_vertices = 7

    cost = bellman_ford(edges, num_vertices)
    print(f"Cost for each verticies: {cost}")


if __name__ == "__main__":
    main()
