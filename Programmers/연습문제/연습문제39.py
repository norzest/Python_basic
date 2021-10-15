# 연습문제 - 피보나치 수


def solution(n):
    stack = [0, 1]
    for i in range(n - 1):
        stack.append(stack[-1] + stack[-2])

    return stack[n] % 1234567


if __name__ == "__main__":
    print(solution(3))
    print(solution(5))
