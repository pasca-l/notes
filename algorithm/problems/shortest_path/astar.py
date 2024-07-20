import heapq

# improved dijkstra by omitting paths that furthen from the goal
# to decide whether the path is getting near or further,
# estimated cost is calculated by such manhattan distance
# - estimation should be somewhat accurate to find the shortest path
# - estimated cost should be static
def astar(edges, goal):
    # initialize cost to every verticies as infinity
    cost = [float("inf") for _ in range(len(edges))]
    cost[0] = 0

    # use heap structure
    q = []
    heapq.heappush(q, [0, [0]])

    while len(q) > 0:
        _, node = heapq.heappop(q)
        last = node[-1]

        # if reached the goal node
        if last == goal:
            return node

        for edge in edges[last]["paths"]:
            if cost[edge["end"]] > cost[last] + edge["cost"]:
                cost[edge["end"]] = cost[last] + edge["cost"]
                heapq.heappush(
                    q,
                    [
                        cost[last] + edge["cost"] + edges[edge["end"]]["est"],
                        node + [edge["end"]]
                    ]
                )

    return cost


def main():
    # edges grouped by start values, with estimated cost
    edges = [
        {
            "est": 4,
            "paths": [
                {"end": 1, "cost": 4},
                {"end": 2, "cost": 3},
            ]
        },
        {
            "est": 4,
            "paths": [
                {"end": 2, "cost": 1},
                {"end": 3, "cost": 1},
                {"end": 4, "cost": 5},
            ],
        },
        {
            "est": 4,
            "paths": [
                {"end": 5, "cost": 2},
            ],
        },
        {
            "est": 2,
            "paths": [
                {"end": 4, "cost": 3},
            ],
        },
        {
            "est": 2,
            "paths": [
                {"end": 6, "cost": 2},
            ],
        },
        {
            "est": 2,
            "paths": [
                {"end": 4, "cost": 1},
                {"end": 6, "cost": 4},
            ],
        },
        {
            "est": 0,
            "paths": [],
        },
    ]

    # set last node as goal
    cost = astar(edges, len(edges) - 1)
    print(f"Cost for each verticies: {cost}")


if __name__ == "__main__":
    main()
