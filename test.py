# 2021 Dev Matching: 웹 백엔드 개발자 - 다단계 칫솔 판매


def solution(enroll, referral, seller, amount):
    def bfs(graph, start, money):
        visited = []
        income = []
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)

                if node in graph:
                    temp = money // 10 if money // 10 >= 1 else 0  # 추천인이 받을 수입
                    # 10%를 계산한 금액이 1원 미만이면 이득 분배 X
                    income.append(money - temp)
                    money = money // 10
                    if money == 0:
                        break
                    queue.extend(graph[node])

        return list(zip(visited, income))

    # 조직도 생성
    group = dict()
    for e, r in zip(enroll, referral):
        if e not in group.keys():
            group[e] = [r]
        else:
            group[e].extend([r])

    # 조직원 별 수입 딕셔너리 생성
    group_income = dict()
    for s, a in zip(seller, amount):
        br = bfs(group, s, a * 100)

        for r in br:
            if r[0] not in group_income.keys():
                group_income[r[0]] = r[1]
            else:
                group_income[r[0]] += r[1]

    answer = [0 for _ in enroll]
    for g in group_income:
        answer[enroll.index(g)] += group_income[g]
    return answer


if __name__ == "__main__":
    print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
    print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]))
