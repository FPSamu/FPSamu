import random

lista = [range(100)]
tries = 0
num = 0
sum = 0
avg = 0

for x in range(100):
    while sum < 1:
        num=random.random()
        sum += num
        tries += 1

    lista[x] = tries
    tries = 0
    num = 0
    sum = 0

for x in range(10):
    avg += lista[x]

avg = avg/10

print(avg)

