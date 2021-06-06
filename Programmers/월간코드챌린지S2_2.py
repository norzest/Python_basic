# 월간 코드 챌린지 시즌2 - 약수의 개수와 덧셈


def get_divisor_count(n):
    count = 1

    for i in range(1, n//2 + 1):
        if n % i == 0:
            count += 1

    return count


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if get_divisor_count(i) % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer


if __name__ == "__main__":
    print(solution(13, 17))
    print(solution(24, 27))
