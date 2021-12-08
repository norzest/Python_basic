# 2018 KAKAO BLIND RECRUITMENT - 셔틀버스


def solution(n, t, m, timetable):
    # 9시는 60분 * 9 이므로 540
    bus_time = [540 + (_ * t) for _ in range(n)]

    # 위와 같이 변환
    timetable.sort()
    for i in range(len(timetable)):
        temp = list(map(int, timetable[i].split(":")))
        timetable[i] = temp[0] * 60 + temp[1]

    num = 0
    while num < len(bus_time):
        bus = []
        num += 1

    answer = 540

    return ''.join([str(answer//60).zfill(2), ':', str(answer % 60).zfill(2)])


if __name__ == "__main__":
    print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
    print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
    print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
    print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
    print(solution(1, 1, 1, ["23:59"]))
    print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
