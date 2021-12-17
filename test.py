# 2021 카카오 채용연계형 인턴쉽 - 표 편집


def solution(n, k, cmd):
    origin = [[i, i] for i in range(n)]  # 비교할 원본
    arr = origin.copy()  # 수정할 표
    deleted = []  # 삭제된 행

    for c in cmd:
        if c[0] == 'U':
            k -= int(c[2])
        elif c[0] == 'D':
            k += int(c[2])
        elif c[0] == 'C':
            print(arr)
        elif c[0] == 'Z':
            print(arr)

        print('---')

    answer = '---'
    return answer


if __name__ == "__main__":
    print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
    print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
