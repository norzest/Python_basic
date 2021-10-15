# 연습문제 - 최솟값 만들기


def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort()

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer


if __name__ == "__main__":
    print(solution([1, 4, 2], [5, 4, 4]))
    print(solution([1, 2], [3, 4]))
