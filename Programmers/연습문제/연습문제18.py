# 연습문제 - 자연수 뒤집어 배열로 만들기

def solution(n):
    return list(map(int, str(n)))[::-1]


if __name__ == "__main__":
    print(solution(12345))
    print('-------------')
