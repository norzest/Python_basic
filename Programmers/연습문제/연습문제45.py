# 연습문제 - 멀리 뛰기


def solution(n):
    if n <= 3:
        return n

    arr = [1, 2, 3]

    for i in range(3, n):
        arr.append(arr[i-2] + arr[i-1])
    print(arr)
    return arr[-1] % 1234567


if __name__ == "__main__":
    print(solution(4))
    print(solution(3))
