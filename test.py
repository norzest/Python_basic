# 2775 부녀회장이 될테야

for t in range(int(input())):
    k = int(input())
    n = int(input())

    arr = [i+1 for i in range(n)]  # 0층

    for i in range(k):
        arr = [sum(arr[:j+1]) for j in range(n)]

    print(arr[-1])
