w = 23
if 49 > w:
    print('The value of the first "if" is true!\n')

w = 78
if 49 > w:
    print('The value of the first "if" is true!')

"""if a logical value, is negative, the function returns the logical value, into positive logical value."""
def absolute(x):
    if x < 0:
        x = -x
    return x
print(absolute(-2))

print('\n Quiz-01:')
def bigger(n1, n2):
    if n1 < n2:
        return n2
    return n1

print('The Bigger number is:' , bigger(25 , 3782))

print("\nNow with 'else':")
def bigger(n1 , n2):
    if n1 < n2:
        return n2
    else:
        return n1

print('The Bigger number is:' , bigger(25 , 3782))

print('\nOr like this, that is more clean(in the code, more or less):')
def bigger(n1 , n2):
    if n1 < n2:
        r = n2
    else:
        r = n1
    return r
print('The Bigger number is:' , bigger(25 , 3782))



print('\nQuiz-02:')
def is_friend(s):
    if s[0] == 'D':
        return True
    else:
        if s[0] == 'N':
            return True
        else:
            return False

    
print(is_friend('Dimitri'))
print(is_friend('Narancia'))
print(is_friend('Hans Zimer'))

print("\nNow with the operator 'or':")
def is_friend(s):
    if s[0] == 'D' or s[0] == 'N':
        return True
    else:
        return False

print(is_friend('Dimitri'))
print(is_friend('Narancia'))
print(is_friend('Hans Zimer'))

print('\nFunction with the operator "or":')
print( False or 'what')
print( 'what' or False)
print( True or 'what')
print( '' or True) #Beacaue '' is False
print( 'what' or False) #Beacaue a string no empty is True  

print('\n\n\nQuiz-03_(with one star of difficulty):')
print('\nMethot 1(the most complex):')
def biggest (a , b , c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

print(biggest(3 , 6 , 9))
print(biggest(3 , 9 , 6))
print(biggest(9 , 6 , 3))

print('\nMethot 2:')
def bigger (n1 , n2):
    if n1 > n2:
        return n1
    else:
        return n2

def biggest (a , b , c):
    if bigger(a , b) > c:
        return bigger(a , b)
    else:
        return c

print(biggest(3 , 6 , 9))
print(biggest(3 , 9 , 6))
print(biggest(9 , 6 , 3))

print('\nMethot 3_(the easiest but with an extra function):')
def biggest (a , b , c):
    return max(a , b , c)

print(biggest(3 , 6 , 9))
print(biggest(3 , 9 , 6))
print(biggest(9 , 6 , 3))



print('\n\n\nPreguntar Gelpi si el siguiente código hay algo que esté mal')
"""def biggest (a , b , c):
    if a > b:
        if a > c:
            return a
    if b > a:
        if b > c:
            return b
    if c > a:
        if c > b:
            return c
print(biggest(3 , 6 , 9))
print(biggest(3 , 9 , 6))
print(biggest(9 , 6 , 3))"""
