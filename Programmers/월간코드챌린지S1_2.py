# 월간 코드 챌린지 시즌1 - 3진법 뒤집기

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


def solution(n):
    tri_reverse = convert(n, 3)[::-1]
    return int(tri_reverse, 3)


if __name__ == "__main__":
    print(solution(45))
    print(solution(125))
