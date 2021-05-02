# 해시 - 완주하지 못한 선수

def solution(participant, completion):
    par = dict()

    for i in participant:
        if i not in par.keys():
            par[i] = 1
        else:
            par[i] += 1

    for i in completion:
        if i in par.keys():
            par[i] -= 1

    answer = ''

    for i in par:
        if par[i] == 1:
            answer = i
            break

    return answer


if __name__ == "__main__":
    aa, bb = input().strip('[]').split('], [')
    aa = aa.replace('"', '').replace(' ', '').split(',')
    bb = bb.replace('"', '').replace(' ', '').split(',')

    print(solution(aa, bb))