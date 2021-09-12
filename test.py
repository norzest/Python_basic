# 월간 코드 챌린지 시즌 1 - 쿼드압축 후 개수 세기


def solution(arr):
    def quadtree(x, y, n):
        # 해당 사각형의 가장 처음 수
        num = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                # 그 수와 하나라도 같지 않으면 압축 불가
                if arr[i][j] != num:
                    half = n//2
                    quadtree(x, y, half)
                    quadtree(x, y + half, half)
                    quadtree(x + half, y, half)
                    quadtree(x + half, y + half, half)
                    return
        # 전부 같으므로 그 부분은 더이상 압축하지않고 카운트
        else:
            answer[num] += 1

    answer = [0, 0]
    quadtree(0, 0, len(arr))
    return answer


if __name__ == "__main__":
    print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
    print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]))
