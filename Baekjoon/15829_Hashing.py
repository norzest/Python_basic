# 15829 Hashing

r = 31
M = 1234567891

L = range(int(input()))
S = input()

answer = 0
for i in L:
    answer += (ord(S[i]) - 96) * (r ** i)

print(answer % M)
