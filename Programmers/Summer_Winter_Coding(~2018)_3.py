# Summer/Winter Coding(~2018) - 배달

from math import inf
import heapq


def solution(N, road, K):
    answer = 0

    # 이어진 길의 정보를 담은 딕셔너리 생성
    graph = {_: dict() for _ in range(1, N + 1)}
    for r in road:
        temp = r[2]
        if r[1] in graph[r[0]]:
            temp = min(graph[r[0]][r[1]], r[2])
        graph[r[0]].update({r[1]: temp})
        graph[r[1]].update({r[0]: temp})

    # 다익스트라
    # 최단 거리를 담기 위한 딕셔너리 생성
    distances = {node: inf for node in graph}
    # 1번 마을부터 시작으로 설정
    distances[1] = 0
    queue = [[1, 0]]

    while queue:
        # 탐색할 마을, 마을까지의 거리
        cur_destination, cur_distance = heapq.heappop(queue)

        # 탐색할 거리가 기존의 거리보다 길다면 패스
        if distances[cur_destination] < cur_distance:
            continue

        for new_destination, new_distance in graph[cur_destination].items():
            # 해당 마을을 거쳐갈 때의 거리
            distance = cur_distance + new_distance
            # 현재 저장된 거리보다 작으면 갱신
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                # 다음 탐색할 마을과 거리 삽입
                heapq.heappush(queue, [new_destination, distance])

    for d in distances.values():
        if d <= K:
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
    print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))


""" 플로이드 알고리즘 사용
from math import inf


def solution(N, road, K):
    answer = 0

    # 각 마을에서 마을로 갈 때 걸리는 시간
    arr = [[inf] * N for _ in range(N)]
    for r in road:
        temp = min(arr[r[0]-1][r[1]-1], r[2])
        arr[r[0]-1][r[1]-1] = temp
        arr[r[1]-1][r[0]-1] = temp

    # 플로이드 알고리즘
    # 경유지
    for i in range(N):
        arr[i][i] = 0
        # 출발지
        for j in range(N):
            # 목적지
            for k in range(N):
                arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])

    for a in arr[0]:
        if a <= K:
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
    print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))

"""