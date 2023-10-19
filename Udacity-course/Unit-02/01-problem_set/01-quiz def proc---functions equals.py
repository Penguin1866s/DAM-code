def test(x):
    if x == 2:
        return True
    return False

def proc(a , b):
    if test(a):
        return b
    return a

print(proc(2 , 3))
