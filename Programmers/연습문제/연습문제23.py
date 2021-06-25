# 연습문제 - 최대공약수와 최소공배수

from math import gcd


def solution(n, m):
    nm_gcd = gcd(n, m)
    return [nm_gcd, (n * m) // nm_gcd]


if __name__ == "__main__":
    print(solution(3, 12))
    print('-------------')
    print(solution(2, 5))
    print('-------------')
