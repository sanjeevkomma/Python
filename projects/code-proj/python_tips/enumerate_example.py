numbers = [1,4,6,3,4]
for number in numbers:
    print(number)

print('=============')

for index, number in enumerate(numbers): # enumberate help to get index
    print(f'{index} - {number}')
    # 0 - 1
    # 1 - 4
    # 2 - 6
    # 3 - 3
    # 4 - 4

print('=============')
values = list('aeiou')
for index, value in enumerate(values):
    print(f'{index} - {value}')
    # 0 - a
    # 1 - e
    # 2 - i
    # 3 - o
    # 4 - u
