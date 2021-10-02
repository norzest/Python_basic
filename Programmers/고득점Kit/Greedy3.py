# 그리디 - 큰 수 만들기

def solution(number, k):

    stack = [number[0]]

    for i in number[1:]:
        while stack and stack[-1] < i and k > 0:
            k -= 1
            stack.pop()

        stack.append(i)

    if k != 0:
        stack = stack[:-k]

    return ''.join(stack)


if __name__ == "__main__":
    print(solution("12111", 3))
    print('-------------')
    print(solution("111111", 3))
    print('-------------')
    print(solution("1231234", 3))
    print('-------------')
    print(solution("4177252841", 4))
