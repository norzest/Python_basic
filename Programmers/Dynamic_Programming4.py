# 동적계획법 - 도둑질

def solution(money):
    dp1 = [money[0], money[0]]
    dp2 = [0, money[1]]
    len_money = len(money)

    for i in range(2, len_money - 1):
        dp1.append(max(dp1[i-1], dp1[i-2] + money[i]))
        dp2.append(max(dp2[i-1], dp2[i-2] + money[i]))

    dp2.append(max(dp2[len_money - 2], dp2[len_money - 3] + money[len_money - 1]))
    print(dp1, dp2)
    return max(dp1[-1], dp2[-1])


if __name__ == "__main__":
    print(solution([1, 2, 3, 1, 5]), 8)