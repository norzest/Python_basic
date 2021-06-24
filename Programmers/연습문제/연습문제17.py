# 연습문제 - 자릿수 더하기

def solution(n):
    return sum(map(int, str(n)))


if __name__ == "__main__":
    print(solution(123))
    print('-------------')
    print(solution(987))
    print('-------------')
