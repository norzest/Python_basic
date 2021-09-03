# 2018 KAKAO BLIND RECRUITMENT - 프렌즈4블록


def solution(m, n, board):
    board = [list(_) for _ in board]
    answer = 0

    while True:
        # 같은 모양의 2x2 블록을 찾으면 1로 표시
        removed = [[0] * n for _ in range(m)]

        for i in range(m - 1):
            for j in range(n - 1):
                # 아직 지워지지 않은 블록이면
                if board[i][j] != 0:
                    # 2x2 블록이면
                    if board[i][j] == board[i][j+1]:
                        if board[i][j] == board[i+1][j]:
                            if board[i][j] == board[i+1][j+1]:
                                # removed 배열에 1로 표시
                                removed[i][j], removed[i][j+1], removed[i+1][j], removed[i+1][j+1] = 1, 1, 1, 1

        # 지워진 블록의 갯수
        count = 0
        for i in range(m):
            count += sum(removed[i])

        # 지워진 블록이 없을 경우 종료
        if count == 0:
            break

        answer += count

        # removed 에 표시됀 블록 board 에서 제거(0 으로 표시)
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if removed[i][j] == 1:
                    temp = i - 1

                    while temp >= 0 and removed[temp][j] == 1:
                        temp -= 1
                    if temp < 0:
                        board[i][j] = 0
                    else:
                        board[i][j] = board[temp][j]
                        removed[temp][j] = 1

    return answer


if __name__ == "__main__":
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
