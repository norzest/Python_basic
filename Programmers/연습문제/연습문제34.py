# 연습문제 - 다음 큰 숫자


def solution(n):
    # 2진수 변환한 n의 1의 갯수
    n_count = format(n, 'b').count('1')

    i = 1
    while True:
        answer = n + i
        if format(answer, 'b').count('1') == n_count:
            return answer
        i += 1


if __name__ == "__main__":
    print(solution(78))
    print(solution(	15))
