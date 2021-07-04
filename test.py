
def solution(maps):
    answer = -1
    n, m = len(maps[0]), len(maps)  # 가로, 세로
    visited = [[0] * n for _ in range(m)]
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]  # 상하좌우
    visited[0][0] = 1
    queue = [(0, 0)]

    while queue:
        x, y = queue.pop(0)

        if x == n - 1 and y == m - 1:
            answer = visited[x][y]
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    return answer


if __name__ == "__main__":
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
