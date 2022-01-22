# 18111 마인크래프트

from sys import stdin


def solution():
    n, m, b = map(int, stdin.readline().split())
    height = dict()
    for i in range(n):
        for j in list(map(int, stdin.readline().split())):
            if j not in height.keys():
                height[j] = 1
            else:
                height[j] += 1

    print(height)




if __name__ == '__main__':
    solution()
