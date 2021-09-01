# Summer/Winter Coding(~2018) - 배달

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
