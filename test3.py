def floyd(n, data):
    dist = [[999] * n for _ in range(n)]

    for i, j, edge in data:
        dist[i-1][j-1] = edge

    for k in range(n):
        dist[k][k] = 0
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def bfs(graph, start):
    visit = list()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit


def dfs(graph, start):
    visit = list()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit


g = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

d = [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]]

print(bfs(g, 'A'))
print(dfs(g, 'A'))
print(floyd(4, d))
