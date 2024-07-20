# selects the least costly path from one vertex to another
# - cannot be used for negative weights
def dijkstra(edges):
    # initialize cost to every verticies as infinity
    cost = [float("inf") for _ in range(len(edges))]
    cost[0] = 0

    # this list can be improved by using a heap structure,
    # to omit searching for minimum vertex
    vertices = [i for i in range(len(edges))]

    while len(vertices) > 0:
        # find the minimum cost within vertices
        min = vertices[0]
        for i in vertices:
            if cost[i] < cost[min]:
                min = i

        min_v = vertices.pop(vertices.index(min))
        # looks through the edges from the minimum cost vertex
        for edge in edges[min_v]:
            if cost[edge["end"]] > cost[min_v] + edge["cost"]:
                cost[edge["end"]] = cost[min_v] + edge["cost"]

    return cost


def main():
    # edges grouped by start values
    edges = [
        [
            {"end": 1, "cost": 4},
            {"end": 2, "cost": 3},
        ],
        [
            {"end": 2, "cost": 1},
            {"end": 3, "cost": 1},
            {"end": 4, "cost": 5},
        ],
        [
            {"end": 5, "cost": 2},
        ],
        [
            {"end": 4, "cost": 3},
        ],
        [
            {"end": 6, "cost": 2},
        ],
        [
            {"end": 4, "cost": 1},
            {"end": 6, "cost": 4},
        ],
        [],
    ]

    cost = dijkstra(edges)
    print(f"Cost for each verticies: {cost}")


if __name__ == "__main__":
    main()
