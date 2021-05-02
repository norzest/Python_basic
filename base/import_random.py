import random


x = random.randint(1, 100)

while x % 3 != 0:
    x += 1

print(x)

cards = [1, 2, 3, 4, 5]
print(random.choices(cards, k=3))

e_list = [10, 20, 30, 40, 50]
print(random.sample(e_list, 3))