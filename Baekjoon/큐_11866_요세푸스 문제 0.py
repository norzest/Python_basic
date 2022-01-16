# 11866 요세푸스 문제 0


def solution():
    n, k = map(int, input().split())
    arr = [i for i in range(1, n + 1)]
    answer = []

    while arr:
        for i in range(k-1):
            arr.append(arr.pop(0))
        answer.append(arr.pop(0))

    print("<", end="")
    for i in range(n - 1):
        print(f"{answer[i]},", end=" ")
    print(answer[-1], end="")
    print(">")


if __name__ == '__main__':
    solution()
