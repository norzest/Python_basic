# 월간 코드 챌린지 시즌 2 - 2개 이하로 다른 비트

def solution(numbers):
    answer = []
    for number in numbers:
        bn = format(number, 'b')

        if bn[-1] == '0':
            answer.append(int(''.join([bn[:-1], '1']), 2))
        else:
            bn = list(bn[::-1])
            if '0' not in bn:
                bn.append('0')
            i = bn.index('0')
            bn[i] = '1'
            bn[i-1] = '0'
            answer.append(int(''.join(bn[::-1]), 2))

    return answer


if __name__ == "__main__":
    print(solution([2, 7]))
