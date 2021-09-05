# 월간 코드 챌린지 시즌 2 - 2개 이하로 다른 비트

def solution(numbers):
    answer = []
    for number in numbers:
        # number 를 이진수로 변환
        bn = format(number, 'b')

        # 가장 오른쪽 수가 0 이면 1로 변환
        # ex) 110 -> 111
        if bn[-1] == '0':
            answer.append(int(''.join([bn[:-1], '1']), 2))
        # 아닐 경우 bn을 뒤집은 뒤 가장 처음 나오는 0과 0 바로 전의 1을 바꿈
        else:
            bn = list(bn[::-1])
            # 0 이 없을경우 추가
            if '0' not in bn:
                bn.append('0')
            i = bn.index('0')
            bn[i] = '1'
            bn[i-1] = '0'
            answer.append(int(''.join(bn[::-1]), 2))

    return answer


if __name__ == "__main__":
    print(solution([2, 7]))