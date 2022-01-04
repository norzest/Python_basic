# 10814 나이순 정렬

import sys


def solution():
    n = int(input())

    member = []
    for i in range(n):
        age, name = sys.stdin.readline().split()
        member.append((int(age), name))

    member.sort(key=lambda x: x[0])

    for m in member:
        print(m[0], m[1])


if __name__ == '__main__':
    solution()
