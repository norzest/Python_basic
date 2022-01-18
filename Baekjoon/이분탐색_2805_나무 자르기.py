# 2805 나무 자르기

from sys import stdin


def solution():
    n, m = map(int, stdin.readline().split())
    trees = list(map(int, stdin.readline().split()))

    start = 1
    end = max(trees)

    while start <= end:
        mid = (start + end) // 2

        cut = [tree - mid for tree in trees if tree > mid]

        if sum(cut) >= m:
            start = mid + 1
        else:
            end = mid - 1

    print(end)


if __name__ == '__main__':
    solution()
