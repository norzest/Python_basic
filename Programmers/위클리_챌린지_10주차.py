# 위클리 챌린지 10주차 - 교점에 별 만들기


def solution(line):
    # 교점
    point = []
    inf = float('inf')
    max_x, min_x, max_y, min_y = -inf, inf, -inf, inf

    # 교점 찾기
    n = len(line)
    for i in range(n):
        for j in range(i+1, n):
            a, b, e = line[i][0], line[i][1], line[i][2]
            c, d, f = line[j][0], line[j][1], line[j][2]
            temp = a * d - b * c
            if temp == 0:
                continue
            x, y = (b*f - e*d)/temp, (e*c - a*f)/temp
            if x - int(x) or y - int(y):
                continue
            x, y = int(x), int(y)
            max_x, min_x = max(max_x, x), min(min_x, x)
            max_y, min_y = max(max_y, y), min(min_y, y)
            point.append([x, y])

    answer = [['.' for _ in range(max_x-min_x+1)] for _ in range(max_y-min_y+1)]
    for x, y in point:
        answer[max_y - y][x-min_x] = '*'
    return [''.join(a) for a in answer]


if __name__ == "__main__":
    print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
    print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
    print(solution([[1, -1, 0], [2, -1, 0]]))
    print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
