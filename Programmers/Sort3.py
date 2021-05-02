# 정렬 - H_Index

def solution(citations):
    citations.sort(reverse=True)
    citations_len = len(citations)

    i = 0
    while True:
        if citations_len <= i or citations[i] <= i:
            return i

        i += 1


if __name__ == "__main__":
    print(solution([3, 0, 6, 1, 5]), 3)
    print(solution([12, 11, 10, 9, 8, 1]), 5)
    print(solution([6, 6, 6, 6, 6, 1]), 5)
    print(solution([4, 4, 4]), 3)
    print(solution([4, 4, 4, 5, 0, 1, 2, 3]), 4)
    print(solution([10, 11, 12, 13]), 4)
    print(solution([0, 0, 1, 1]), 1)
    print(solution([0, 1]), 1)
    print(solution([10, 9, 4, 1, 1]), 3)