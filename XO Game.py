class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
class GameBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

