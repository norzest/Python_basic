temp = '123'

while len(temp) <= 5:
    temp = temp.join(temp[-1])
    print(temp)