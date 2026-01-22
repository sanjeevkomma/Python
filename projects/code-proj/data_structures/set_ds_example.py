numbers = [1,2,3,2,1]
print(numbers) # [1, 2, 3, 2, 1]
numbers_set = set(numbers)
print(numbers_set) # {1, 2, 3}
numbers_set.add(3)
numbers_set.add(4)
print(numbers_set) # {1, 2, 3, 4}
numbers_set.remove(2)
print(numbers_set) # {1, 3, 4}
#print(numbers_set[0]) # TypeError: 'set' object is not subscriptable
print(1 in numbers_set) # True
print(5 in numbers_set) # False
print(min(numbers_set)) # 1
print(max(numbers_set)) # 4
print(sum(numbers_set))  # 8
print(len(numbers_set))  # 3

numbers_1_to_5_set = set(range(1, 6))
print(numbers_1_to_5_set) # {1, 2, 3, 4, 5}
numbers_4_to_10_set = set(range(4, 11))
print(numbers_4_to_10_set) # {4, 5, 6, 7, 8, 9, 10}
print(numbers_1_to_5_set | numbers_4_to_10_set) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} , UNION
print(numbers_1_to_5_set & numbers_4_to_10_set) # {4, 5} , INTERSECTION
print(numbers_1_to_5_set - numbers_4_to_10_set) # {1, 2, 3}
print(numbers_1_to_5_set ^ numbers_4_to_10_set) # {1, 2, 3, 6, 7, 8, 9, 10}

