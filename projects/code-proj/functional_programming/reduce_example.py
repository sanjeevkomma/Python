from functools import reduce

numbers = [3,15,12,10]
print(sum(numbers)) # 40
print(max(numbers)) # 15
print(reduce(lambda x,y : x+y, numbers)) # 40
print(reduce(lambda x,y : x*y, numbers)) # 5400
print(reduce(lambda x,y : max(x,y), numbers)) # 15
print(reduce(lambda x,y : min(x,y), numbers)) # 3

words = ['Apple', 'Ant', 'Bat']
print(reduce(lambda x,y : x if len(x) > len(y) else y, words)) # Apple
