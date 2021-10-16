# 2018 KAKAO BLIND RECRUITMENT - 추석 트래픽


def solution(lines):
    def get_end_time(time):
        h = int(time[:2]) * 3600  # 시간
        m = int(time[3:5]) * 60  # 분
        s = int(time[6:8])  # 초
        ms = int(time[9:])  # 밀리 초
        return (h + m + s) * 1000 + ms  # 시간을 밀리초 기준으로 변환

    def get_start_time(time, t):
        return time - int(float(t) * 1000) + 1

    start = []  # 시작 시간 리스트
    end = []  # 끝나는 시간 리스트

    for line in lines:
        temp_split = line.split(' ')
        end.append(get_end_time(temp_split[1]))
        start.append(get_start_time(end[-1], temp_split[2][:-1]))

    answer = 0
    lines_len = len(lines)
    for i in range(lines_len):
        count = 0
        cur_time = end[i]
        for j in range(i, lines_len):
            # 1초 안지났으면 +1
            if cur_time > start[j] - 1000:
                count += 1

        answer = max(answer, count)

    return answer


if __name__ == "__main__":
    print(solution(["2016-09-15 00:00:00.000 3s"]))
    print(solution(["2016-09-15 23:59:59.999 0.001s"]))
    print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
    print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
    print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))
    print(solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]))
