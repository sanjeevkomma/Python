#Dictionay = Key-Value pair
occurrences = dict(a=5, b=6, c=8)
print(occurrences)  # {'a': 5, 'b': 6, 'c': 8}
print(occurrences['a']) # 5
print(occurrences['b'])  # 6
print(type(occurrences)) # <class 'dict'>
print(occurrences.get('b')) # 6
occurrences['e']=10
print(occurrences) # {'a': 5, 'b': 6, 'c': 8, 'e': 10}
# print(occurrences['z']) # KeyError: 'z'
print(occurrences.get('z')) # None
print(occurrences.get('z',20)) # 20
print(occurrences) # {'a': 5, 'b': 6, 'c': 8, 'e': 10}
print(occurrences.keys()) # dict_keys(['a', 'b', 'c', 'e'])
print(occurrences.values()) # dict_values([5, 6, 8, 10])
print(occurrences.items()) # dict_items([('a', 5), ('b', 6), ('c', 8), ('e', 10)])  # Its Tuple
for (key, value) in occurrences.items():
    print(f"{key} {value}")
# a 5
# b 6
# c 8
# e 10
occurrences['a']=14
print(occurrences) # {'a': 14, 'b': 6, 'c': 8, 'e': 10}
del occurrences['a']
print(occurrences) # {'b': 6, 'c': 8, 'e': 10}
