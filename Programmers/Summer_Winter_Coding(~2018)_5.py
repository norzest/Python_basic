# Summer/Winter Coding(~2018) - 점프와 순간 이동

def solution(n):
    ans = 0

    while n > 1:

        if n % 2 == 1:
            ans += 1
            n -= 1

        while n % 2 != 1:
            n = n // 2

    return ans + 1 if n == 1 else ans


if __name__ == "__main__":
    print(solution(5))
    print(solution(6))
    print(solution(5000))
