def check_num_tipeValue(sudoku):
    for n in sudoku:
        if all(type(sub_n) == int for sub_n in n): #it can be "type(sub_n) == int" or "isinstance(sub_n, int)"
            continue
        else:
            return False
    return True

def check_num_range(sudoku):
    num_range = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for n in sudoku:
        if all(sub_n in num_range for sub_n in n):
            continue
        else:
            return False
    range_for_sudoku = []
    k = 0
    for n in sudoku[0]:
        k += 1
        range_for_sudoku.append(k)
    for n in sudoku:
        if all(sub_n in range_for_sudoku for sub_n in n):
            continue
        else:
            return False
    return True
