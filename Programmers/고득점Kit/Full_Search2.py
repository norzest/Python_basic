# 완전탐색 - 소수 찾기

from itertools import permutations


def solution(numbers):
    arr = []

    for i in range(1, len(numbers) + 1):
        arr.append(list(map(''.join, permutations(numbers, i))))

    arr = sum(arr, [])
    arr = list(set(list(map(int, arr))))
    print(arr)
    count = 0
    for number in arr:
        if number > 1:
            for j in range(2, number // 2 + 1):
                if number % j == 0:
                    count += 1
                    break
        else:
            count += 1

    return len(arr) - count


if __name__ == "__main__":
    print(solution("17"))
    print('-------------')
    print(solution("011"))
    print('-------------')