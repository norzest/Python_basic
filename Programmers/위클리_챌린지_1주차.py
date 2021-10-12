# 위클리 챌린지 1주차 - 부족한 금액 계산하기


def solution(price, money, count):
    need = 0
    i = 1
    while count >= i:
        need += price * i
        i += 1

    return 0 if need - money < 0 else need - money


if __name__ == "__main__":
    print(solution(3, 20, 4))
