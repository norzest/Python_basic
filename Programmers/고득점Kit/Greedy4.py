# 그리디 - 구명보트

def solution(people, limit):
    people.sort()
    answer = 0

    start = 0
    end = len(people) - 1
    while end - start >= 1:
        if people[end] + people[start] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1

        answer += 1

    if start == end:
        answer += 1

    return answer


if __name__ == "__main__":
    print(solution([70, 50, 80, 50], 100))
    print('-------------')
    print(solution([70, 80, 50], 100))
    print('-------------')
    print(solution([40, 50, 50, 59, 70], 100))
    print('-------------')