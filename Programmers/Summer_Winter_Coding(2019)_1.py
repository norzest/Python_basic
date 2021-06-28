# Summer/Winter Coding(2019) - 멀쩡한 사각형

from math import gcd


def solution(w, h):
    return (w * h) - (w + h - gcd(w, h))


if __name__ == "__main__":
    print(solution(3, 5))
    print('----------------')
    print(solution(4, 5))
    print('----------------')
    print(solution(1, 7))
    print('----------------')
    print(solution(3, 3))
