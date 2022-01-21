# 1929 소수 구하기

from sys import stdin


def solution():
    m, n = map(int, stdin.readline().split())
    n += 1
    arr = [True] * n

    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            for j in range(i + i, n, i):
                arr[j] = False

    for i in range(m, n):
        if arr[i] and i > 1:
            print(i)


if __name__ == '__main__':
    solution()
