class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
class GameBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
 def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
def check_winner(self, symbol):
        for i in range(3):
            if all(self.board[i][j] == symbol for j in range(3)):
                return True
            if all(self.board[j][i] == symbol for j in range(3)):
                return True
        if all(self.board[i][i] == symbol for i in range(3)) or all(self.board[i][2 - i] == symbol for i in range(3)):
            return True
        return False
    def is_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def make_move(self, row, col, symbol):
        if self.board[row][col] == ' ':
            self.board[row][col] = symbol
            return True
        else:
            print("Invalid move. Try again.")
            return False
