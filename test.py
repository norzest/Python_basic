# 2021 KAKAO BLIND RECRUITMENT - 순위 검색

import bisect


changes = []
temp = []


def make_cases():
    global changes, temp
    if len(temp) == 4:
        t = []
        for index in temp:
            t.append(index)
        changes.append(t)
        return

    for i in (False, True):
        temp.append(i)
        make_cases()
        temp.pop()


def solution(info, query):
    answer = []
    make_cases()
    print(changes)
    print(temp)
        
    return answer


if __name__ == "__main__":
    print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
