# 월간 코드 챌린지 시즌3 - n^2 배열 자르기


def solution(n, left, right):
    answer = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j >= i:
                answer.append(j)
            else:
                answer.append(i)

    return answer[left:right+1]


if __name__ == "__main__":
    print(solution(3, 2, 5))
    print(solution(4, 7, 14))
