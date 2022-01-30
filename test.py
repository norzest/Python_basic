# 1764 듣보잡

from sys import stdin


def solution():
    sr = stdin.readline
    n, m = map(int, sr().split(" "))
    dd = set()
    for i in range(n):
        dd.add(sr().rstrip())

    cnt = 0
    bd = set()
    for i in range(m):
        temp = sr().rstrip()
        if temp in dd:
            bd.add(temp)
            cnt += 1

    print(cnt)
    for b in sorted(bd):
        print(b)


if __name__ == '__main__':
    solution()
