# 연습문제 - 가장 큰 정사각형 찾기


def solution(board):
    answer = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end='')

        print()

    return answer


if __name__ == "__main__":
    print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
    print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
