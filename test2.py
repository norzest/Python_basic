# 2021 KAKAO BLIND RECRUITMENT - 순위 검색

import re


def solution(info, query):
    answer = []

    for qry in query:
        # 점수만 추출
        d = "".join(re.findall('\d+', qry))
        # 점수와 띄어쓰기 제거 후 and 로 스플릿
        qry = qry.replace(d, "").replace(" ", "").split("and")
        # 다시 점수 추가
        qry.append(d)

        num = 0
        for i in info:
            i = i.split(" ")

            # 점수를 제외한 각 컬럼별로 비교
            for j in range(len(qry) - 1):
                if qry[j] != "-" and i[j] != qry[j]:
                    break
            # 마지막으로 점수 비교
            else:
                if int(i[-1]) >= int(qry[-1]):
                    num += 1

        answer.append(num)

    return answer


if __name__ == "__main__":
    print(solution(
        ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
        ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]))
