# 연습문제 - 제일 작은 수 제거

def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]


if __name__ == "__main__":
    print(solution([4, 3, 2, 1]))
    print('-------------')
    print(solution([10]))
    print('-------------')
