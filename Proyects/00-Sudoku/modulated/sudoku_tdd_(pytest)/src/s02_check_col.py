def check_col(sudoku):
    for col in sudoku:
        if sorted(col) == list(set(col)):
            continue
        else:
            return False
    return True
