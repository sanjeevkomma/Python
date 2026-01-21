numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
numbers.reverse() # in-place reverse
print(numbers) # ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'Zero']
print('=========')
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
for number in reversed(numbers):
    print(number)
# Nine
# Eight
# Seven
# Six
# Five
# Four
# Three
# Two
# One
# Zero
print('=========')
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
numbers.sort() # in-place sort
print(numbers) # ['Eight', 'Five', 'Four', 'Nine', 'One', 'Seven', 'Six', 'Three', 'Two', 'Zero']

print('=========')
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
for number in sorted(numbers):
    print(number)
# Eight
# Five
# Four
# Nine
# One
# Seven
# Six
# Three
# Two
# Zero
print('=========')
print(numbers) # ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']


print('=========')
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
for number in sorted(numbers,key=len):
    print(number)
# One
# Two
# Six
# Zero
# Four
# Five
# Nine
# Three
# Seven
# Eight

print('=========')
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
for number in sorted(numbers,key=len, reverse=True):
    print(number)
# Three
# Seven
# Eight
# Zero
# Four
# Five
# Nine
# One
# Two
# Six

print('=========')
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
numbers.sort(key=len, reverse=True)
print(numbers) # ['Three', 'Seven', 'Eight', 'Zero', 'Four', 'Five', 'Nine', 'One', 'Two', 'Six']

