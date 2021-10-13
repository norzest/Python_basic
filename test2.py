def quadratic(a,b,c):
    D = ((b**2)-4*a*c)**0.5
    x = (-b + D) / 2*a
    y = (-b - D) / 2*a
    print('X1:{}, X2:{}'.format(x,y))


quadratic(4, 0, 0)