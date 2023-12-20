def is_valid_coloring(graph, coloring, k):
    for i in range(len(graph)):
        for j in graph[i]:
            if coloring[i] == coloring[j]:
                return False
    return True


def map_coloring(graph, k):
    coloring = [0] * len(graph)

    coloring[0] = 0

    is_possible = True

    for i in range(1, len(graph)):
        available_colors = [True] * k
        for j in graph[i]:
            if coloring[j] != -1:
                available_colors[coloring[j]] = False
        color = -1
        for j in range(k):
            if available_colors[j]:
                color = j
                break
        if color == -1:
            is_possible = False
            break
        coloring[i] = color

    if is_possible:
        for c in coloring:
            print(c)
    else:
        print("NO")


V, E = map(int, input().split()) 

graph = [[0 for column in range(V)]  
        for row in range(V)] 

for i in range(E): 
    u, v = map(int, input().split()) 
    graph[u-1][v-1] = 1
    graph[v-1][u-1] = 1

K = int(input())

map_coloring(graph, K)
