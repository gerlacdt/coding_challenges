"""Connect 4 is a game where opponents take turns dropping red or
black discs into a 7x6 vertically suspended grid. The game ends either
when one player creates a line of four consecutive discs of their
color (horizontally, vertically, diagonally), or when there is no more
spots left in the grid.

nDesign and implement Connect 4.

"""

from collections import namedtuple


class Game:
    def __init__(self):
        self.board = [["." for _ in range(7)] for _ in range(6)]
        self.game_over = False
        self.winner = None
        self.last_move = None
        self.players = ["x", "o"]
        self.turn = 0

    def play(self):
        while not self.game_over:
            self.print_board()
            self.move(self.players[self.turn])
            self.check_win()
        self.print_outcome()

    def print_board(self):
        for row in self.board:
            print("".join(row))

    def move(self, player):
        col = input("{}'s turn to move: ".format(player))
        while not self.is_valid(col):
            col = input("Move not valid. Please try again.")

        row, col = 5, int(col)
        while self.board[row][col] != ".":
            row -= 1

        self.board[row][col] = player
        self.turn = 1 - self.turn
        self.last_move = (row, col)

    def is_valid(self, col):
        try:
            col = int(col)
        except ValueError:
            return False
        if 0 <= col <= 6 and self.board[0][col] == ".":
            return True
        else:
            return False

    def check_win(self):
        row, col = self.last_move
        horizontal = self.board[row]
        vertical = [self.board[i][col] for i in range(6)]

        neg_offset, pos_offset = col - row, col + row
        neg_diagonal = [
            row[i + neg_offset]
            for i, row in enumerate(self.board)
            if 0 <= i + neg_offset <= 6
        ]

        pos_diagonal = [
            row[-i + pos_offset]
            for i, row in enumerate(self.board)
            if 0 <= -i + pos_offset <= 6
        ]

        possible_wins = [horizontal, vertical, pos_diagonal, neg_diagonal]
        for p in possible_wins:
            for i in range(len(p) - 3):
                if len(set(p[i : i + 4])) == 1 and p[i] != ".":
                    self.game_over = True
                    self.winner = p[i]
                    break

        if all(self.board[0][col] != "." for col in range(7)):
            self.game_over = True

    def print_outcome(self):
        self.print_board()
        if not self.winner:
            print("Game over, it was a draw")
        else:
            print("Game over, {} won!".format(self.winner))


if __name__ == "__main__":
    game = Game()
    game.play()
