squares_first_ten_numbers = [ i*i for i in range(11) ] # List Comprehension
print(squares_first_ten_numbers) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(type(squares_first_ten_numbers)) # <class 'list'>

#squares_first_ten_numbers_set = set(squares_first_ten_numbers)
squares_first_ten_numbers_set = { i*i for i in range(11) } # Set Comprehension
print(squares_first_ten_numbers_set) # {0, 1, 64, 4, 36, 100, 9, 16, 49, 81, 25}
print(type(squares_first_ten_numbers_set)) # <class 'set'>

squares_first_ten_numbers_dict = { i:i*i for i in range(11) } # Dictionary Comprehension
print(type(squares_first_ten_numbers_dict)) # <class 'dict'>
print(squares_first_ten_numbers_dict) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

print(type([])) # <class 'list'>
print(type({})) # <class 'dict'>
print(type(set())) # <class 'set'>
print(type({1})) # <class 'set'>
print(type({'A':5})) # <class 'dict'>
print(type(())) # <class 'tuple'>
print(type((1,2,3))) # <class 'tuple'>
