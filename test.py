# 17219 비밀번호 찾기

from sys import stdin


def solution():
    sr = stdin.readline
    n, m = map(int, sr().split(" "))
    d = dict()

    for _ in range(n):
        site, pwd = sr().split(" ")
        d[site] = pwd.rstrip()

    for _ in range(m):
        site = sr().rstrip()
        print(d[site])


if __name__ == '__main__':
    solution()
