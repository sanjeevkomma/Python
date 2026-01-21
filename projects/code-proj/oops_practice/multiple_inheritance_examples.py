class LandAnimal:
    def walk(self):
        print('walking')

class WaterAnimal:
    def swim(self):
        print('swimming')

class Amphibian(LandAnimal,WaterAnimal):
    pass

frog = Amphibian()

frog.walk()
frog.swim()

# --output--
# walking
# swimming
