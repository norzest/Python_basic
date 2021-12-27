# 2798 블랙잭

from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0
for lst in list(combinations(cards, 3)):
    temp = sum(lst)
    if answer < temp <= m:
        answer = temp

print(answer)
