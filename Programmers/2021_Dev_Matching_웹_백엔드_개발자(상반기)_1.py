# 2021 Dev Matching 웹 백엔드 개발자(상반기) - 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    z = lottos.count(0)
    num = len(set(lottos).intersection(win_nums))
    return [7 - (z+num) if (z+num) >= 2 else 6, 7 - num if num >= 2 else 6]


if __name__ == "__main__":
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
    print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))


