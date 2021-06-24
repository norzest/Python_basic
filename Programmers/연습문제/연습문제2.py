# 연습문제 - 가운데 글자 가져오기

def solution(s):

    s_len = int(len(s)/2)
    if len(s) % 2 != 0:
        return s[int(s_len)]
    else:
        return ''.join([s[s_len-1], s[s_len]])


if __name__ == "__main__":
    print(solution("abcde"))
    print('-------------')
    print(solution("qwer"))
    print('-------------')