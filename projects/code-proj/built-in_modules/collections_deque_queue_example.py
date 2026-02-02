from collections import deque
queue = deque(['Zero', 'One', 'Two', 'Three', 'Four', 'Five'])
print(queue) # deque(['Zero', 'One', 'Two', 'Three', 'Four', 'Five'])
print(queue.pop()) # Five
print(queue) # deque(['Zero', 'One', 'Two', 'Three', 'Four'])
queue.append('Six')
print(queue) # deque(['Zero', 'One', 'Two', 'Three', 'Four', 'Six'])
queue.appendleft('Seven')
print(queue) # deque(['Seven', 'Zero', 'One', 'Two', 'Three', 'Four', 'Six'])
print(queue.pop()) # Six
queue.popleft()
print(queue) # deque(['Zero', 'One', 'Two', 'Three', 'Four'])
