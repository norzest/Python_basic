# 1259 팰린드롬수

while True:
    ip = input()

    if ip == '0':
        break

    if ip == ip[::-1]:
        print('yes')
    else:
        print('no')
