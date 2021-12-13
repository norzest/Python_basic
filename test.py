# 2018 KAKAO BLIND RECRUITMENT - 셔틀버스


def solution(n, t, m, timetable):
    # 9시는 60분 * 9 이므로 540
    # 버스 출발 시간 리스트
    bus_time = [540 + (_ * t) for _ in range(n)]

    # 위와 같이 변환
    timetable.sort()
    for i in range(len(timetable)):
        temp = list(map(int, timetable[i].split(":")))
        timetable[i] = temp[0] * 60 + temp[1]

    answer = 0
    num = 0  # num 번째 버스
    while num < len(bus_time):
        bus = []  # 현재 버스
        people_count = 0  # 현재 정원

        # 정원이 찰 때까지
        while people_count < m:
            timetable_len = len(timetable)

            # 아직 탈 인원이 존재하고, 출발시간 이전에 있던 사람이라면
            if timetable_len >= 1 and timetable[timetable_len-1] <= bus_time[num]:
                # 현재 버스에 탑승
                people_count += 1
                bus.append(timetable.pop())
            else:
                break

        # 마지막 버스일 경우
        if num == len(bus_time) - 1:
            # 정원이 다 찼다면
            if people_count == m:
                # 자신이 마지막에 탑승
                answer = bus.pop() - 1
            else:
                # 최대한 늦게
                answer = bus_time[num]

        num += 1

    # answer 를 다시 시간으로 변환
    hh = str(answer // 60)
    mm = str(answer % 60)
    return ''.join([hh.zfill(2), ":", mm.zfill(2)])


if __name__ == "__main__":
    print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
    print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
    print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
    print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
    print(solution(1, 1, 1, ["23:59"]))
    print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
