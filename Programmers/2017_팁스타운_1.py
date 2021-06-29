# 2017 팁스타운 - 짝지어 제거하기

def solution(s):
    stacks = []

    for i in s:
        if stacks and stacks[-1] == i:
            stacks.pop()
        else:
            stacks.append(i)

    return 0 if stacks else 1


if __name__ == "__main__":
    print(solution("baabaa"))
    print('------------------')
    print(solution("cdcd"))
    print('------------------')
