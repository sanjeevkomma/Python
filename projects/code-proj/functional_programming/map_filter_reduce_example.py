from functools import reduce

numbers = [3,7,8,15,24,35,46]

print(reduce(lambda x,y : x + y , map(lambda x:x ** 2, filter(lambda x : x%2 == 0, numbers)))) # 2756

months = [('Jan',31), ('Feb', 28), ('Mar', 31)]
tuple_ex = ('Dec',31)
print(tuple_ex[0]) # Dec
print(tuple_ex[1]) # 31
print(sum(map(lambda x: x[1] , months))) # 90
print(reduce(lambda x,y : x if x[1] < y[1] else y, months)) # ('Feb', 28)
print(reduce(lambda x,y : x if x[1] < y[1] else y, months)[0]) # Feb
