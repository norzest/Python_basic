# 월간 코드 챌린지 시즌 3 - 빛의 경로 사이클


def solution(grid):
    # 가로 세로 길이 이상 벗어나면 반대편 가장 끝으로 이동
    def pointer_check():
        if pointer[0] < 0:
            pointer[0] = x_len - 1
        elif pointer[0] >= x_len:
            pointer[0] = 0
        if pointer[1] < 0:
            pointer[1] = y_len - 1
        elif pointer[1] >= y_len:
            pointer[1] = 0

    # 포인터 이동
    def pointer_move():
        pointer[0] += move[0]
        pointer[1] += move[1]

    # 칸 방문
    def visit():
        pointer_move()
        pointer_check()
        
        # 이동 방향 재설정
        location = grid[pointer[1]][pointer[0]]
        if location == 'L':
            if move[0] == 0:
                move[0], move[1] = move[1], move[0]
            elif move[1] == 0:
                move[0], move[1] = move[1], -move[0]
        if location == 'R':
            if move[0] == 0:
                move[0], move[1] = -move[1], move[0]
            elif move[1] == 0:
                move[0], move[1] = move[1], move[0]

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
        # 사이클을 특정하기 위한 첫 위치와 방향
        first = [pointer.copy(), move.copy()]

        n = 1
        while n < 20:
            visit()
            if first == [pointer, move]:
                answer.append(n)
                break
            n += 1
        pointer = [0, 0]

    return answer


if __name__ == "__main__":
    print(solution(["SL", "LR"]))
    print(solution(["S"]))
    print(solution(["R", "R"]))
