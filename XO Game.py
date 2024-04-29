# Define a class for players
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
# Define a class for the game board
class GameBoard:
    def __init__(self):
        # Initialize an empty 3x3 board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
 # Method to display the current state of the board
 def display(self):
        for row in self.board:
            print('|'.join(row))# Print each row of the board
            print('-' * 5)# Print a separator line
# Method to check if a player has won
def check_winner(self, symbol):
        for i in range(3):
               # Check rows and columns for a winning pattern
            if all(self.board[i][j] == symbol for j in range(3)):
                return True
            if all(self.board[j][i] == symbol for j in range(3)):
                return True
             # Check diagonals for a winning pattern
        if all(self.board[i][i] == symbol for i in range(3)) or all(self.board[i][2 - i] == symbol for i in range(3)):
            return True
        return False
    # Method to check if the board is full
    def is_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))
     # Method to make a move on the board
    def make_move(self, row, col, symbol):
        if self.board[row][col] == ' ':
            self.board[row][col] = symbol
            return True
        else:
            print("Invalid move. Try again.")
            return False
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = GameBoard()
 def start(self):
        current_player = self.player1
        while True:
            print(f"{current_player.name}'s turn ({current_player.symbol})")
            self.board.display()
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if self.board.make_move(row, col, current_player.symbol):
                if self.board.check_winner(current_player.symbol):
                    print(f"Congratulations! {current_player.name} wins!")
                    break
                elif self.board.is_full():
                    print("It's a tie!")
                    break
                else:
                    current_player = self.player2 if current_player == self.player1 else self.player1
player1 = Player("Player 1", 'X')
player2 = Player("Player 2", 'O')
game = Game(player1, player2)
game.start()
