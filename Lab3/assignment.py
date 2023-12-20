# Assignment 3

WHITE = 0
GREY = 1
BLACK = 2
has_cycle = False
colors = []
dfs_costs = []
traversed = []
parents = []


def undirected_graph(verticies, edges):
    costs = [[] for _ in range(verticies + 1)]
    grph = [[] for _ in range(verticies + 1)]

    for i in range(edges):
        start, end, dist = map(int, input().split())
        grph[start].append(end)
        costs[start].append(dist)
        if start != end:
            grph[end].append(start)
            costs[end].append(dist)

    return [grph, costs]


def initializing(x):
    global colors, dfs_costs, traversed, parents
    colors = [-1]*(x)
    dfs_costs = [0 for _ in range(x)]
    traversed = [0 for _ in range(x)]
    parents = [-1 for _ in range(x)]


def print_path(dest, src):
    unreachable = False
    path = []

    while dest != src:
        if dest == -1:
            unreachable = True
            break

        path.append(dest)
        dest = parents[dest]

    if not unreachable:
        print(len(path) + 1)
        print(src)

        while len(path) != 0:
            top = path[-1]
            path.pop()
            print(top)
    else:
        print(-1)


def DFS(graph, costs, source, total_cost):
    global colors, dfs_costs, traversed, parents, has_cycle
    vertices_traversed = 0
    colors[source] = GREY
    dfs_costs[source] += total_cost
    traversed[source] = vertices_traversed
    vertices_traversed += 1

    i = 0
    while i < len(graph[source]):
        neighbour = graph[source][i]
        if colors[neighbour] == WHITE:
            parents[neighbour] = source
            next = dfs_costs[source] + costs[source][i]
            DFS(graph, costs, neighbour, next)
        elif colors[neighbour] == GREY:
            has_cycle = True

        i += 1

    colors[source] = BLACK

    return


if __name__ == '__main__':
    vertices, edges = map(int, input().split())
    graph, costs = undirected_graph(vertices, edges)

    initializing(vertices+1)

    src, des, Vertices, edges = map(int, input().split())
    DFS(graph, costs, src, 0)

    print(dfs_costs[des])
    print_path(des, src)
    print(traversed[des])