# 연습문제 - 행렬의 곱셈


def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp_lst = []
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr2)):
                temp += arr1[i][k] * arr2[k][j]
            temp_lst.append(temp)
        answer.append(temp_lst)

    return answer


if __name__ == "__main__":
    print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
    print(solution(	[[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
