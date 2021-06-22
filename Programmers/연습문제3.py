# 연습문제 - 같은 숫자는 싫어

def solution(arr):
    answer = []

    for num in arr:
        if answer:
            if answer[-1] != num:
                answer.append(num)
        else:
            answer.append(num)

    return answer


if __name__ == "__main__":
    print(solution([1, 1, 3, 3, 0, 1, 1]))
    print('-------------')
    print(solution(	[4, 4, 4, 3, 3]))
    print('-------------')
