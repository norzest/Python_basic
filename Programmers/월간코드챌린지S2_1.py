# 월간 코드 챌린지 시즌2 - 음양 더하기

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        answer += absolutes[i] if signs[i] else -absolutes[i]

    return answer


if __name__ == "__main__":
    print(solution([4, 7, 12], [True, False, True]))
    print(solution([1, 2, 3], [False, False, True]))

