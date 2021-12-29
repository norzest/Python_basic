# 2869 달팽이는 올라가고 싶다

import sys


def solution():
    a, b, v = map(int, sys.stdin.readline().split(" "))

    if (v - b) % (a - b) == 0:
        print((v - b) // (a - b))
    else:
        print((v - b) // (a - b) + 1)


if __name__ == '__main__':
    solution()
