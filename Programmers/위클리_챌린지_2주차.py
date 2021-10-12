# 위클리 챌린지 2주차 - 상호평가


def solution(scores):
    answer = ''
    n = len(scores)
    # 각각 받은 점수
    score = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            score[j].append(scores[i][j])

    # 각각의 평균
    avg = [0 for _ in range(n)]
    for i in range(n):
        max_num = max(score[i])
        min_num = min(score[i])
        if (score[i][i] == max_num and score[i].count(max_num) <= 1) or \
                (score[i][i] == min_num and score[i].count(min_num) <= 1):
            avg[i] = (sum(score[i]) - score[i][i])/(n - 1)
        else:
            avg[i] = sum(score[i])/n

    # 학점
    answer = ['F' for _ in range(n)]
    for i in range(n):
        if avg[i] >= 90:
            answer[i] = 'A'
        elif avg[i] >= 80:
            answer[i] = 'B'
        elif avg[i] >= 70:
            answer[i] = 'C'
        elif avg[i] >= 50:
            answer[i] = 'D'

    return ''.join(answer)


if __name__ == "__main__":
    print(solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))
    print(solution([[50, 90], [50, 87]]))
    print(solution([[70, 49, 90], [68, 50, 38], [73, 31, 100]]))
