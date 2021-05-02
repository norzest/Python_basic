# 그리디 = 조이스틱

def solution(name):
    name = list(name)
    answer = 0
    num = 0

    while name.count('A') != len(name):

        if name[num] != 'A':
            temp = ord(name[num])
            if ord('N') >= temp:
                answer += temp - 65
            else:
                answer += 91 - temp

        name[num] = 'A'
        nxt = prv = num
        while name[nxt] == 'A' and nxt < len(name) - 1:
            nxt += 1

        while name[prv] == 'A' and prv > -len(name) + 1:
            prv -= 1

        if nxt - num > -prv + num:
            num -= 1
        else:
            num += 1

        if name.count('A') != len(name):
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution("JEROEN"))
    print('-------------')
    print(solution("JAN"))
    print('-------------')
    print(solution("AAA"))
    print('-------------')
    print(solution("BABAAAAAB"))
    print('-------------')