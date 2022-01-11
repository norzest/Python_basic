# 10845 큐

import sys


def solution():
    n = int(sys.stdin.readline())
    queue = []
    for i in range(n):
        order = sys.stdin.readline().split()
        if order[0] == 'push':
            queue.append(order[1])
        elif order[0] == 'pop':
            if not queue:
                print(-1)
            else:
                print(queue.pop(0))
        elif order[0] == 'size':
            print(len(queue))
        elif order[0] == 'empty':
            if not queue:
                print(1)
            else:
                print(0)
        elif order[0] == 'front':
            if not queue:
                print(-1)
            else:
                print(queue[0])
        elif order[0] == 'back':
            if not queue:
                print(-1)
            else:
                print(queue[-1])


if __name__ == '__main__':
    solution()
