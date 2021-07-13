# 2021 Dev Matching 웹 백엔드 개발자(상반기) - 행렬 테두리 회전하기

def solution(rows, columns, queries):
    answer = []
    # rows * columns 행렬
    arr = [[i + (j*rows) for i in range(1, rows+1)] for j in range(columns)]
    for i in arr:
        print(i)

    for q in queries:
        # 현재 가리키는 위치(숫자를 바꿀 예정인 위치)
        pointer = [q[0] - 1, q[1] - 1]
        # 가로, 세로 이동할 횟수
        h, v = q[3] - 1 - pointer[1], q[2] - 1 - pointer[0]

        for i in range(h):
            print(arr[pointer[0]][pointer[1]])
            pointer[1] += 1

        for i in range(v):
            print(arr[pointer[0]][pointer[1]])
            pointer[0] += 1

        for i in range(h):
            print(arr[pointer[0]][pointer[1]])
            pointer[1] -= 1

        for i in range(v):
            print(arr[pointer[0]][pointer[1]])
            pointer[0] -= 1

        print('--')
    return answer


if __name__ == "__main__":
    print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
    print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
    # print(solution(100, 97, [[1, 1, 100, 97]]))
