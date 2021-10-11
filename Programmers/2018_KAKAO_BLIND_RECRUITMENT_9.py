# 2018 KAKAO BLIND RECRUITMENT - n진수 게임


def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


def solution(n, t, m, p):
    # 말해야 할 숫자를 담은 배열
    arr = ''
    num = t * m

    for i in range(num):
        arr = ''.join([arr, str(convert(i, n))])

    return arr[p - 1:num:m]


if __name__ == "__main__":
    print(solution(2, 4, 2, 1))
    print(solution(16, 16, 2, 1))
    print(solution(16, 16, 2, 2))