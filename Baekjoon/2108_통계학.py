# 2108 통계학

import sys


def solution():
    n = int(sys.stdin.readline())

    arr = []
    for i in range(n):
        arr.append(int(sys.stdin.readline()))
    arr.sort()

    # 산술평균
    print(round(sum(arr) / n))
    # 중앙값
    print(arr[n//2])
    # 최빈값
    dic = {i: 0 for i in arr}
    for ar in arr:
        dic[ar] += 1
    temp = [a for a, b in dic.items() if max(dic.values()) == b]
    if len(temp) == 1:
        print(temp[0])
    else:
        temp.sort()
        print(temp[1])
    # 범위
    print(max(arr) - min(arr))


if __name__ == '__main__':
    solution()
