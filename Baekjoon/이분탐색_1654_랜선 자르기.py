# 1654 랜선 자르기

from sys import stdin


def solution():
    k, n = map(int, stdin.readline().split())
    line = list(map(int, stdin.readlines()))

    answer = 0
    start = 1
    end = sum(line) // n

    while start <= end:
        mid = (start + end) // 2

        cut = sum([ln // mid for ln in line])

        if cut < n:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid

    print(answer)


if __name__ == '__main__':
    solution()
