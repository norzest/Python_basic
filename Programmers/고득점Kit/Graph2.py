# 그래프 - 순위 <-- 맞는 것 같은데 틀렸다고 해서 일단 올림..

def solution(n, results):
    graph = [[0] * n for _ in range(n)]

    for w, d in results:
        graph[w-1][d-1] = 1
        graph[d-1][w-1] = -1

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                for a, b in enumerate(graph[j]):
                    if b == 1:
                        graph[i][a] = 1
                        graph[a][i] = -1

    for i in graph:
        print(i)

    answer = 0
    for i in graph:
        if i.count(0) == 1:
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))