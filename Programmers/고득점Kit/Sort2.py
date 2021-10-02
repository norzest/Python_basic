# 정렬 - 가장 큰 수 <-- x*3 하면 인덱스 에러 안나게 가능

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)

    return str(int("".join(numbers)))


if __name__ == "__main__":
    print(solution([6, 10, 2]))
    print('-------------')
    print(solution([3, 30, 34, 5, 9]))
    print('-------------')
    print(solution([40, 403]))
    print('-------------')
