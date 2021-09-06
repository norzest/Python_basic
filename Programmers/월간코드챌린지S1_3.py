# 월간 코드 챌린지 시즌 1 - 삼각 달팽이

def solution(n):
    # 삼각형 배열 생성
    arr = [[0] * i for i in range(1, n + 1)]
    # 현재 위치
    di, dj = 0, 0
    # 해당 위치에 입력할 숫자
    num = 1
    # while 문 break controller
    breaker = True
    while breaker:
        # 아래로
        while di < n and arr[di][dj] == 0:
            arr[di][dj] = num
            num += 1
            di += 1

        # 오른쪽으로
        di -= 1
        dj += 1
        while dj < n and arr[di][dj] == 0:
            arr[di][dj] = num
            num += 1
            dj += 1

        # 위로
        dj -= 2
        di -= 1
        while di >= 0 and arr[di][dj] == 0:
            arr[di][dj] = num
            num += 1
            di -= 1
            dj -= 1

        # 다음 시작할 위치 지정
        di += 2
        dj += 1
        try:
            # 다음 시작 위치가 0이 아니면 끝
            if arr[di][dj] != 0:
                breaker = False
        except IndexError:
            breaker = False

    return sum(arr, [])


if __name__ == "__main__":
    print(solution(1))
    print(solution(2))
    print(solution(3))
    print(solution(4))
    print(solution(5))
    print(solution(6))