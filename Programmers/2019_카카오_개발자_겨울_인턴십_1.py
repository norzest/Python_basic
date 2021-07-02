# 2019 카카오 개발자 겨울 인턴십 - 튜플

import re


def solution(s):
    # 받은 문자열의 리스트화
    arr = [re.sub('{|}', '', i).split(',')
           for i in s.split('},{')]
    # 효율적인 탐색을 위한 이차원 배열의 길이를 기준으로 정렬
    arr.sort(key= len)
    
    answer = []
    for i in arr:
        for j in i:
            # 정렬되어있기 때문에 순서대로 리스트에 추가됀다
            if j not in answer:
                answer.append(j)

    return list(map(int, answer))


if __name__ == "__main__":
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    print('------')
    print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
    print('------')
    print(solution("{{20,111},{111}}"))
    print('------')
    print(solution("{{123}}"))
    print('------')
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
    print('------')
