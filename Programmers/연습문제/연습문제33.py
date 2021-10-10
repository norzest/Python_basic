# 연습문제 - 올바른 괄호


def solution(s):
    stack = []

    for g in s:
        if g == ')':
            if '(' not in stack:
                return False
            else:
                stack.pop()
        else:
            stack.append(g)

    return stack == []


if __name__ == "__main__":
    print(solution('(())()'))
    print(solution('())('))
