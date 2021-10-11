# 위클리 챌린지 6주차 - 복서 정렬하기


def solution(weights, head2head):
    answer = []
    p = len(weights)
    total = []

    for i in range(p):
        # 자신보다 몸무게가 많은 선수를 이긴 횟수
        big_win = 0
        for j in range(p):
            if head2head[i][j] == 'W' and weights[i] < weights[j]:
                big_win += 1

        # 번호, 체중, h2h, big_win
        total.append((i + 1, weights[i],
                      head2head[i].count('W'), big_win))

    # 1순위 승률, 2순위 체급차 승리, 3순위 몸무게 정렬
    total.sort(key=lambda x: (x[2], x[3], x[1]), reverse=True)

    for t in total:
        answer.append(t[0])
    return answer


if __name__ == "__main__":
    print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))
    print(solution([145, 92, 86], ["NLW", "WNL", "LWN"]))
    print(solution([60, 70, 60], ["NNN", "NNN", "NNN"]))
