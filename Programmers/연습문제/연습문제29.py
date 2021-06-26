# 연습문제 - x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    return [i * x + x for i in range(n)]


if __name__ == "__main__":
    print(solution(2, 5))
    print('-------------')
    print(solution(4, 3))
    print('-------------')
    print(solution(-4, 2))
    print('-------------')
