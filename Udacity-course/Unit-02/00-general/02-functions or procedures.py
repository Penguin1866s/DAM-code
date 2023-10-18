def rest_of_string (s):
    return s[1 : ]
print(rest_of_string('audacity') + '!')

print('\n\n#Another advance video')
def sum(a , b):
    print('\nHi everyone!')
    print('a is', a)
    a = a + b
    return a
print(sum(2, 123))

def sum(a , b):
    print('\nHi everyone!')
    print('a is', a)
    a = a + b
print(sum(2 , 123))

print('\n\n')

def sum(a , b):
    a = a +b

a = 2
b = 123
print(sum(a , b))

print('\n\n\nQuiz 1:')
def square (n):
    return n * n

print(square(5))


print('\n\nQuiz 2:')
def sum3 (n1 , n2 , n3):
    return n1 + n2 + n3

print(sum3(1 , 2 , 3))


print('\n\nQuiz 3:')
def abbaize (s1 , s2):
    return s1 + s2 * 2 + s1

print(abbaize('a' , 'b'))

print('\n\nQuiz 4_(Two Stars difficulty):')
def find_second (s_target ,s_search):
    return s_search.find(s_target , s_search.find(s_target) +1)

print(find_second('trees' , 'A forest is made up of many trees, witch coexist with other forms of live as well as other trees,in the same area'))