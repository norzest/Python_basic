# 2839 설탕 배달

import sys


def solution():
    N = int(sys.stdin.readline())

    cnt = 0
    while N >= 0:
        if N % 5 == 0:
            cnt += (N // 5)
            print(cnt)
            break
        N -= 3
        cnt += 1
    else:
        print(-1)


if __name__ == '__main__':
    solution()
