# 1920 수 찾기

import sys


def solution():
    n = int(input())
    a = list(map(int, sys.stdin.readline().split()))
    m = int(input())
    b = list(map(int, sys.stdin.readline().split()))

    a.sort()
    for num in b:
        start = 0
        end = n - 1

        # 이진 탐색
        while start <= end:
            mid = (start + end) // 2

            if a[mid] == num:
                print(1)
                break
            elif a[mid] < num:
                start = mid + 1
            else:
                end = mid - 1
        else:
            print(0)


if __name__ == '__main__':
    solution()
