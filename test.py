# 2019 KAKAO BLIND RECRUITMENT - 후보키


def solution(relation):
    answer = 0
    attr = [[r[i] for r in relation] for i in range(len(relation[0]))]
    len_attr = len(attr)
    for i in range(len_attr):
        if len(set(attr[i])) == len(relation):
            answer += 1
        else:
            temp = [attr[_] for _ in range(i, len_attr)]
            for j in temp:
                print(j)
        print('--')
    return answer


if __name__ == "__main__":
    print(solution([["100", "ryan", "music", "2"],
                    ["200", "apeach", "math", "2"],
                    ["300", "tube", "computer", "3"],
                    ["400", "con", "computer", "4"],
                    ["500", "muzi", "music", "3"],
                    ["600", "apeach", "music", "2"]]))
