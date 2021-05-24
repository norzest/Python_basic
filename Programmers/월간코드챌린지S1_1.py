# 월간 코드 챌린지 시즌1 - 내적

def solution(a, b):
    return sum([a*b for a, b in zip(a, b)])


if __name__ == "__main__":
    print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
    print(solution([-1, 0, 1], [1, 0, -1]))
