# Uniform Cost Search
from collections import defaultdict
from queue import PriorityQueue

#cost
def uniform_cost_search(goal, start):

    global graph, cost
    answer = []

    queue = []

    for i in range(len(goal)):
        answer.append(10**8)

    queue.append([0, start])

    visited = {}

    count = 0

    while (len(queue) > 0):

        queue = sorted(queue)
        p = queue[-1]

        del queue[-1]

        p[0] *= -1

        if (p[1] in goal):

            index = goal.index(p[1])

            if (answer[index] == 10**8):
                count += 1

            if (answer[index] > p[0]):
                answer[index] = p[0]

            del queue[-1]

            queue = sorted(queue)
            if (count == len(goal)):
                return answer

        if (p[1] not in visited):
            for i in range(len(graph[p[1]])):

                queue.append(
                    [(p[0] + cost[(p[1], graph[p[1]][i])]) * -1, graph[p[1]][i]])

        visited[p[1]] = 1
        # print(visited)

    return answer

# path
class UCS_Graph:
    def __init__(self, directed):

        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight):

        if self.directed:
            value = (weight, v)
            self.graph[u].append(value)
        else:
            value = (weight, v)
            self.graph[u].append(value)
            value = (weight, u)
            self.graph[v].append(value)

    def ucs(self, current_node, goal_node):

        count = 0
        i = 0
        visited = []
        path = []
        queue = PriorityQueue()
        queue.put((0, current_node))

        while not queue.empty():
            item = queue.get()
            current_node = item[1]

            if current_node == goal_node:
                # print(current_node)
                path.append(current_node)
                count+=1
                queue.queue.clear()
            else:
                if current_node in visited:
                    continue

                # print(current_node)
                path.append(current_node)
                count+=1
                visited.append(current_node)

                for neighbour in self.graph[current_node]:
                    queue.put((neighbour[0], neighbour[1]))

        print(count)

        for j in range(len(path)):
            print(path[j])

        print(len(visited))


if __name__ == '__main__':

    V, E = input().split()
    V = int(V)
    E = int(E)

    graph, cost = [[] for i in range(V)], {}

    g = UCS_Graph(False)
    g.graph = defaultdict(list)

    for i in range(E):
        x, y, w = input().split()
        x = int(x)
        y = int(y)
        w = int(w)
        g.add_edge(x, y, w)
        x = x-1
        y = y-1
        graph[x].append(y)
        cost[(x, y)] = w

    goal = []

    S, D = input().split()
    S = int(S)
    D = int(D)
    Ss = S-1
    Dd = D-1

    goal.append(Dd)

    answer = uniform_cost_search(goal, Ss)
    print(answer[0])

    g.graph

    g.ucs(S, D)
