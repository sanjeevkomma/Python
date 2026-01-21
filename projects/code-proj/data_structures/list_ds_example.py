marks = [23,56,67]

print(sum(marks))
print(max(marks))
print(min(marks))
print(len(marks))

marks.append(76)
print(marks)

marks.insert(2,60)
print(marks)
marks.remove(60)
print(marks)
print(55 in marks)
print(56 in marks)
print(marks.index(67))
print(marks.index(69))



# --output--
# 146
# 67
# 23
# 3
# [23, 56, 67, 76]
# [23, 56, 60, 67, 76]
# [23, 56, 67, 76]
# False
# True
# 2
# ValueError: 69 is not in list
