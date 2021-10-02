# 이분탐색 - 입국심사

def solution(n, times):
    right = min(times) * n  # 42
    left = 1
    answer = 0

    while left <= right:
        mid = (right + left) // 2  # 21
        people = 0

        for i in times:
            people += mid // i  # 3
            if people >= n:
                break

        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


if __name__ == "__main__":
    print(solution(6, [7, 10]))
    print('-------------')
    print(solution(4, [1, 29, 2, 5, 13]))
    print('-------------')
