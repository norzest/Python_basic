# 2017 팁스타운 - 예상 대진표

def solution(n, a, b):
    p = 2
    ac, bc = 0, 0

    count = 0
    while p <= n:
        count += 1

        if a <= p and ac == 0:
            ac = count

        if b <= p and bc == 0:
            bc = count

        p *= 2

    print(ac, bc)

    return 0


if __name__ == "__main__":
    print(solution(8, 4, 7))
    print('---')
    print(solution(256, 46, 243))
    print('---')
    print(solution(2, 2, 1))
    print('---')
    print(solution(16, 14, 16))



