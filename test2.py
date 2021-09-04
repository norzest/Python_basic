# 월간 코드 챌린지 시즌 2 - 2개 이하로 다른 비트

def solution(numbers):
    answer = []
    for number in numbers:
        # number 를 50자리의 이진수로 변환 (10의 15승은 이진수로 50자리)
        bn = format(number, 'b').zfill(50)

        # bn 과 bn 에 n 을 더한 수의 문자열 차이가 2개 이하일 때까지 n += 1
        n = 1
        while True:
            temp = format(number + n, 'b').zfill(50)
            diff = 0
            for a, b in zip(bn, temp):
                if a != b:
                    diff += 1

            # 차이가 2개 이하일 경우 answer 에 추가 후 break
            if diff <= 2:
                answer.append(int(temp, 2))
                break

            n += 1

    return answer


if __name__ == "__main__":
    print(solution([2, 7]))
