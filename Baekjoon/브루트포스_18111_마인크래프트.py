# 18111 마인크래프트

from sys import stdin


def solution():
    n, m, b = map(int, stdin.readline().split())

    # 현재 블록들의 높이와 그 갯수
    height = dict()
    for i in range(n):
        for j in map(int, stdin.readline().split()):
            if j in height:
                height[j] += 1
            else:
                height[j] = 1

    # 총 블록 개수
    total_block = 0
    for h in height.keys():
        total_block += h * height[h]

    # 가장 높은 높이
    higher = 0
    # 최소 시간
    sec = 9999999999999999999999

    for i in range(257):
        # 만약 자신이 가질 수 있는 블록 개수가 해당 높이의 n * m 칸 보다 많을경우
        if n * m * i <= total_block + b:

            # 그렇게 만드는데 걸리는 시간
            temp = 0
            for block in height:
                if block < i:
                    temp += (i - block) * height[block]
                elif block > i:
                    temp += (block - i) * 2 * height[block]

            if temp <= sec:
                sec = temp
                higher = i

    print(sec, higher)


if __name__ == '__main__':
    solution()
