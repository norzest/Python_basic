# 연습문제 - 문자열 내 p와 y의 개수

def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')


if __name__ == "__main__":
    print(solution("pPoooyY"))
    print('-------------')
    print(solution("Pyy"))
    print('-------------')
