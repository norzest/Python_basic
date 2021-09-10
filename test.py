# 월간 코드 챌린지 시즌 1 - 이진 변환 반복하기

def solution(s):
    answer = [0, 0]

    while s != "1":
        answer[0] += 1
        answer[1] += s.count("0")

        s = s.replace("0", "")
        s_len = len(s)
        s = format(s_len, 'b')

    return answer


if __name__ == "__main__":
    print(solution("110010101001"))
    print(solution("01110"))
    print(solution("1111111"))
