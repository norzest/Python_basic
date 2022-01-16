# 1966 프린터 큐

from sys import stdin


def solution():
    t = int(stdin.readline())

    for _ in range(t):
        n, m = map(int, stdin.readline().split())
        arr = list(map(int, stdin.readline().split()))

        big = max(arr)
        cnt = 0

        while arr:
            if arr[0] >= big:
                arr.pop(0)
                cnt += 1

                if m == 0:
                    print(cnt)
                    break
                else:
                    m -= 1
                big = max(arr)
            else:
                arr.append(arr.pop(0))

                if m == 0:
                    m = len(arr) - 1
                else:
                    m -= 1


if __name__ == '__main__':
    solution()
