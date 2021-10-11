# 월간 코드 챌린지 시즌3 - 없는 숫자 더하기


def solution(numbers):
    return sum([i for i in range(10) if i not in numbers])


if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
    print(solution([5, 8, 4, 0, 6, 7, 9]))
