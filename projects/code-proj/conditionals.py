i = 45
if i: print("Something")
if 0: print("Zero") #It won't print as The condition is False as its Zero. Its True for Non-Zero
print(bool(45))
print(bool(-1))
print(bool(1))
print(bool(0))
print(bool(0.0))
print(bool(-1.0))
print(bool("Test"))
print(bool(""))
print(bool(''))
print(bool([]))
if i%2 : print("odd")
else: print("even")

i = 44
if i%2 : print("odd")
else: print("even")
# ---output-----
# Something
# True
# True
# True
# False
# False
# True
# True
# False
# False
# False
# odd
# even
