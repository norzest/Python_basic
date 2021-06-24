# 연습문제 - 이상한 문자 만들기

def solution(s):
    s = list(s)
    count = 0
    for i in range(len(s)):
        if s[i] == ' ':
            count = 0
        else:
            if count % 2 == 0:
                s[i] = s[i].upper()
            else:
                s[i] = s[i].lower()
            count += 1
    return ''.join(s)


if __name__ == "__main__":
    print(solution("try hello world"))
    print('-------------')

