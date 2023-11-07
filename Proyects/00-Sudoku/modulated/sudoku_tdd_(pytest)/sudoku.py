from src.s00_check_issquare import check_issquare
from src.s01_check_num import check_num_tipeValue
from src.s01_check_num import check_num_range
from src.s02_check_col import check_col
from src.s03_check_row import check_row
from test_cases import sudoku_test as stest

def check_sudoku(sudoku):
    if check_issquare(sudoku) and check_num_tipeValue(sudoku) and check_num_range(sudoku) and check_col(sudoku) and check_row(sudoku):
        return True
    else:
        return False

if __name__ == '__main__':
    #Test with assertions:
    assert check_sudoku(stest.correcto) == True , "It don't pass the test -01_(correcto)"
    assert check_sudoku(stest.incorrecto1) == False , "It don't pass the test -02_(incorrecto1)"
    assert check_sudoku(stest.incorrecto2) == False , "It don't pass the test -03_(incorrecto2)"
    assert check_sudoku(stest.incorrecto3) == False , "It don't pass the test -04_(incorrecto3)"
    assert check_sudoku(stest.incorrecto4) == False , "It don't pass the test -05_(incorrecto4)"
    assert check_sudoku(stest.incorrecto5) == False , "It don't pass the test -06_(incorrecto5)"
    assert check_sudoku(stest.incorrecto6) == False , "It don't pass the test -07_(incorrecto6)"

    #Extra-test with assertions:
    assert check_sudoku(stest.extraCorrecto1) == True , "It don't pass the test -08_(extraCorrecto1)"
    assert check_sudoku(stest.extraCorrecto2) == True , "It don't pass the test -09_(extraCorrecto2)"
    assert check_sudoku(stest.extraIncorrecto1) == False , "It don't pass the test -10_(extraIncorrecto1)"
    assert check_sudoku(stest.extraIncorrecto2) == False , "It don't pass the test -11_(extraIncorrecto2)"
else:
    print("The tests with assertions were not executed")
