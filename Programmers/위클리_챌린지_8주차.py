# 위클리 챌린지 8주차 - 최소직사각형


def solution(sizes):
    a, b = 0, 0

    for size in sizes:
        big, small = max(size), min(size)
        a = big if a <= big else a
        b = small if b <= small else b

    return a * b


if __name__ == "__main__":
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
    print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
