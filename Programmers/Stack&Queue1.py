# 스택/큐 - 주식 가격 <------------- 스택큐 사용 x

def solution(prices):
    answer = []

    for i in range(len(prices)):
        answer.append(0)
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:
                break

    return answer


if __name__ == "__main__":
    a = input().strip('[]')
    a = list(map(int, a.replace(' ', '').split(',')))

    print(solution(a))