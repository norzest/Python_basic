# 찾아라 프로그래밍 마에스트로 - 게임 맵 최단거리

def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우 방향 이동

    # BFS 경로 탐색
    queue = [(0, 0)]
    visited[0][0] = 1

    while queue:
        x, y = queue.pop(0)

        if x == n - 1 and y == m - 1:
            # 최종 경로 도착
            answer = visited[x][y]
            break

        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 이동 가능한 경로이면서 아직 방문하지 않은 경우
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    return answer


if __name__ == "__main__":
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
