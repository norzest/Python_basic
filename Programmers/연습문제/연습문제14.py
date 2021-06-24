# 연습문제 - 시저 암호

def solution(s, n):
    s = [ord(i) for i in s]
    for i in range(len(s)):
        if s[i] != 32:
            if s[i] <= 90 and s[i]+n >= 97:
                s[i] = chr(s[i] + n - 26)
            elif chr(s[i] + n).isalpha():
                s[i] = chr(s[i] + n)
            else:
                s[i] = chr(s[i] + n - 26)
        else:
            s[i] = chr(s[i])

    return ''.join(s)


if __name__ == "__main__":
    print(solution("AaZz", 25))
    print('-------------')
    print(solution("z", 1))
    print('-------------')
    print(solution("a B z", 4))
    print('-------------')
