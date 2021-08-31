# 2021 KAKAO BLIND RECRUITMENT - 순위 검색

from itertools import combinations


def solution(info, query):
    answer = []
    # 지원자를 검색 조건별로 나누어 저장할 딕셔너리
    applicant = {}

    for i in info:
        s = i.split()
        # 지원자 딕셔너리의 값을 점수, 나머지를 키로 지정
        key, value = s[:-1], int(s[-1])

        for j in range(5):
            # 지원자의 정보를 토대로 나올 수 있는 모든 조건
            # ex) java, backend, junior, pizza 4개로 나올수 있는 모든 조합
            for k in combinations(key, j):
                temp = "".join(k)
                if temp in applicant:
                    applicant[temp].append(value)
                else:
                    applicant[temp] = [value]

    # 각 키의 값들을 정렬
    for key in applicant.keys():
        applicant[key].sort()

    for qry in query:
        q = qry.split(" ")
        # 조건의 점수는 value 나머지는 key
        q_key = "".join([_ for _ in q[:-1] if _ != 'and' and _ != '-'])
        q_value = int(q[-1])

        # 점수를 제외한 조건을 만족하는 key 가 applicant 에 있다면
        if q_key in applicant:
            value = applicant[q_key]
            len_value = len(value)

            # 조건을 만족하는 key 의 value 가 점수 조건도 만족하는지 이분탐색
            left, right = 0, len_value
            while left < right:
                mid = (left + right) // 2
                if value[mid] >= q_value:
                    right = mid
                else:
                    left = mid + 1

            answer.append(len_value - left)
        else:
            answer.append(0)
    return answer


if __name__ == "__main__":
    print(solution(
        ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
        ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]))
