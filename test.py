# 10866 덱

import sys
from collections import deque


def solution():
    n = int(sys.stdin.readline())
    deq = deque()
    for i in range(n):
        order = sys.stdin.readline().split()
        if order[0] == 'push_front':
            deq.appendleft(order[1])
        elif order[0] == 'push_back':
            deq.append(order[1])
        elif order[0] == 'pop_front':
            if not deq:
                print(-1)
            else:
                print(deq.popleft())
        elif order[0] == 'pop_back':
            if not deq:
                print(-1)
            else:
                print(deq.pop())
        elif order[0] == 'size':
            print(len(deq))
        elif order[0] == 'empty':
            if not deq:
                print(1)
            else:
                print(0)
        elif order[0] == 'front':
            if not deq:
                print(-1)
            else:
                print(deq[0])
        elif order[0] == 'back':
            if not deq:
                print(-1)
            else:
                print(deq[-1])


if __name__ == '__main__':
    solution()
