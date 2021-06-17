# 2018 KAKAO BLIND RECRUITMENT - [1차] 다트 게임

def solution(dartResult):
    stacks = []
    alpha = ['S', 'D', 'T']
    answer = 0

    for result in dartResult:
        if result.isdigit():
            stacks.append(int(result))
        if result in alpha:
            stacks[-1] *= alpha.index(result) + 1

    print(stacks)

    return answer


if __name__ == "__main__":
    print(solution("1S2D*3T"))
    print('-------------')
    print(solution("1D2S#10S"))
    print('-------------')
