# 연습문제 - 야근지수

import heapq


def solution(n, works):
    answer = 0

    # 최대 힙 생성
    heap = []
    for work in works:
        heapq.heappush(heap, (-work, work))

    # n 번 만큼 반복
    while n > 0:
        if not heap:
            break

        # 최대값을 pop
        temp = heapq.heappop(heap)[1] - 1
        # 최대값이 1 이상이였으면 최대값 - 1 을 push
        if temp >= 1:
            heapq.heappush(heap, (-temp, temp))

        n -= 1

    for h in heap:
        answer += h[1] * h[1]
    return answer


if __name__ == "__main__":
    print(solution(4, [4, 3, 3]))
    print(solution(1, [2, 1, 2]))
    print(solution(3, [1, 1]))
