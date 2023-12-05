from the_board import Board
from the_score import Score


def is_valid_move(row, col, board):
    # Check if the move is within the bounds and the cell is empty
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '


def play_tic_tac_toe():
    board = Board([[' ' for _ in range(3)] for _ in range(3)])
    score = Score(board.board)
    current_player = 'X'

    while True:
        board.print_board()
        
        # Get player move
        try:
            row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if not is_valid_move(row, col, board.board):
            print("Invalid move. Try again.")
            continue

        # Make the move
        board.board[row][col] = current_player

        # Check for a winner or a tie
        if score.check_winner():
            board.print_board()
            print(f"Player {current_player} wins!")
            break
        elif board.is_board_full():
            board.print_board()
            print("It's a tie!")
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_tic_tac_toe()
