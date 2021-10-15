# 연습문제 - JadenCase 문자열 만들기


def solution(s):
    s = s.split(' ')
    s = [_.capitalize() for _ in s]
    return ' '.join(s)


if __name__ == "__main__":
    print(solution("3people unFollowed me"))
    print(solution("for the last week"))
