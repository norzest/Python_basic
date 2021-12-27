# 2675 문자열 반복

n = range(int(input()))

for i in n:
    a, b = input().split()

    for j in range(len(b)):

        for k in range(int(a)):
            print(b[j], end='')

    print()

