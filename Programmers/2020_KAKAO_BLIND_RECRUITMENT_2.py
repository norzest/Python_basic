# 2020 KAKAO BLIND RECRUITMENT - 괄호 변환

def solution(p):

    def discrimination(u):
        stack = []

        for i in u:
            # ( 가 나오면 스택에 저장
            if i == '(':
                stack.append(i)
            else:
                # ) 가 나오면 가장 나중에 저장된 괄호가 ( 인지 확인
                if stack and stack.pop() == '(':
                    continue
                # ( 가 아닐 경우 올바른 괄호가 아님
                else:
                    return False

        # 반복문이 끝나고 스택이 비어있으면 올바른 괄호
        return len(stack) == 0

    def sep(w):
        # 빈 문자열일 경우, 빈 문자열 반환
        if not w:
            return []

        u = []
        v = []
        # ( 과 ) 의 수가 같아질 때까지 u에 괄호 추가
        for i in range(len(w)):
            u.append(w[i])
            # ( 과 ) 의 수가 같아지면 나머지는 v에 추가 후 break
            if u.count('(') == u.count(')'):
                v = w[i+1:]
                break

        # u가 올바른 괄호일 경우
        if discrimination(u):
            # v에 대해 재귀 호출 후 u에 이어 붙혀 반환
            u.extend(sep(v))
            return u
        else:
            # ( 를 가진 빈 문자열 생성
            temp = ['(']
            # v에 대해 재귀 호출 후 temp에 추가
            temp.extend(sep(v))
            # temp 에 ) cnrk
            temp.append(')')
            # u의 첫 번쨰와 마지막 문자 제거
            del u[0]
            del u[-1]
            # 남은 괄호를 뒤집어서 temp의 뒤에 추가
            u = [')' if i == '(' else '(' for i in u]
            temp.extend(u)
            # 반환
            return temp

    return ''.join(sep(list(p)))


if __name__ == "__main__":
    print(solution("(()())()"))
    print(solution(")("))
    print(solution("()))((()"))
    print(solution(""))
