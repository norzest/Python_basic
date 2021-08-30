# 위클리 챌린지 - 5주차

def solution(word):
    answer = 0
    # word 의 최대 길이
    str_len = 5
    # word 의 남은 칸은 띄어쓰기로 대체
    word = "".join([word, " " * (str_len - len(word))])
    # 각 문자가 나올 경우 더할 숫자
    arr = [
        [0, 1, 782, 1563, 2344, 3125],  # 1 + (625 + 125 + 25 + 5 + 1)n
        [0, 1, 157, 313, 469, 625],  # 1 + (125 + 25 + 5 + 1)n
        [0, 1, 32, 63, 94, 125],  # 1 + (25 + 5 + 1)n
        [0, 1, 7, 13, 19, 25],  # 1 + (5 + 1)n
        [0, 1, 2, 3, 4, 5]
    ]
    # 순서
    seq = [" ", "A", "E", "I", "O", "U"]

    # ex) 첫번째 문자가 E 일 경우 seq[2] 이므로 arr[0][2]를 더한다
    for i in range(str_len):
        answer += arr[i][seq.index(word[i])]

    return answer


if __name__ == "__main__":
    print(solution("AAAAE"))
    print(solution("AAAE"))
    print(solution("I"))
    print(solution("EIO"))
