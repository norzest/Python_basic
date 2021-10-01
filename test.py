# 연습문제 - 가장 큰 정사각형 찾기


def solution(board):
    # 가장 큰 정사각형의 변의 길이
    max_num = 0
    x = len(board)
    y = len(board[0])
    if x <= 1 or y <= 1:
        return 1

    for i in range(1, x):
        for j in range(1, y):
            if board[i][j] >= 1:
                # 현재 칸의 위, 왼쪽, 왼쪽 위 중 최소값
                min_num = min(board[i-1][j], board[i][j-1], board[i-1][j-1])
                # min_num + 1 을 현재 칸에 대입
                board[i][j] = min_num + 1
                max_num = max(min_num + 1, max_num)

    return max_num * max_num


if __name__ == "__main__":
    print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
    print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
