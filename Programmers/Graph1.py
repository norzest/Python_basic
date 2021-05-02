# 그래프 - 가장 먼 노드

def solution(n, edge):
    answer = 0
    adj = [[] for _ in range(n)]
    distance = [0 for _ in range(n)]

    for i in range(len(edge)):
        a, b = map(int, edge[i])
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)

    queue = [0]
    temp = 0
    while queue:
        for i in range(len(queue)):
            n = queue.pop(0)

            if distance[n] == 0:
                distance[n] = temp

                for j in adj[n]:
                    queue.append(j)
        temp += 1

    distance[0] = 0
    temp = max(distance)

    for i in distance:
        if i == temp:
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
    print('-------------')
