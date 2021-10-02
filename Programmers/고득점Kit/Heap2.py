# 힙 - 디스크 컨트롤러 <-- 클래스 다시 한번 보기

import heapq


def solution(jobs):
    jobs.sort()
    jobs_len = len(jobs)
    times = heap_time = i = 0
    use = []
    heap = []
    total = []

    while heap or times <= jobs[-1][0]:
        while i <= jobs_len - 1 and times == jobs[i][0]:
            heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
            i += 1

        if use and heap_time == use[0]:
            heap.remove(use)
            heapq.heapify(heap)
            total.append(times - use[1])
            use = []
            heap_time = 0

        if not use and heap:
            use = heap[0]
            heap_time = 0

        times += 1
        heap_time += 1

    return sum(total)//jobs_len


if __name__ == "__main__":
    print(solution([[0, 3], [1, 9], [2, 6]]))
    print('-------------')
    print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))
    print('-------------')
    print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]))
    print('-------------')