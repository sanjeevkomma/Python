class Planet:
    pass

earth = Planet()
mars = Planet()

earth.name = 'Earth'
earth.speed = 20

print(earth.name)
print(earth.speed)

mars.name = 'Mars'
print(mars.name)

#Moter
class Moter:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        
moter1 = Moter('Moter1', 20)
print(moter1.name)

moter2 = Moter('Moter2', 30)
print(moter2.name)

moter1.distance = 1000
print(moter1.distance)

# ---ouput--
# Earth
# 20
# Mars
# Moter1
# Moter2
# 1000
