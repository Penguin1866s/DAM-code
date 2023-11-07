import pytest
from sudoku import check_sudoku
from test_cases import sudoku_test as stest
@pytest.mark.incorrects
def test_incorrects_sudoku():
    assert check_sudoku(stest.incorrecto1) == False , "It don't pass the test -01_(incorrecto1)"
    assert check_sudoku(stest.incorrecto2) == False , "It don't pass the test -02_(incorrecto2)"
    assert check_sudoku(stest.incorrecto3) == False , "It don't pass the test -03_(incorrecto3)"
    assert check_sudoku(stest.incorrecto4) == False , "It don't pass the test -04_(incorrecto4)"
    assert check_sudoku(stest.incorrecto5) == False , "It don't pass the test -05_(incorrecto5)"
    assert check_sudoku(stest.incorrecto6) == False , "It don't pass the test -06_(incorrecto6)"
    #The extratest:
    assert check_sudoku(stest.extraIncorrecto1) == False , "It don't pass the test -01_(extraIncorrecto1)"
    assert check_sudoku(stest.extraIncorrecto2) == False , "It don't pass the test -02_(extraIncorrecto2)"

@pytest.mark.corrects
def test_corrects_sudoku():
    assert check_sudoku(stest.correcto) == True , "It don't pass the test -01_(correcto)"
    #The extratest:
    assert check_sudoku(stest.extraCorrecto1) == True , "It don't pass the test -01_(extraCorrecto1)"
    assert check_sudoku(stest.extraCorrecto2) == True , "It don't pass the test -02_(extraCorrecto2)"
