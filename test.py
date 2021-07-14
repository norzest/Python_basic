# 2021 Dev Matching 웹 백엔드 개발자(상반기) - 행렬 테두리 회전하기

def solution(rows, columns, queries):
    answer = []
    # rows * columns 행렬
    arr = [[i + (j*rows) for i in range(1, columns+1)] for j in range(rows)]

    for q in queries:
        # 현재 가리키는 위치(숫자를 바꿀 예정인 위치)
        pointer = [q[0] - 1, q[1] - 1]
        # 숫자를 이동시키면서 임시 저장할 변수
        temp = arr[pointer[0]][pointer[1]]
        # 자리가 바뀐 숫자들 중 가장 작은 수를 찾기 위한 임시 배열
        answer_temp = [temp]
        # 가로, 세로 이동할 횟수
        h, v = q[3] - 1 - pointer[1], q[2] - 1 - pointer[0]

        # 오른쪽으로 이동
        for i in range(h):
            pointer[1] += 1
            arr[pointer[0]][pointer[1]], temp = temp, arr[pointer[0]][pointer[1]]
            answer_temp.append(temp)

        # 아래로 이동
        for i in range(v):
            pointer[0] += 1
            arr[pointer[0]][pointer[1]], temp = temp, arr[pointer[0]][pointer[1]]
            answer_temp.append(temp)

        # 왼쪽으로 이동
        for i in range(h):
            pointer[1] -= 1
            arr[pointer[0]][pointer[1]], temp = temp, arr[pointer[0]][pointer[1]]
            answer_temp.append(temp)

        # 위로 이동
        for i in range(v):
            pointer[0] -= 1
            arr[pointer[0]][pointer[1]], temp = temp, arr[pointer[0]][pointer[1]]
            answer_temp.append(temp)

        # 가장 작은 수 저장
        answer.append(min(answer_temp))

    return answer


if __name__ == "__main__":
    print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
    print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
    print(solution(100, 97, [[1, 1, 100, 97]]))
