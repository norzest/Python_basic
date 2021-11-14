# 연습문제 - 가장 긴 팰린드롬


def solution(s):
    s_len = len(s)
    answer = 0

    for i in range(s_len):
        for j in range(i + 1, s_len + 1):
            temp_len = len(s[i:j])
            if s[i:j] == s[i:j][::-1] and answer < temp_len:
                answer = temp_len
    return answer


if __name__ == "__main__":
    print(solution("abcdcba"))
    print(solution("abacde"))
