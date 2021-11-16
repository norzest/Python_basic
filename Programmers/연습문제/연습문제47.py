# 연습문제 - 줄 서는 법

import math


def solution(n, k):
    answer = []
    num = [_ for _ in range(1, n + 1)]

    while n > 0:
        temp = math.factorial(n - 1)
        index = k // temp
        k = k % temp

        if k == 0:
            answer.append(num.pop(index-1))
        else:
            answer.append(num.pop(index))

        n -= 1

    return answer


if __name__ == "__main__":
    print(solution(3, 5))
