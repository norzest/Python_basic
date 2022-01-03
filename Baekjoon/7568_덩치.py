# 7568 덩치

import sys


def solution():
    n = int(input())

    people = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        people.append((x, y))

    bigger = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
                bigger[j] += 1
            elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                bigger[i] += 1

    for b in bigger:
        print(b, end=' ')


if __name__ == '__main__':
    solution()
