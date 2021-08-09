# 2021 카카오 채용연계형 인턴십 - 거리두기 확인하기

# BFS 로 풀어보기
from itertools import product


def solution(places):
    answer = []
    plc_len = 5

    for place in places:
        place = list(map(list, place))
        result = 1

        for x, y in product(range(plc_len), range(plc_len)):
            breaker = False
            # P 찾기
            if place[x][y] == 'P':
                # 맨해튼 거리 1 확인
                dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
                for i in range(4):
                    tx, ty = x + dx[i], y + dy[i]
                    if tx >= 0 and ty >= 0:
                        try:
                            if place[tx][ty] == 'P':
                                result = 0
                                breaker = True
                        except IndexError:
                            pass
                # 대각 확인
                dx, dy = [1, 1, -1, -1], [1, -1, 1, -1]
                for i in range(4):
                    tx, ty = x + dx[i], y + dy[i]
                    if tx >= 0 and ty >= 0:
                        try:
                            if place[tx][ty] == 'P':
                                if place[x][ty] == 'O' or place[tx][y] == 'O':
                                    result = 0
                                    breaker = True
                        except IndexError:
                            pass
                # 맨해튼 거리 2 확인
                # 세로 POP 일 경우
                try:
                    if x - 2 >= 0 and place[x - 2][y] == 'P' and place[x - 1][y] == 'O':
                        result = 0
                        breaker = True
                except IndexError:
                    pass
                try:
                    if place[x + 2][y] == 'P' and place[x + 1][y] == 'O':
                        result = 0
                        breaker = True
                except IndexError:
                    pass
                # 가로 POP 일 경우
                try:
                    if y - 2 >= 0 and place[x][y - 2] == 'P' and place[x][y - 1] == 'O':
                        result = 0
                        breaker = True
                except IndexError:
                    pass
                try:
                    if place[x][y + 2] == 'P' and place[x][y + 1] == 'O':
                        result = 0
                        breaker = True
                except IndexError:
                    pass

            if breaker:
                break

        answer.append(result)

    return answer


if __name__ == "__main__":
    print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"], ["OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"],
                    ["OOOOP", "OOOOO", "OOOOP", "OOOOO", "OOOOO"]]))
