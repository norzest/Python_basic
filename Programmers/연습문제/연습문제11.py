# 연습문제 - 소수 찾기

def solution(n):  # 에라토스테네스의 채
    a = [False, False] + [True]*(n-1)
    answer = 0

    for i in range(2, n+1):
        if a[i]:
            answer += 1
            for j in range(2 * i, n + 1, i):
                a[j] = False
    return answer


if __name__ == "__main__":
    print(solution(10))
    print('-------------')
    print(solution(5))
    print('-------------')
