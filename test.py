# 2018 KAKAO BLIND RECRUITMENT - 방금그곡


def solution(m, musicinfos):
    answer = []

    # '#'이 붙은 음을 소문자로 치환
    m = list(m)
    for i in range(len(m)):
        if m[i] == '#':
            m[i-1] = m[i-1].lower()
    m = ''.join(m)
    m = m.replace('#', "")

    for musicInfo in musicinfos:
        # 곡의 정보들을 , 를 구분으로 분할
        info = musicInfo.split(",")
        # 곡의 재생 시간
        run = int(info[1][3:]) - int(info[0][3:])
        while run < 0:
            run += 60
        diff = int(info[1][:2]) - int(info[0][:2])
        if diff > 1:
            run += 60 * (diff - 1)

        # 악보를 음 별로 분할
        lst = []
        for i in info[3]:
            if i != '#':
                lst.append(i)
            else:
                # '#'이 붙은 음을 소문자로 치환
                lst[-1] = lst[-1].lower()
        lst = ''.join(lst)
        # 곡의 길이
        n = len(lst)
        # 실제 재생한 악보
        play = ''.join((lst * (run // n)) + lst[:run % n])

        if m in play:
            answer.append(info[2])

    # 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다.
    # 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
    return answer


if __name__ == "__main__":
    print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
    print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
    print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
    # print(solution("ABC", ["10:50,12:10,HELLO,C#DEFGAB"]))
