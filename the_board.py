class Board:
    def __init__(self, board):
        self.board = board

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def is_board_full(self):
        # Check if the board is full
        for row in self.board:
            if ' ' in row:
                return False
        return True
