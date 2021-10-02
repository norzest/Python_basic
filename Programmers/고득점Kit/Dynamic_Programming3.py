# 동적계획법 - 등굣길

def solution(m, n, puddles):
    arr = [[0] * m for _ in range(n)]
    arr[0][0] = 1

    for a, b in puddles:
        arr[b-1][a-1] = -1

    for i in range(n):  # 분할 정복
        for j in range(m):
            if arr[i][j] != -1:
                try:
                    if arr[i][j+1] != -1:
                        arr[i][j+1] += arr[i][j]
                except IndexError:
                    arr[i][j] = arr[i][j]

                try:
                    if arr[i+1][j] != -1:
                        arr[i+1][j] += arr[i][j]
                except IndexError:
                    arr[i][j] = arr[i][j]

    return arr[-1][-1] % 1000000007


if __name__ == "__main__":
    print(solution(4, 3, [[2, 2]]))
    print('-------------')
    print(solution(4, 3, [[1, 2], [2, 1]]))
    print('-------------')