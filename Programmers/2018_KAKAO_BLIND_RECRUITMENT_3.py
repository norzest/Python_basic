# 2018 KAKAO BLIND RECRUITMENT - [1차] 뉴스 클러스터링

def solution(str1, str2):

    def create_multi_dict(s):
        dict = {}
        for i in range(len(s) - 1):
            temp = s[i:i + 2]
            if temp.isalpha():
                temp = temp.upper()
                if temp in dict:
                    dict[temp] += 1
                else:
                    dict[temp] = 1
        return dict

    str1_d = create_multi_dict(str1)
    str2_d = create_multi_dict(str2)

    intrs = {}
    union = str2_d.copy()
    for key in str1_d:
        if key in str2_d:
            intrs[key] = min(str1_d[key], str2_d[key])
            union[key] = max(str1_d[key], str2_d[key])
        else:
            union[key] = str1_d[key]

    if sum(union.values()) == 0:
        return 65536
    else:
        return int((sum(intrs.values())/sum(union.values())) * 65536)


if __name__ == "__main__":
    print(solution("FRANCE", "french"))
    print('------------------')
    print(solution("handshake", "shake hands"))
    print('------------------')
    print(solution("aa1+aa2", "AAAA12"))
    print('------------------')
    print(solution("E=M*C^2", "e=m*c^2"))
    print('------------------')
