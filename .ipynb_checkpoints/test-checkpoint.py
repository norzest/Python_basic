# 연습문제 - 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = [num for num in arr if num % divisor == 0]
    return sorted(answer) if answer else [-1]


if __name__ == "__main__":
    print(solution([5, 9, 7, 10], 5))
    print('-------------')
    print(solution([2, 36, 1, 3], 1))
    print('-------------')
    print(solution([3, 2, 6], 10))
    print('-------------')
