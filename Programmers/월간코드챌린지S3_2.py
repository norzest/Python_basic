# 월간 코드 챌린지 시즌3 - n^2 배열 자르기


def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        answer.append(max(divmod(i, n)) + 1)

    return answer


if __name__ == "__main__":
    print(solution(3, 2, 5))
    print(solution(4, 7, 14))
