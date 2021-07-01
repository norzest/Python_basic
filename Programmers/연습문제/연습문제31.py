# 연습문제 - 124 나라의 숫자


def convert(n, base):
    T = "124"
    q, r = divmod(n-1, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


def solution(n):
    answer = convert(n, 3)
    return answer


if __name__ == "__main__":
    print(1, solution(1))
    print(2, solution(2))
    print(3, solution(3))
    print(4, solution(4))
    print(5, solution(5))
    print(6, solution(6))
    print(7, solution(7))
    print(8, solution(8))
    print(9, solution(9))
    print(10, solution(10))
    print(11, solution(11))
    print(12, solution(12))
