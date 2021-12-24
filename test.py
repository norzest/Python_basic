# 2231 분해합

n = int(input())
c = 0
for i in range(n):
    temp = [int(j) for j in str(i)]

    if i + sum(temp) == n:
        c = i
        break

print(c)
