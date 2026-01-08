number1 = int(input("Enter Number1:"))
number2 = int(input("Enter Number2:"))

print("Choices Available are")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")

choice = int(input("Enter your choice: "))
if choice == 1:
    print(f"Result = {number1 + number2}")
elif choice == 2:
    print(number1 - number2)
elif choice == 3:
    print(number1 * number2)
else:
    print("Invalid Choice")
