# 2021 KAKAO BLIND RECRUITMENT - 신규 아이디 추천

def solution(new_id):
    # 1단계 소문자 치환
    new_id = new_id.lower()

    # 2단계 특정 문자 제거
    temp = "abcdefghijklmnopqrstuvwxyz0123456789-_."
    new_id = ''.join(x for x in new_id if x in temp)

    # 3단계 연속된 마침표 제거
    new_id = ''.join(new_id[x] for x in range(len(new_id))
                     if not (new_id[x] == new_id[x-1] == '.'))

    # 4단계 처음과 끝의 마침표 제거
    new_id = new_id.strip(".")

    # 5단계 빈 문자열일 경우 a 대입
    new_id = new_id if new_id != '' else 'a'

    # 6단계 길이가 16자 이상일 경우 15로 만들기
    new_id = new_id if len(new_id) < 16 else new_id[:15].strip(".")

    # 7단계 길이가 2자 이하일 경우, 3이 될 때까지 반복
    if len(new_id) <= 2:
        while len(new_id) <= 2:
            new_id = ''.join([new_id, new_id[-1]])

    return new_id


if __name__ == "__main__":
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    print(solution("z-+.^."))




