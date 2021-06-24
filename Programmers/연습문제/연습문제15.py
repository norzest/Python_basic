# 연습문제 - 약수의 합

def solution(n):
    answer = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            answer += i + (n//i) if i != n//i else i

    return answer


if __name__ == "__main__":
    print(solution(12))
    print('-------------')
    print(solution(5))
    print('-------------')
    print(solution(1))
    print('-------------')
