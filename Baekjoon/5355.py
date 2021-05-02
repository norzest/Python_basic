# 5355 화성 수학

def cal(base, b):
    if b == '@':
        return float(base) * 3
    elif b == '%':
        return float(base) + 5
    elif b == '#':
        return float(base) - 7
    else:
        return float(base)


n = range(int(input()))

for i in n:
    a = input().split()

    for j in a:
        a[0] = cal(a[0], j)

    print('%0.2f' % a[0])