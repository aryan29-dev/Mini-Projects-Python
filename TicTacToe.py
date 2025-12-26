import random

class TicTacToe:
    def __init__(self):
        self.board = [str(x)[0] for x in range(9)]

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i * 3 + j], end=' ')
            print()

    def computer_play(self):
        while True:
            num = random.randrange(0, 9)
            if '0' <= self.board[num] <= '8':
                break
        self.board[num] = 'X'

    def move(self):
        while True:
            n = int(input("Your move? [0 - 8] "))
            if '0' <= self.board[n] <= '8':
                self.board[n] = '@'
                break
            else:
                print("Invalid move.")

    def check_win(self, c):
        for i in range(3):
            if self.board[3 * i] == self.board[3 * i + 1] == self.board[3 * i + 2] == c:
                return True
        for j in range(3):
            if self.board[j] == self.board[3 + j] == self.board[6 + j] == c:
                return True
        if (self.board[0] == self.board[4] == self.board[8] == c) or \
            (self.board[2] == self.board[4] == self.board[6] == c):
            return True

        return False

    def turn(self, n):
        if n % 2 == 0:
            self.computer_play()
            self.print_board()
        else:
            self.move()

    def game(self):
        for i in range(9):
            self.turn(i)
            if self.check_win('X'):
                print("I win!")
                return False
            elif self.check_win('@'):
                self.print_board()
                print("You win!")
                return True
        return None

print("Welcome to the game of Tic Tac Toe!")
board = TicTacToe()
r = board.game()
if r is None:
    print("Tied!")
