# 2019 KAKAO BLIND RECRUITMENT - 후보키


def solution(relation):
    answer = 0
    relation_len = len(relation[0])
    attr = [[r[i] for r in relation] for i in range(relation_len)]

    print(attr)
    return answer


if __name__ == "__main__":
    print(solution([["100", "ryan", "music", "2"],
                    ["200", "apeach", "math", "2"],
                    ["300", "tube", "computer", "3"],
                    ["400", "con", "computer", "4"],
                    ["500", "muzi", "music", "3"],
                    ["600", "apeach", "music", "2"]]))
