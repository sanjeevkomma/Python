print('==as Stack====')
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)

print(numbers.pop()) # 4
print(numbers) # [1, 2, 3]
print(numbers.pop()) # 3
numbers.append(10)
print(numbers) # [1, 2, 10]
print(numbers.pop()) # 10
print(numbers) # [1, 2]

print('==as Queue====')
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
print(numbers.pop(0)) # 1
print(numbers.pop(0)) # 2
numbers.append(10)
print(numbers.pop(0)) # 3
print(numbers) # [4, 10]
