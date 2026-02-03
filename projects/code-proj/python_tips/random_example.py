import random

print(random.random()) # 0.05554950128926606
print(random.randint(1, 10)) # generate any number between 1 & 10. 1 & 10 are inclusive
print(random.randrange(1,25,2))  # generate odd number
print(random.randrange(0,30,3))  # generate multiple of 3

ex_list = [2,7,9,34,56]
print(random.choice(ex_list))  # 7
print(random.choice('abcdefghijklmnopqrstuvwxyz'))  # p
print(random.sample(ex_list,3))  # [7, 34, 9]
