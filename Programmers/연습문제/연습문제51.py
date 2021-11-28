# 연습문제 - 2 x n 타일링


def solution(n):
    a = 1
    b = 2
    answer = a + b
    for i in range(3, n):
        a = b
        b = answer
        answer = a + b

    return answer % 1000000007


if __name__ == "__main__":
    print(solution(4))
