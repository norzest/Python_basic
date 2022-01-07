# 2164 카드2

from collections import deque


def solution():
    n = int(input())
    if n == 1:
        print(1)
        return

    cards = deque([i for i in range(1, n+1)])
    while True:
        cards.popleft()
        n -= 1
        if n == 1:
            print(cards[0])
            break
        cards.append(cards.popleft())


if __name__ == '__main__':
    solution()
