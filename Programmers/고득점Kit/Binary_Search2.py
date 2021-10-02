# 이분탐색 - 징검다리

def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()  # 이분탐색을 위한 정렬

    left = 0
    right = distance

    # 아래의 루프를 실행하여 삭제한 바위의 개수가 n개 이면 정답
    # 루프 처음엔 중앙까지의 거리를 기준값으로 지정하여
    # 삭제한 바위의 개수가 n개 이상이면 그 값을 증가
    # n개 이하 이면 값을 감소 시키는 방법으로 이분탐색 알고리즘 적용
    while left <= right:
        mid = (left + right) // 2  # 기준값
        temp = float('inf')  # 각 루프마다 최소값을 저장할 임시 변수
        location = 0  # 현재 위치
        count = 0  # 바위 제거한 갯수

        for i in rocks:
            dif = i - location

            # mid 값 이하면 바위 삭제
            if dif < mid:
                count += 1
            else:
                location = i  # 현재 위치 변경
                temp = dif if dif < temp else temp

        # 제거한 바위 수가 목표 수보다 많을 경우 기준값(mid)을 줄이고 재 탐색
        if count > n:
            right = mid - 1
        # 제거한 바위 수가 목표 수보다 작거나 같을 경우 answer에 최소값을 저장한 후
        # 기준값을 늘려 재 탐색
        else:
            answer = temp
            left = mid + 1

    return answer


if __name__ == "__main__":
    print(solution(25, [2, 14, 11, 21, 17], 2))



