# 연습문제 - 하노이의 탑


answer = []


def hanoi(n, start, end, other):
    if n == 1:
        answer.append([start, end])
        return

    hanoi(n - 1, start, other, end)  # 1, 2, 3
    answer.append([start, end])  # [1, 3]
    hanoi(n - 1, other, end, start)  # 3, 2, 1


def solution(n):
    hanoi(n, 1, 3, 2)
    return answer


if __name__ == "__main__":
    print(solution(2))
    print(solution(3))
