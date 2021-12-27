# 9506 약수들의 합

while True:
    n = int(input())
    arr = []

    if n == -1:
        break

    for i in range(1, (n//2) + 1):
        if not n % i:
            arr.append(i)

    if sum(arr) == n:
        print(n, '=', arr[0], end='')
        for j in arr[1:]:
            print(' +', j, end='')
        print()
    else:
        print(f'{n} is NOT perfect.')