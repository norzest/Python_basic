# 2019 KAKAO BLIND RECRUITMENT - 후보키

from itertools import combinations


def solution(relation):
    answer = []
    column_len = len(relation[0])

    # column 한개 조합부터 4개 조합까지 전부 확인
    for i in range(1, column_len+1):
        # column 한개 조합부터 4개 조합까지 전부 확인
        for comb in combinations(list(range(column_len)), i):
            # 중복을 확인할 임시 배열
            temp = []
            for r in relation:
                # 현재 키 값
                key = [r[_] for _ in comb]

                # 한개라도 중복돼면 break
                if key in temp:
                    break
                # 중복 안돼면 temp 에 추가
                else:
                    temp.append(key)
            # break 가 발생 안했을 시
            else:
                for a in answer:
                    # 현재 key 의 조합이
                    # 현재까지 구했던 조합들의 부분집합인지 확인
                    if set(a).issubset(set(comb)):
                        break
                # 부분집합이 아니면 해당 조합 추가
                else:
                    answer.append(comb)

    return len(answer)


if __name__ == "__main__":
    print(solution([["100", "ryan", "music", "2"],
                    ["200", "apeach", "math", "2"],
                    ["300", "tube", "computer", "3"],
                    ["400", "con", "computer", "4"],
                    ["500", "muzi", "music", "3"],
                    ["600", "apeach", "music", "2"]]))