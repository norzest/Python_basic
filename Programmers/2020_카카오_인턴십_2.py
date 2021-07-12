# 2020 카카오 인턴십 - 수식 최대화

from itertools import permutations
import re


def solution(expression):
    answer = 0
    # +, -, * 의 우선순위의 경우의 수
    arr = list(permutations([2, 1, 0]))
    # 각각의 우선순위의 경우에서 연산식을 임시로 저장해줄 딕셔너리
    operator = {2: '', 1: '', 0: ''}
    # 문자열을 연산기호와 숫자로 나누기
    expression = re.split('([^\d])', expression)

    for p, m, x in arr:
        # 해당 우선순위에 연산식을 매칭
        operator[p] = '+'
        operator[m] = '-'
        operator[x] = '*'

        # 우선순위대로 연산 실행
        for i in range(3):
            print(expression)
    return answer


if __name__ == "__main__":
    print(solution("100-200*300-500+20"))
    print(solution("50*6-3*2"))
