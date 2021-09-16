move = [1, 0]

if move[0] == 0:
    move[0], move[1] = move[1], move[0]
elif move[1] == 0:
    move[0], move[1] = move[1], -move[0]

print(move)