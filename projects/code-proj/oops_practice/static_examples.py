class Player:
    count = 0 # Any class level variable is Static by default in Python

    def __init__(self, name):
        self.name = name
        Player.count += 1

    @staticmethod
    def get_count():
        return Player.count

messi = Player('Messi')
ronaldo = Player('Ronaldo')

print(Player.count) # 2

messi.count = 100
print(Player.count) # 2
print(messi.count) # 100

print('==========')
print(messi.get_count())
print(ronaldo.get_count())
print(Player.get_count())

# --output--
# 2
# 2
# 100
# ==========
# 2
# 2
# 2
