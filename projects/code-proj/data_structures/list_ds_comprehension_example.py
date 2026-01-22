numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

numbers_length_four=[]
for number in numbers:
    if len(number)==4:
        numbers_length_four.append(number)

print(numbers_length_four) # ['Zero', 'Four', 'Five', 'Nine']

print('===========')
numbers_length_four = [number for number in numbers]
print(numbers_length_four) # ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

print('===========')
numbers_length_four = [len(number) for number in numbers]
print(numbers_length_four) # [4, 3, 3, 5, 4, 4, 3, 5, 5, 4]

print('===========')
numbers_length_four = [number.upper() for number in numbers]
print(numbers_length_four) # ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

print('===========')
numbers_length_four = [ number for number in numbers if len(number)==4] # List Comprehension
print(numbers_length_four) # ['Zero', 'Four', 'Five', 'Nine']

print('===========')
values = [3,6,9,1,4,15,6,3]
values_even = [value for value in values if value%2==0] # List Comprehension
print(values_even) # [6, 4, 6]

print('===========')
values_odd = [value for value in values if value%2==1] # List Comprehension
print(values_odd) # [3, 9, 1, 15, 3]
