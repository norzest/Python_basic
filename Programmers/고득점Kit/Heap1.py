# 힙 - 더 맵게

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) <= 1:
            if scoville[0] < K:
                answer = -1
            break
        else:
            temp = heapq.heappop(scoville)
            heapq.heappush(scoville, temp + (heapq.heappop(scoville) * 2))
            answer += 1

    return answer


if __name__ == "__main__":
    aa, bb = input().strip('[').split('], ')
    print(solution(list(map(int, aa.split(','))), int(bb)))