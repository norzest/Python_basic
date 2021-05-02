# 정렬 - K번째 수

def solution(array, commands):
    answer = []

    for i in commands:
        answer.append(sorted(array[i[0]-1:i[1]])[i[2]-1])

    return answer


if __name__ == "__main__":
    aa = [1, 5, 2, 6, 3, 7, 4]
    bb = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(aa, bb))
