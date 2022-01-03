# 2609 최대공약수와 최소공배수

from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


def solution():
    a, b = map(int, input().split())
    print(gcd(a, b))
    print(lcm(a, b))


if __name__ == '__main__':
    solution()
