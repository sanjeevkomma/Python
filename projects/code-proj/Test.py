print("Hello World")

city = 'Chicago'
print(city)

name: str = 'Alex'
print(name);

country: str = "USA"
print(country)
print(type(country))
print(country.lower())
print(country.capitalize())
print("india".capitalize())


x = 5
if x > 3 and x < 6:
    print(f"{x} is greater than 3")
elif x < 6:
    print(f"{x} is less than 6")

number = 5
if(number%2 == 0):
    isEven = True
else:
    isEven = False

isEven = True if number%2 == 0 else False
print(isEven)
