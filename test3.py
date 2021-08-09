def drawing_pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1), '*' * (1 + (i * 2)))


inp = 1
while inp > 0:
    try:
        inp = int(input('양의 정수만 입력: '))
        drawing_pyramid(inp)
    except ValueError:
        print('양의 정수를 입력해 주세요')

##############################

while True:
    inp = input('양의 정수만 입력: ')
    if inp.isdigit():
        drawing_pyramid(int(inp))
    else:
        print('양의 정수를 입력해 주세요')
        break
