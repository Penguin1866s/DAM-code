#Ejerices rat book Charapter 8:
print('Ejercice-01:')
print(len([1 , 2 , 3]))                #    Length
print([1 , 2 , 3] + [4 , 5 , 6])       # Concatenation
print(['Ni!'] * 4)                     # Repetition

print('\nEjercice-02:')
print(str([1 , 2]) + '34')             # Same as "[1, 2]" + "34"
print([1 , 2] + list('34'))            # Same as [1, 2] + ["3", "4"]

print('\nEjercice-03:')
print(3 in [1 , 2 , 3])                # Membership
for x in [1 , 2 , 3]:
    print(x , end=' ')                 # Iteration (2.X uses: print x,)

print('\n\nEjercice-04:')
res = [c * 4 for c in 'SPAM']          # List comprehensions
print(res)
res = []
for c in 'SPAM':                       # List comprehension equivalent
    res.append(c * 4)
print(res)

print('\nEjercice-05:')
L = ['spam', 'Spam', 'SPAM!']
print(L[2])                            # Offsets start at zero
print(L[-2])                           # Negative: count from the right
print(L[1:])

print('\nEjercice-06:')
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(matrix[1])
print(matrix[1][1])
print(matrix[2][0])
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
print(matrix[1][1])

print('\nEjercice-07:')
L = ['spam', 'Spam', 'SPAM!']
L[1] = 'eggs'                          # Index assignment
print(L)
L[0:2] = ['eat', 'more']               # Slice assignment: delete+insert
print(L)                               # Replaces items 0,1

print('\nEjercice-08:')
L = ['eat', 'more', 'SPAM!']
L.append('please')                     # Append method call: add item at end
print(L)
L.sort()                               # Sort list items ('S' < 'e')
print(L)
a = ['a' , 'c' , 'b' , 'D']
a.sort()
print(a)

print('\nEjercice-09:')
L = ['abc', 'ABD', 'aBe']
L.sort()
print(L)
L.sort(key=str.lower)                  # Normalize to lowercase
print(L)
L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower , reverse=True)   # Change sort order
print(L)

print('\nEjercice-10:')
L = [1, 2]
L.extend([3, 4, 5])                    # Add many items at end (like in-place +)
print(L)
print(L.pop())                         # Delete and return last item (by default: −1)
print(L)
L.reverse()                            # In-place reversal method
print(L)
print(list(reversed(L)))               # Reversal built-in with a result (iterator)

print('\nEjercice-11:')
L = []
L.append(1)                            # Push onto stack
L.append(2)
print(L)
L.pop()                                # Pop off stack
print(L)

print('\nEjercice-12:')
L = ['spam', 'eggs', 'ham']
print(L.index('eggs'))                 # Index of an object (search/find)
L.insert(1, 'toast')                   # Insert at position
print(L)
L.remove('eggs')                       # Delete by value
print(L)
L.pop(1)                               # Delete by position
print(L)
print(L.count('spam'))                 # Number of occurrences

print('\nEjercice-13:')
L = ['spam', 'eggs', 'ham', 'toast']
print(L)
del L[0]                               # Delete one item
print(L)
del L[1:]                              # Delete an entire section
print(L)                               # Same as L[1:] = []

print('\nEjercice-14:')
print('\nEjercice-15:')
print('\nEjercice-16:')
#print('\nEjercice-17:')
#print('\nEjercice-18:')
#print('\nEjercice-19:')
#print('\nEjercice-20:')
#print('\nEjercice-21:')
#print('\nEjercice-22:')
#print('\nEjercice-23:')