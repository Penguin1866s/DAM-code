def check_row(sudoku):
    pos = 0
    while pos < len(sudoku[0]):
        j = []
        for i in sudoku:
            j.append(i[pos])
        if sorted(j) == list(set(j)):
            pos += 1
            continue
        else:
            return False
    return True
