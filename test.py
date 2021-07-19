# 2021 카카오 채용연계형 인턴십 - 거리두기 확인하기

def solution(places):
    answer = []

    for place in places:
        place = list(map(list, place))
        for plc in place:
            for p in plc:
                print(p, end='')
            print()

        print('----')

    return answer


if __name__ == "__main__":
    print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
