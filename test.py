# 연습문제 - 2 x n 타일링


def solution(n):
    if n <= 3:
        return n
    arr = [1, 2, 3]
    for i in range(3, n):
        arr.append(arr[i-2] + arr[i-1])

    return arr[-1] % 1000000007


if __name__ == "__main__":
    print(solution(4))
