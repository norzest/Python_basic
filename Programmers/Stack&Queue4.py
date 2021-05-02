# 스택/큐 - 프린터

def solution(priorities, location):
    answer = 0

    while priorities:
        temp = priorities.pop(0)

        if priorities and temp < max(priorities):
            priorities.append(temp)
            if location != 0:
                location -= 1
            else:
                location = len(priorities) - 1
        else:
            answer += 1
            if location == 0 or len(priorities) == 0:
                return answer

            if location != 0:
                location -= 1
            else:
                location = len(priorities) - 1


if __name__ == "__main__":
    print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))
    print(solution([1, 2], 0))
