# 연습문제 - 문자열 내 마음대로 정렬하기

def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))


if __name__ == "__main__":
    print(solution(["sun", "bed", "car"], 1))
    print('-------------')
    print(solution(	["abce", "abcd", "cdx"], 2))
    print('-------------')
