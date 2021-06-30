# 2020 KAKAO BLIND RECRUITMENT - 문자열 압축

def solution(s):
    answer = 0
    s_len = len(s)
    for i in range(1, int(s_len/2) + 1):
        temp = [s[j:j+i] for j in range(0, int(s_len), i)]
        print(temp)
        for j in range(len(temp) - 1):
            if temp[j] == temp[j+1]:
                try:
                    temp[j] = '2'
                except:
                    temp[j] = '2'
        print(temp)
        print('--')

    return answer


if __name__ == "__main__":
    print(solution("aabbaccc"))
    print('-------------')
    print(solution("ababcdcdababcdcd"))
    print('-------------')
    print(solution("abcabcdede"))
    print('-------------')
    print(solution("a"))
    print('-------------')

