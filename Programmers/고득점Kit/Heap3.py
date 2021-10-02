# 힙 - 이중우선순위큐

import heapq


def solution(operations):
    answer = []

    for i in operations:
        if i == 'D 1' and answer:
            answer = [-i for i in answer]
            heapq.heapify(answer)
            heapq.heappop(answer)
            answer = [-i for i in answer]
            heapq.heapify(answer)
        elif i == 'D -1' and answer:
            heapq.heappop(answer)
        elif i[0] == 'I':
            heapq.heappush(answer, int(i[2:]))

    try:
        return [max(answer), min(answer)]
    except:
        return [0, 0]


if __name__ == "__main__":
    print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))