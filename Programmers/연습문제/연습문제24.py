# 연습문제 - 콜라츠 추측

def solution(num):
    for i in range(500):
        if num == 1:
            return i
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
    else:
        return -1


if __name__ == "__main__":
    print(solution(6))
    print('-------------')
    print(solution(16))
    print('-------------')
    print(solution(626331))
    print('-------------')
