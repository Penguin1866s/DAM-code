def check_issquare(sudoku):
    if all(len(row) == len(sudoku) for row in sudoku):
        return True
    else:
        return False
