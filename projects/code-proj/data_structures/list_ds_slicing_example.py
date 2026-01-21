numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

print(len(numbers)) # 10
print(numbers[2]) # Two

#This is called Slicing
print(numbers[2:6]) # ['Two', 'Three', 'Four', 'Five']
print(numbers[:6]) # ['Zero', 'One', 'Two', 'Three', 'Four', 'Five']
print(numbers[3:]) # ['Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
print(numbers[1:8:2]) # ['One', 'Three', 'Five', 'Seven']
print(numbers[1:8:3]) # ['One', 'Four', 'Seven']
print(numbers[::3])  # ['Zero', 'Three', 'Six', 'Nine']
print(numbers[::-1]) # ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'Zero']
print(numbers[::-3]) # ['Nine', 'Six', 'Three', 'Zero']
del numbers[3:]
print(numbers)  # ['Zero', 'One', 'Two']
del numbers[1:2]
print(numbers) # ['Zero', 'Two']

numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
numbers[3:7] = [3,4,5,6]
print(numbers) # ['Zero', 'One', 'Two', 3, 4, 5, 6, 'Seven', 'Eight', 'Nine']
