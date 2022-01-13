# 11866 요세푸스 문제 0


def solution():
    n, k = map(int, input().split())
    arr = [i for i in range(1, n + 1)]
    answer = []
    num = k

    while arr:
        if num <= len(arr):
            del arr[num-1]
            answer.append(num)
            num += k
            if num > n:
                num -= n
        else:
            num += k
            if num > n:
                num -= n

        print(arr)
        print(answer)
        print('--')


if __name__ == '__main__':
    solution()
