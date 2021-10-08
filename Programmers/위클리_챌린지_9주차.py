def make_dict(wires):
    graph = dict()

    for wire in wires:
        if wire[0] not in graph:
            graph[wire[0]] = [wire[1]]
        else:
            graph[wire[0]].append(wire[1])

        if wire[1] not in graph:
            graph[wire[1]] = [wire[0]]
        else:
            graph[wire[1]].append(wire[0])

    return graph


def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)
            if node in graph:
                queue.extend(graph[node])

    return visited


def solution(n, wires):
    min_diff = 999

    for i in range(n):
        graph = make_dict(wires[:i] + wires[i+1:])
        num = len(bfs(graph, 1))
        diff = max(n - num, num) - min(n - num, num)
        min_diff = diff if diff <= min_diff else min_diff

    return min_diff


if __name__ == "__main__":
    print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
    print(solution(4, [[1, 2], [2, 3], [3, 4]]))
    print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
