def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
        if board[i][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:

                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve_sudoku(board):
                            return True

                        board[row][col] = 0

                return False
    return True
