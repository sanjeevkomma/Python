from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
point1 = Point(1, 2)
print(point1) # Point(x=1, y=2)
print(point1.x, point1.y) # 1 2
