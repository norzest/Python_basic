# 연습문제 - 하샤드 수

def solution(x):
    return x % sum(list(map(int, str(x)))) == 0


if __name__ == "__main__":
    print(solution(10))
    print('-------------')
    print(solution(12))
    print('-------------')
