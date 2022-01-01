# 1018 체스판 다시 칠하기

import sys


def solution():
    n, m = map(int, sys.stdin.readline().split(" "))

    board = [sys.stdin.readline().strip() for i in range(n)]
    answer = []
    for i in range(n - 7):
        for j in range(m - 7):
            a, b = 0, 0

            for x in range(i, i+8):
                for y in range(j, j+8):
                    if(x + y) % 2 == 0:
                        if board[x][y] != 'W':
                            a += 1
                        if board[x][y] != 'B':
                            b += 1
                    else:
                        if board[x][y] != 'B':
                            a += 1
                        if board[x][y] != 'W':
                            b += 1

            answer.append(min(a, b))

    print(min(answer))


if __name__ == '__main__':
    solution()
