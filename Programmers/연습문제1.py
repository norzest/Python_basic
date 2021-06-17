# 연습문제 - 2016년

import calendar


def solution(a, b):
    day_week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return day_week[calendar.weekday(2016, a, b)]


if __name__ == "__main__":
    print(solution(5, 24))
    print('-------------')