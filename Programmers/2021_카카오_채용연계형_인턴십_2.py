# 2021 카카오 채용연계형 인턴샙 - 숫자 문자열과 영단어


def solution(s):
    match = [
        ['zero', '0'], ['one', '1'], ['two', '2'],
        ['three', '3'], ['four', '4'], ['five', '5'],
        ['six', '6'], ['seven', '7'], ['eight', '8'], ['nine', '9']
    ]

    for i in range(10):
        s = s.replace(match[i][0], match[i][1])

    return s


if __name__ == "__main__":
    print(solution("one4seveneight"))
    print(solution("23four5six7"))
    print(solution("2three45sixseven"))
    print(solution("123"))
