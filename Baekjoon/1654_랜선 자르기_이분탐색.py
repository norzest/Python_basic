# 1654 랜선 자르기

import sys


def solution():
    k, n = map(int, sys.stdin.readline().split())
    line = []
    for i in range(k):
        line.append(int(sys.stdin.readline()))

    start = 1
    end = max(line)

    while start <= end:
        mid = (start + end) // 2

        cut = sum([ln // mid for ln in line])

        if cut < n:
            end = mid - 1
        else:
            start = mid + 1

    print(end)


if __name__ == '__main__':
    solution()
