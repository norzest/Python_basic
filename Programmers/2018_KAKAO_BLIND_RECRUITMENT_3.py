# 2018 KAKAO BLIND RECRUITMENT - [1차] 뉴스 클러스터링

def solution(str1, str2):
    str1 = [str1[i:i+2].upper() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i + 2].upper() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]
    print(str1)
    print(str2)

    intrs = [i for i in str1 if i in str2]
    union = []

    print(intrs)

    answer = 0

    return answer


if __name__ == "__main__":
    print(solution("FRANCE", "french"))
    print('------------------')
    print(solution("handshake", "shake hands"))
    print('------------------')
    print(solution("aa1+aa2", "AAAA12"))
    print('------------------')
    print(solution("E=M*C^2", "e=m*c^2"))
    print('------------------')
