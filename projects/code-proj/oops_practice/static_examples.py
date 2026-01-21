class Player:
    count = 0 # Any class level variable is Static by default in Python

    def __init__(self, name):
        self.name = name
        Player.count += 1

messi = Player('Messi')
ronaldo = Player('Ronaldo')

print(Player.count) # 2

messi.count = 100
print(Player.count) # 2
print(messi.count) # 100

# --output--
# 2
# 2
# 100
