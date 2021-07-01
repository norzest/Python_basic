# 2020 KAKAO BLIND RECRUITMENT - 문자열 압축

def solution(s):
    s_len = len(s)
    if s_len <= 2:  # aa 를 2a로 바꿔도 길이는 같다
        return s_len

    answer = 9999
    # 문자열 길이의 반을 넘겨 쪼갤 경우 압축이 불가능
    for i in range(1, int(s_len/2) + 1):
        # 쪼갠 문자열들을 저장할 임시 변수
        temp = [s[j:j+i] for j in range(0, s_len, i)]
        # 쪼갠 문자열들을 비교하여 압축한 결과물을 저장할 스택
        stacks = []
        for j in temp:
            # 스택이 비었을 경우 일단 추가
            if not stacks:
                stacks.append(j)
            else:
                # 앞에서 추가된 문자열과 현재 문자열이 같을 경우
                if stacks[-1] == j:
                    try:
                        # 문자열이 같은 상황이 이전에 나와서
                        # 문자 앞에 이미 숫자가 붙어있을 경우
                        if stacks[-2].isdigit():
                            stacks[-2] = str(int(stacks[-2]) + 1)
                        # 아닐 경우 2를 붙인다
                        else:
                            stacks.insert(-1, '2')
                    # 스택에 하나밖에 차있지 않을 경우
                    # [-2]는 존재하지 않기 가장 앞에 2 추가
                    except Exception:
                        stacks.insert(0, '2')
                else:
                    stacks.append(j)

        # 스택의 길이가 최소값이 맞는지 확인
        stacks_len = len(''.join(stacks))
        if answer > stacks_len:
            answer = stacks_len

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
