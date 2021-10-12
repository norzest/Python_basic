# 위클리 챌린지 10주차 - 교점에 별 만들기

from sympy import Symbol, solve


def solution(line):
    answer = []
    point = []
    n = len(line)
    for i in range(n):
        for j in range(i+1, n):
            x = Symbol('x')
            y = Symbol('y')
            eq1 = line[i][0] * x + line[i][1] * y + line[i][2]
            eq2 = line[j][0] * x + line[j][1] * y + line[j][2]
            result = solve((eq1, eq2), dict=True)
            if result:
                point.append([result[0][x], result[0][y]])

    print(point)
    return answer


if __name__ == "__main__":
    print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
    print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
    print(solution([[1, -1, 0], [2, -1, 0]]))
    print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
