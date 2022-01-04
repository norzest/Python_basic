# 11651 좌표 정렬하기 2

import sys


def solution():
    n = int(input())

    location = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        location.append((x, y))

    location.sort(key=lambda a: (a[1], a[0]))

    for loc in location:
        print(loc[0], loc[1])


if __name__ == '__main__':
    solution()
