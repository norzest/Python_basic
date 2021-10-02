# 동적계획법 - n으로 표현

def solution(N, number):
    answer = -1
    DP = []

    for i in range(1, 9):
        numbers = set()
        numbers.add(int(str(N) * i))

        for j in range(0, i - 1):
            for x in DP[j]:
                for y in DP[-j - 1]:
                    print(x, y, numbers)
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)

                    if y != 0:
                        numbers.add(x // y)
                    print(numbers)

        if number in numbers:
            answer = i
            break

        DP.append(numbers)

    return answer


if __name__ == "__main__":
    print(solution(5, 5))
    print('-------------')
    print(solution(5, 10))
    print('-------------')
    print(solution(3, 4))
