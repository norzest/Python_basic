# 2019 KAKAO BLIND RECRUITMENT - 실패율

import collections


def solution(n, stages):
    # 실패율을 저장할 딕셔너리
    failure_rate = {}
    # 도전자의 수
    challenger = len(stages)

    for stage in range(n):
        # 도전자가 0명이면 실패율은 0
        if challenger == 0:
            failure_rate[stage+1] = 0
        else:
            # 해당 스테이지의 도전자의 수
            count = stages.count(stage+1)
            # 해당 스테이지의 실패율 입력
            failure_rate[stage+1] = count / challenger
            # 해당 스테이지에 있는 도전자의 수만큼 도전자 감소
            challenger -= count

    # 실패율을 기준으로 인덱스에 대하여 내림차순 정렬
    return sorted(failure_rate, key=lambda x: failure_rate[x], reverse=True)


if __name__ == "__main__":
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    print(solution(4, [4, 4, 4, 4, 4]))

