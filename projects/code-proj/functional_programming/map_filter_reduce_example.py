from functools import reduce

numbers = [3,7,8,15,24,35,46]

print(reduce(lambda x,y : x + y , map(lambda x:x ** 2, filter(lambda x : x%2 == 0, numbers)))) # 2756
