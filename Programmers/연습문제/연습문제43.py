# 연습문제 - 거스름돈


def solution(n, money):
    dp = [1] + [0] * n

    for m in money:
        for i in range(m, n + 1):
            if i >= m:
                dp[i] += dp[i - m]

    return dp[n] % 1000000007


if __name__ == "__main__":
    print(solution(5, [1, 2, 5]))
