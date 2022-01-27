# 1620 나는야 포켓몬 마스터 이다솜

from sys import stdin


def solution():
    sr = stdin.readline
    n, m = map(int, sr().split())

    l = list()
    d = dict()
    for i in range(n):
        temp = sr().rstrip()
        l.append(temp)
        d[temp] = i + 1

    for i in range(m):
        p = sr().rstrip()
        if p.isalpha():
            print(d[p])
        else:
            print(l[int(p) - 1])


if __name__ == '__main__':
    solution()
