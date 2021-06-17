h, m, s = map(int, input("시 분 초>>").split())
print(h*3600 + m*60 + s)
print(divmod(s, 60))