def create_person():
    return 'John','1987','USA'

john = create_person()
print(type(john)) # <class 'tuple'>
print(john) # ('John', '1987', 'USA')
name, year, country = john # tuple unpacking or sequence unpacking
print(name) # John
print(year) # 1987
print(country) # USA

print(len(john)) # 3
print(john[0]) # John
print(john[1]) # 1987
print(john[2])  # USA

# john[1] = 1998 # TypeError: 'tuple' object does not support item assignment. Tuple is immutable by default

person = ('Sanjeev', 5, 'India')
print(type(person)) # <class 'tuple'>
name, age, country = person
# name,age = person # ValueError: too many values to unpack (expected 2)

# Swapping
x, y = 0, 1
print(x, y) # 0 1
x, y = y, x
print(x, y) # 1 0

x = (0)
print(type(x)) # <class 'int'>
x = (0,)
print(type(x)) # <class 'tuple'>
x = 1,
print(type(x)) # <class 'tuple'>
