# 11723 집합

from sys import stdin


def solution():
    sr = stdin.readline
    m = int(sr())

    s = set()
    for i in range(m):
        cal = sr().split()

        if len(cal) == 1:
            if cal[0] == 'all':
                s = set(range(1, 21))
            elif cal[0] == 'empty':
                s = set()
            continue

        cal[1] = int(cal[1])

        if cal[0] == 'add':
            s.add(cal[1])
        elif cal[0] == 'remove':
            s.discard(cal[1])
        elif cal[0] == 'check':
            print(1 if cal[1] in s else 0)
        elif cal[0] == 'toggle':
            if cal[1] in s:
                s.discard(cal[1])
            else:
                s.add(cal[1])


if __name__ == '__main__':
    solution()
