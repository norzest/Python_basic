# Summer/Winter Coding(~2018) - 소수 만들기

from itertools import combinations
import math


def is_prime_number(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        answer += is_prime_number(sum(i))

    return answer


if __name__ == "__main__":
    print(solution([1, 2, 3, 4]))
    print(solution([1, 2, 7, 6, 4]))


