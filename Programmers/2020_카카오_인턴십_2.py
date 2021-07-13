# 2020 카카오 인턴십 - 수식 최대화

from itertools import permutations
import re


def solution(expression):
    answer = 0
    # +, -, * 의 우선순위의 경우의 수
    arr = list(permutations(['+', '-', '*']))
    # 문자열을 연산기호와 숫자로 나누기
    expression = re.split('([^\d])', expression)

    # 각각 조합별로 값 비교 실행
    for ar in arr:
        expression_temp = expression.copy()
        # 가장 우선순위가 높은 연산기호 순으로 처리
        for a in ar:
            while a in expression_temp:
                # 해당 연산기호의 인덱스를 찾아서
                a_index = expression_temp.index(a)
                # eval을 통해 양옆의 수를 계산해서 담는다
                result = str(eval(expression_temp[a_index-1] + expression_temp[a_index] + expression_temp[a_index+1]))
                # 그 수를 저장 후 남은 연산기호와 수는 없앤다
                # ex. 100 + 200 을 계산하면 300 + 200 으로 만든 후 + 와 200 제거
                expression_temp[a_index-1] = result
                expression_temp = expression_temp[:a_index] + expression_temp[a_index+2:]
        
        # 최대값인지 확인
        answer = max(answer, abs(int(expression_temp[-1])))
    
    return answer


if __name__ == "__main__":
    print(solution("100-200*300-500+20"))
    print(solution("50*6-3*2"))
