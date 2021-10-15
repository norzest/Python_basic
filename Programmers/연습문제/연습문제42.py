# 연습문제 - N개의 최소공배수

from math import gcd


def solution(arr):
    answer = arr[0]
    for a in arr[1:]:
        answer = answer * a // gcd(answer, a)
    return answer


if __name__ == "__main__":
    print(solution([2, 6, 8, 14]))
    print(solution([1, 2, 3]))
