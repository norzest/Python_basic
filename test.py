# 1234 제목

n = range(int(input()))

for i in n:
    ip = list(map(int, input().split()))
    h = ip[2] % ip[0]
    w = ip[2] // ip[0] + 1
    print(h * 100, w)
