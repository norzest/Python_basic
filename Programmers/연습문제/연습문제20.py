# 연습문제 - 정수 제곱근 판별

def solution(n):
    sqrt = n**0.5
    return (int(sqrt)+1)**2 if sqrt % 1 == 0 else -1


if __name__ == "__main__":
    print(solution(121))
    print('-------------')
    print(solution(3))
    print('-------------')
