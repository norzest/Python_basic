# 위클리 챌린지 7주차 - 입실 퇴실


def solution(enter, leave):
    n = len(enter)
    answer = [0] * n
    enter_, leave_ = {}, {}

    for i in range(1, n + 1):
        enter_[i] = enter[enter.index(i) + 1:]
        leave_[i] = leave[:leave.index(i)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j in enter_[i] and j in leave_[i]:
                answer[j - 1] += 1
                answer[i - 1] += 1

                temp = enter[enter.index(i) + 1:enter.index(j)]
                if temp:
                    for t in temp:
                        if not (t in enter_[i] and t in leave_[i]):
                            answer[i - 1] += 1
                            answer[t - 1] += 1

    return answer


if __name__ == "__main__":
    print(solution([1, 3, 2], [1, 2, 3]))
    print(solution([1, 4, 2, 3], [2, 1, 3, 4]))
    print(solution([3, 2, 1], [2, 1, 3]))
    print(solution([3, 2, 1], [1, 3, 2]))
    print(solution([1, 4, 2, 3], [2, 1, 4, 3]))
