# 10817 세 수

def second_largest_num(num):
    second = first = -float('inf')

    for i in num:
        if int(i) >= first:
            second = first
            first = int(i)
        elif second <= int(i) <= first:
            second = int(i)

    print(second)


a = input().split()

second_largest_num(a)