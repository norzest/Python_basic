# 10816 숫자 카드 2

import sys


def solution():
    n = int(sys.stdin.readline())
    have = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    cards = list(map(int, sys.stdin.readline().split()))
    cnt = dict()
    for card in cards:
        cnt[card] = 0
    for h in have:
        if h in cnt.keys():
            cnt[h] += 1

    for card in cards:
        print(cnt[card], end=' ')


if __name__ == '__main__':
    solution()
