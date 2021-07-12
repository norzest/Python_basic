from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for i in course:
        comb = []

        # 각각의 문자열에서 i개를 뽑을 때의 조합을 추가
        for order in orders:
            comb += combinations(sorted(order), i)

        if comb:
            # 결과로 나온 조합 리스트를 다시 각각의 나온 횟수로 정리한 객체 생성
            cnt_comb = Counter(comb)
            # 가장 나온횟수가 많은 조합을 answer 에 추가
            answer += [k for k, v in cnt_comb.items() \
                       if v > 1 and v == max(cnt_comb.values())]

    return [''.join(i) for i in sorted(answer)]


if __name__ == "__main__":
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
    print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
    print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
