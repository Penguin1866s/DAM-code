#Enunciated:
# encoding: utf-8

# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.
def check_issquare(sudoku):
    if all(len(row) == len(sudoku) for row in sudoku):
        return True
    else:
        return False

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

def check_col(sudoku):
    for col in sudoku:
        if sorted(col) == list(set(col)):
            continue
        else:
            return False
    return True

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

def check_sudoku(sudoku):
    if check_issquare(sudoku) and check_num_tipeValue(sudoku) and check_num_range(sudoku) and check_col(sudoku) and check_row(sudoku):
        return True
    else:
        return False


#Test with assertions:
assert check_sudoku([[1, 2, 3], [2, 3, 1], [3, 1, 2]]) == True , "It don't pass the test -01_(correcto)"
assert check_sudoku([[1, 2, 3, 4], [2, 3, 1, 3], [3, 1, 2, 3], [4, 4, 4, 4]]) == False , "It don't pass the test -02_(incorrecto1)"
assert check_sudoku([[1, 2, 3, 4], [2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 1, 2]]) == False , "It don't pass the test -03_(incorrecto2)"
assert check_sudoku([[1, 2, 3, 4, 5], [2, 3, 1, 5, 6], [4, 5, 2, 1, 3], [3, 4, 5, 2, 1], [5, 6, 4, 3, 2]]) == False , "It don't pass the test -04_(incorrecto3)"
assert check_sudoku([['a', 'b', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b']]) == False , "It don't pass the test -05_(incorrecto4)"
assert check_sudoku([[1, 1.5], [1.5, 1]]) == False , "It don't pass the test -06_(incorrecto5)"
assert check_sudoku([[1, 0, 0, 0], [0, 1, 0], [0, 0, 0, 1]]) == False , "It don't pass the test -07_(incorrecto6)"

#Extra-test with assertions:
assert check_sudoku([[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]]) == True , "It don't pass the test -08_(extraCorrecto1)"
assert check_sudoku([[1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9, 1, 2, 3], [7, 8, 9, 1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7, 8, 9, 1], [5, 6, 7, 8, 9, 1, 2, 3, 4], [8, 9, 1, 2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8, 9, 1, 2], [6, 7, 8, 9, 1, 2, 3, 4, 5], [9, 1, 2, 3, 4, 5, 6, 7, 8]]) == True , "It don't pass the test -09_(extraCorrecto2)"
assert check_sudoku([[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 3, 3]]) == False , "It don't pass the test -10_(extraIncorrecto1)"
assert check_sudoku([[1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9, 1, 2, 3], [7, 8, 9, 1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7, 8, 9, 1], [5, 6, 7, 8, 9, 1, 2, 3, 4], [8, 9, 1, 2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8, 9, 1, 2], [6, 7, 8, 9, 1, 2, 3, 4, 5], [9, 1, 2, 3, 4, 5, 6, 7, 1]]) == False , "It don't pass the test -11_(extraIncorrecto2)"


#Test:
'''
correcto = [[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]

incorrecto1 = [[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 2, 3],
               [4, 4, 4, 4]]

incorrecto2 = [[1, 2, 3, 4],
               [2, 3, 1, 4],
               [4, 1, 2, 3],
               [3, 4, 1, 2]]

incorrecto3 = [[1, 2, 3, 4, 5],
               [2, 3, 1, 5, 6],
               [4, 5, 2, 1, 3],
               [3, 4, 5, 2, 1],
               [5, 6, 4, 3, 2]]

incorrecto4 = [['a', 'b', 'c'],
               ['b', 'c', 'a'],
               ['c', 'a', 'b']]

incorrecto5 = [[1, 1.5],
               [1.5, 1]]

incorrecto6 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]

# Casos test

print(check_sudoku(correcto))
# >>> True

print(check_sudoku(incorrecto1))
# >>> False

print(check_sudoku(incorrecto2))
# >>> False

print(check_sudoku(incorrecto3))
# >>> False

print(check_sudoku(incorrecto4))
# >>> False

print(check_sudoku(incorrecto5))
# >>> False

print(check_sudoku(incorrecto6))
# >>> False
'''

# Extra-test:
'''
extraCorrecto1 = [[1, 2, 3, 4],
           [2, 3, 4, 1],
           [3, 4, 1, 2],
           [4, 1, 2, 3]]

extraCorrecto2 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
           [4, 5, 6, 7, 8, 9, 1, 2, 3],
           [7, 8, 9, 1, 2, 3, 4, 5, 6],
           [2, 3, 4, 5, 6, 7, 8, 9, 1],
           [5, 6, 7, 8, 9, 1, 2, 3, 4],
           [8, 9, 1, 2, 3, 4, 5, 6, 7],
           [3, 4, 5, 6, 7, 8, 9, 1, 2],
           [6, 7, 8, 9, 1, 2, 3, 4, 5],
           [9, 1, 2, 3, 4, 5, 6, 7, 8]]

extraIncorrecto1 = [[1, 2, 3, 4],
           [2, 3, 4, 1],
           [3, 4, 1, 2],
           [4, 1, 3, 3]]

extraIncorrecto2 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
           [4, 5, 6, 7, 8, 9, 1, 2, 3],
           [7, 8, 9, 1, 2, 3, 4, 5, 6],
           [2, 3, 4, 5, 6, 7, 8, 9, 1],
           [5, 6, 7, 8, 9, 1, 2, 3, 4],
           [8, 9, 1, 2, 3, 4, 5, 6, 7],
           [3, 4, 5, 6, 7, 8, 9, 1, 2],
           [6, 7, 8, 9, 1, 2, 3, 4, 5],
           [9, 1, 2, 3, 4, 5, 6, 7, 1]]

#Cases extra test:

print(check_sudoku(extraCorrecto1))
# >>> True

print(check_sudoku(extraCorrecto2))
# >>> True

print(check_sudoku(extraIncorrecto1))
# >>> False

print(check_sudoku(extraIncorrecto2))
# >>> False
'''
