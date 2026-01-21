animals = ['dog', 'cat', 'elephant']

print(len(animals)) # 3
#print(sum(animals)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
animals.append('Fish')
print(animals) # ['dog', 'cat', 'elephant', 'Fish']
animals.remove('cat')
print(animals) # ['dog', 'elephant', 'Fish']
print(animals[2]) # Fish
del animals[2]
print(animals) # ['dog', 'elephant']
animals.extend('Fish')
print(animals) # ['dog', 'elephant', 'F', 'i', 's', 'h']
animals.extend(['Giraffe','Horse'])
print(animals) # ['dog', 'elephant', 'F', 'i', 's', 'h', 'Giraffe', 'Horse']
animals = animals + ['Jackal','Kangaroo']
print(animals) # ['dog', 'elephant', 'F', 'i', 's', 'h', 'Giraffe', 'Horse', 'Jackal', 'Kangaroo']
animals += ['Lion','Monkey']
print(animals) # ['dog', 'elephant', 'F', 'i', 's', 'h', 'Giraffe', 'Horse', 'Jackal', 'Kangaroo', 'Lion', 'Monkey']
animals.append(10)
print(animals) # ['dog', 'elephant', 'F', 'i', 's', 'h', 'Giraffe', 'Horse', 'Jackal', 'Kangaroo', 'Lion', 'Monkey', 10]
