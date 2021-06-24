# 연습문제 - 수박수박수박수박수박수?

def solution(n):
    s = '수박' * n
    return s[:n]


if __name__ == "__main__":
    print(solution(3))
    print('-------------')
    print(solution(4))
    print('-------------')
