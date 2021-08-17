# 월간 코드 챌린지 시즌2 - 괄호 회전하기

def parentheses_check(s):
    stack = []
    for i in s:
        if i in ("[", "{", "("):
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                if i == "]" and stack[-1] == "[":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
                elif i == ")" and stack[-1] == "(":
                    stack.pop()
                else:
                    return False

    return stack == []


def solution(s):
    answer = 0

    for i in range(len(s)):
        s = "".join([s[1:], s[0]])
        if parentheses_check(s):
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution("[](){}"))
    print(solution("}]()[{"))
    print(solution("[)(]"))
    print(solution("}}}"))
