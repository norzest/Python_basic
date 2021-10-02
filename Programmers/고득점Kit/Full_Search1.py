# 완전탐색 - 모의고사

def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    answer = []

    for i in range(len(answers)):
        if answers[i] == one[i % 5]:
            score[0] += 1
        if answers[i] == two[i % 8]:
            score[1] += 1
        if answers[i] == three[i % 10]:
            score[2] += 1

    for a, b in enumerate(score):
        if b == max(score):
            answer.append(a+1)

    return answer


if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 5]))
    print(solution([1, 3, 2, 4, 2]))
