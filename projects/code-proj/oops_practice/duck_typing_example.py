from abc import ABC, abstractmethod

# class GamingConsole(ABC):
#     @abstractmethod
#     def up(self):
#         pass
#     @abstractmethod
#     def down(self):
#         pass
#     @abstractmethod
#     def left(self):
#         pass
#     @abstractmethod
#     def right(self):
#         pass

class MarioGame():
    def up(self):
        print('jump')
    def down(self):
        print('goes into a hole')
    def left(self):
        pass
    def right(self):
        print('go forward')

class ChessGame():
    def up(self):
        print('ChessGame up')
    def down(self):
        print('ChessGame down')
    def left(self):
        print('ChessGame left')
    def right(self):
        print('ChessGame right')

marioGame = MarioGame()
marioGame.up()
marioGame.down()
marioGame.left()
marioGame.right()

chessGame = ChessGame()
chessGame.up()
chessGame.down()
chessGame.left()
chessGame.right()

print('==========')

# Polymorphism
games = [MarioGame(), ChessGame()]
for game in games:
    game.up()
    game.down()
    game.left()
    game.right()

print('==========')

class Test1:
    def method(self): print('Test1')

class Test2:
    def method(self): print('Test2')

tests = [Test1(), Test2()]
for test in tests:
    test.method()


# --output--
# jump
# goes into a hole
# go forward
# ChessGame up
# ChessGame down
# ChessGame left
# ChessGame right
# ==========
# jump
# goes into a hole
# go forward
# ChessGame up
# ChessGame down
# ChessGame left
# ChessGame right
# ==========
# Test1
# Test2
