# 2018 KAKAO BLIND RECRUITMENT - 방금그곡


def solution(m, musicinfos):
    answer = "(None)"
    runtime = 99999

    # m에서 '#'이 붙은 음을 소문자로 치환
    token = ['C#', 'D#', 'F#', 'G#', 'A#']
    for t in token:
        m = m.replace(t, t[0].lower())

    for musicInfo in musicinfos:
        # 곡의 정보들을 , 를 구분으로 분할
        info = musicInfo.split(",")
        # 곡의 재생 시간
        run = int(info[1][3:]) - int(info[0][3:])
        # 11:50 부터 13:10 일 경우 시간당 60분을 추가해야 하므로
        diff = int(info[1][:2]) - int(info[0][:2])
        run += diff*60

        # 방송된 곡에서 '#'이 붙은 음을 소문자로 치환
        for t in token:
            info[3] = info[3].replace(t, t[0].lower())
        # 곡의 길이
        n = len(info[3])
        # 실제 재생한 악보
        play = ''.join((info[3] * (run // n)) + info[3][:run % n])

        # 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다.
        # 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
        if m in play:
            if answer == "(None)" or runtime < run:
                answer = info[2]
                runtime = run

    return answer


if __name__ == "__main__":
    print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
    print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
    print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
    print(solution("ABC", ["10:50,12:10,HELLO,C#DEFGAB"]))
