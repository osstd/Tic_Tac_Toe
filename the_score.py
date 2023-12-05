class Score:
    def __init__(self, board):
        self.board = board

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ' or \
                    self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ' or \
                self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True

        return False
