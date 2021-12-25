# 2231 분해합

n = int(input())
m = 1
cnt = 1
while True:
    if n <= m:
        print(cnt)
        break
    else:
        m = m + (6 * cnt)
        cnt += 1

