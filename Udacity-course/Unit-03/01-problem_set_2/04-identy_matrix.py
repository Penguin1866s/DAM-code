# Dada una lista de lista representando una matriz n*n:
# Define una rutina que devuelve True si la entrada es una matriz indentidad
# y False en otro caso.

# Una matriz identidad es una matriz cuadrada en la que todos los elementos
# en la diagonal principal son 1 y el resto de elementos fuera de la
# diagonal principal son 0. 
# (Una matriz cuadrada es una matriz con el numero de filas
# igual al numero de columnas)
def issquare(matrix):
    if all(len(row) == len(matrix) for row in matrix):
        return True
    else:
        return False

def esMatrizIdentidad(matrix):
    #assert issquare(matrix) == True , "The matrix isn't square"
    if len(matrix) < 2:
        return False
    elif not issquare(matrix):
        optional_retunr = "the matrix isn't square but the result is in the previous line"
    else:
        optional_retunr = ''

    k = -1
    for i in matrix:
        k += 1
        if i[k] == 1 and all(x == 0 for x in i[k + 1: ]):
            continue
        else:
            return False
    print(optional_retunr)
    return True

#Test with assertions:
assert esMatrizIdentidad([[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]) == True , "It don't pass the test -01_(matrix1)"
assert esMatrizIdentidad([[1,0,0], [0,1,0], [0,0,0]]) == False , "It don't pass the test -02_(matrix2)"
assert esMatrizIdentidad([[2,0,0], [0,2,0], [0,0,2]]) == False , "It don't pass the test -03_(matrix3)"
assert esMatrizIdentidad([[1,0,0,0], [0,1,0,2], [0,0,1,0], [0,0,0,1]]) == False , "It don't pass the test -04_(matrix6)"
assert esMatrizIdentidad([[1, -1, 1], [0, 1, 0], [0, 0, 1]]) == False , "It don't pass the test -05_(matrix7)"
assert esMatrizIdentidad([[1,0,0,0], [0,1,1,0], [0,0,0,1]]) == False , "It don't pass the test -06_(matrix4)"
assert esMatrizIdentidad([[1,0,0,0,0,0,0,0,0]]) == False, "It don't pass the test -07_(matrix5)"


#Test:
'''
# Casos test:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print esMatrizIdentidad(matrix1)
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print esMatrizIdentidad(matrix2)
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print esMatrizIdentidad(matrix3)
#>>>False

matrix6 = [[1,0,0,0],  
           [0,1,0,2],  
           [0,0,1,0],  
           [0,0,0,1]]

print esMatrizIdentidad(matrix6)
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print esMatrizIdentidad(matrix7)
#>>>False           


# casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert):

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print esMatrizIdentidad(matrix4)
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print esMatrizIdentidad(matrix5)
#>>>False          
'''
