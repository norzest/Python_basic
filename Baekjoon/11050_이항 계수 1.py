# 11050 이항 계수 1

import sys


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def solution():
    n, k = map(int, sys.stdin.readline().split(" "))
    print(factorial(n) // (factorial(k) * factorial(n-k)))


if __name__ == '__main__':
    solution()
