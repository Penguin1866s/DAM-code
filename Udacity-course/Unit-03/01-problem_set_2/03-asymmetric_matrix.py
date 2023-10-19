# Define una rutina que devuelve True si una matriz es
# atisimetrica y False en otro caso. 
# Una matriz n*n es antisimetrica si se verifica que 
# sus elementos mantienen la relación:
# matriz[i][j] = - matriz[j][i] 
# para cada i=0,1,...,n-1 y para cada j=0,1,...,n-1.

def esAntisimetrica(matriz):
    i = -1
    j = 0
    while i + 1 < len(matriz):
        j = 0
        i += 1
        while j < len(matriz):
            if matriz[i][j] == - matriz[j][i]:
                j += 1
                continue
            else:
                return False
    return True

assert esAntisimetrica([[0, 1, 2], [-1, 0, 3], [-2, -3, 0]]) == True , "It don't pass the test -01"
assert esAntisimetrica([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == True , "It don't pass the test -02"
assert esAntisimetrica([[0, 1, 2], [-1, 0, -2], [2, 2, 3]]) == False , "It don't pass the test -03"
assert esAntisimetrica([[1, 2, 5], [0, 1, -9], [0, 0, 1]]) == False , "It don't pass the test -04"
assert esAntisimetrica([[1, 2, 5], [0, 1, -9], [0, 0, 1]]) == False , "It don't pass the test -05"
assert esAntisimetrica([[1,0,0,0], [0,1,1,0], [0,0,0,1]]) == False , "It don't pass the test -06_(matriz4)"
assert esAntisimetrica([[1,0,0,0,0,0,0,0,0]]) == False, "It don't pass the test -07_(matriz5)"


#Test:
'''
# Casos Test:

print esAntisimetrica([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print esAntisimetrica([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print esAntisimetrica([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print esAntisimetrica([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False

# casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert)

matriz4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print esAntisimetrica(matriz4)
#>>>False

matriz5 = [[1,0,0,0,0,0,0,0,0]]

print esAntisimetrica(matriz5)
#>>>False'''
