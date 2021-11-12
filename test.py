# 연습문제 - 가장 긴 팰린드롬


def solution(s):
    answer = len(s)

    for i in range(answer):
        answer -= 1

    return answer


if __name__ == "__main__":
    print(solution("abcdcba"))
    print(solution("abacde"))
