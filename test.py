# 1676 팩토리얼 0의 개수

from sys import stdin


def solution():
    sr = stdin.readline()
    n = int(sr)
    a = 1
    for i in range(1, n + 1):
        a = a * i
    a = str(a)

    cnt = 0
    for i in reversed(range(0, len(a))):
        if a[i] == '0':
            cnt += 1
        else:
            print(cnt)
            break


if __name__ == '__main__':
    solution()
