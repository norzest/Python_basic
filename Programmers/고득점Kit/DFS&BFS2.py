# DFS/BFS - 네트워크

def solution(n, computers):
    answer = 0
    visited = [0] * n
    stack = [0]
    graph = []

    while True:
        while stack:
            temp = stack.pop()
            visited[temp] = 1
            graph.append(temp)

            for i in range(len(computers[temp])):
                if computers[temp][i] == 1 and visited[i] == 0 and temp != i:
                    stack.append(i)

        answer += 1

        try:
            stack = [visited.index(0)]
        except ValueError:
            break

    return answer


if __name__ == "__main__":
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print('-------------')
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
    print('-------------')