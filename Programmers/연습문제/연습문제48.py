# 연습문제 - 최고의 집합


def solution(n, s):
    if s < n:
        return [-1]

    a = s // n
    b = s % n

    answer = []
    for i in range(n):
        if b != 0:
            answer.append(a + 1)
            b -= 1
        else:
            answer.append(a)

    return answer[::-1]


if __name__ == "__main__":
    print(solution(2, 9))
    print(solution(4, 7))
    print(solution(2, 8))
