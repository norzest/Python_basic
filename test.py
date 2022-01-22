# 18111 마인크래프트

from sys import stdin


def solution():
    n, m, b = map(int, stdin.readline().split())
    height = [list(map(int, stdin.readline().split())) for _ in range(n)]

    answer = [99999999999999999999, 0]
    for i in range(257):
        remove_block = 0
        add_block = 0
        for j in range(n):
            for k in range(m):
                if height[j][k] < i:
                    add_block += i - height[j][k]
                else:
                    remove_block += height[j][k] - i

        if remove_block + b >= add_block:
            time = 2 * remove_block + add_block
            if answer[0] >= time:
                answer[0] = time
                answer[1] = i

    print(answer[0], answer[1])


if __name__ == '__main__':
    solution()
