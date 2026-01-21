from abc import ABC, abstractmethod

class GamingConsole(ABC):
    @abstractmethod
    def up(self):
        pass
    @abstractmethod
    def down(self):
        pass
    @abstractmethod
    def left(self):
        pass
    @abstractmethod
    def right(self):
        pass

class MarioGame(GamingConsole):
    def up(self):
        print('jump')
    def down(self):
        print('goes into a hole')
    def left(self):
        pass
    def right(self):
        print('go forward')

class ChessGame(GamingConsole):
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

# --outut--
# jump
# goes into a hole
# go forward
# ChessGame up
# ChessGame down
# ChessGame left
# ChessGame right
