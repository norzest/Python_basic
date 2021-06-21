# 2018 KAKAO BLIND RECRUITMENT - [1차] 다트 게임

import re


def solution(dartResult):
    stacks = list(map(int, re.findall('\d+', dartResult)))
    alpha = ['S', 'D', 'T']
    count = 0
    for result in dartResult:
        if result in alpha:
            stacks[count] *= stacks[count] ** (alpha.index(result))
            count += 1
        if result == '*':
            stacks[count-1] *= 2
            if stacks[count-2] and count-2 >= 0:
                stacks[count-2] *= 2
        if result == '#':
            stacks[count-1] = -stacks[count-1]

    return sum(stacks)


if __name__ == "__main__":
    print(solution("1D2S0T"))
    print('-------------')
    print(solution("1D2S#10S"))
    print('-------------')
    print(solution("1D2S3T*"))
    print('-------------')
    print(solution("1D*2S3T"))
    print('-------------')
