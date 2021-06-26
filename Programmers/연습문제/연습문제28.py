# 연습문제 - 행렬의 덧셈

from numpy import array


def solution(arr1, arr2):
    return (array(arr1) + array(arr2)).tolist()


if __name__ == "__main__":
    print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
    print('-------------')
    print(solution(	[[1], [2]], [[3], [4]]))
    print('-------------')
