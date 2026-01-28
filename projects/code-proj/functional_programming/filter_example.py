numbers = [1, 89,54,35]
print(numbers) # [1, 89, 54, 35]

print(list(filter(lambda x: x % 2 == 1, numbers))) # [1, 89, 35]
print(list(filter(lambda x: x % 2 == 0, numbers))) # [54]
print(list(filter(lambda x: x % 2, numbers))) # [1, 89, 35]

words = ["apple", "banana", "cherry", "Ant", "bat"]
print(words)
print(list(filter(lambda word: word.endswith('ry'), words))) # ['cherry']
print(list(filter(lambda word : len(word) == 3, words))) # ['Ant', 'bat']
print(list(filter(lambda word:word.startswith('ap') , words))) # ['apple']
