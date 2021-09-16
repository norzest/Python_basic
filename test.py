# 월간 코드 챌린지 시즌 3 - 빛의 경로 사이클


def solution(grid):
    def pointer_check():
        if pointer[0] < 0:
            pointer[0] = x_len - 1
        elif pointer[0] >= x_len:
            pointer[0] = 0
        if pointer[1] < 0:
            pointer[1] = y_len - 1
        elif pointer[1] >= y_len:
            pointer[1] = 0

    def pointer_move():
        pointer[0] += move[0]
        pointer[1] += move[1]

    def visit():
        location = grid[pointer[1]][pointer[0]]
        if location == 'L':
            if move[0] == 0:
                move[0], move[1] = move[1], move[0]
            elif move[1] == 0:
                move[0], move[1] = move[1], -move[0]
        if location == 'R':
            if move[0] == 0:
                move[0], move[1] = move[1], -move[0]
            elif move[1] == 0:
                move[0], move[1] = move[1], move[0]

        pointer_move()
        pointer_check()

    answer = []
    grid = [list(g) for g in grid]
    # 가로 길이
    x_len = len(grid[0])
    # 세로 길이
    y_len = len(grid)
    # 현재 위치
    pointer = [0, 0]
    # 처음 이동하는 방향 [상, 하, 좌, 우]
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    # 현재 이동하는 방향
    move = [0, -1]

    for k in range(4):
        move = [dx[k], dy[k]]
        n = 0
        while n < 20:
            print(grid[pointer[1]][pointer[0]], end=" ")
            visit()
            n += 1
        pointer = [0, 0]
        print('')
    return answer


if __name__ == "__main__":
    print(solution(["SL", "LR"]))
    print(solution(["S"]))
    print(solution(["R", "R"]))
