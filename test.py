# 2018 KAKAO BLIND RECRUITMENT - 방금그곡


def solution(m, musicinfos):
    answer = "(None)"

    for musicInfo in musicinfos:
        # 곡의 정보들을 , 를 구분으로 분할
        info = musicInfo.split(",")
        # 곡의 길이
        n = len(info[3])
        # 곡의 재생 시간
        run = int(info[1][3:]) - int(info[0][3:])
        while run < 0:
            run += 60
        diff = int(info[1][:2]) - int(info[0][:2])
        if diff > 1:
            run += 60 * (diff - 1)
        print(info[3])

    return answer


if __name__ == "__main__":
    print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
    print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
    print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
    print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
    # print(solution("ABC", ["10:50,12:10,HELLO,C#DEFGAB"]))
