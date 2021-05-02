# 그리디 - 섬 연결하기

def solution(n, costs):
    maximum = float('inf')
    island = [[maximum] * n for i in range(n)]
    for i in costs:  # 인접행렬 생성
        island[i[0]][i[1]] = i[2]
        island[i[1]][i[0]] = i[2]

    visited = [0] * n
    distances = [maximum] * n  # 이 배열이 다 채워졌다 == 다 갈 수 있다
    distances[0] = 0
    for i in range(n):  # 프림 알고리즘
        node = 0
        for j in range(n):  # 방문 안한 섬 확인
            if visited[j] == 0:
                node = j
                break

        for j in range(n):  #
            if visited[j] == 0 and distances[j] < distances[node]:
                node = j

        visited[node] = 1  # 여기로 방문하자

        for j in range(n):
            if island[node][j] != maximum:
                if visited[j] == 0 and island[node][j] < distances[j]:
                    distances[j] = island[node][j]

    return sum(distances)
