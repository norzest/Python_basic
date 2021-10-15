# 연습문제 - 숫자의 표현


def solution(n):
    answer = 1

    half = (n // 2) + 2  # 반복문을 위한 int(n 의 반) + 1
    i = 1  # 반복문 시작 숫자
    while True:
        # i 가 반을 넘었다면 자기 자신 말고 연속된 수로 표현 불가
        if i == half + 1:
            break

        temp = 0
        for k in range(i, half):
            temp += k

            if temp == n:
                answer += 1
            elif temp > n:
                break

        i += 1

    return answer


if __name__ == "__main__":
    print(solution(15))
