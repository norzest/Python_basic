# 연습문제 - 최댓값과 최솟값


def solution(s):
    arr = list(map(int, s.split(' ')))
    return ''.join([str(min(arr)), ' ', str(max(arr))])


if __name__ == "__main__":
    print(solution("1 2 3 4"))
    print(solution("-1 -2 -3 -4"))
    print(solution("-1 -1"))
