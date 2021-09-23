# Summer/Winter Coding(~2018) - 방문 길이


def solution(dirs):
    answer = 0
    # 좌표 평면의 최대 x, y 값
    n = 5
    # 방문한 좌표를 저장할 집합
    visited = set()
    # 현재 xy 값
    x, y = 0, 0

    for d in dirs:
        # 이동할 xy 값
        nx, ny = x, y

        if d == "U":
            ny += 1
        elif d == "D":
            ny -= 1
        elif d == "R":
            nx += 1
        elif d == "L":
            nx -= 1

        # 좌표를 벗어났으면 다음 문장은 실행 x
        if nx < -n or nx > n or ny < -n or ny > n:
            continue

        # 어디서 어디로 이동했는지 집합에 추가
        # 반대 방향도 같은 취급이므로 같이 추가
        if (x, y, nx, ny) not in visited:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            answer += 1

        x, y = nx, ny

    return answer


if __name__ == "__main__":
    print(solution("ULURRDLLU"))
    print(solution("LULLLLLLU"))
    print(solution("DU"))
