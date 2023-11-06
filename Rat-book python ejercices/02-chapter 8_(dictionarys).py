#Ejerices rat book Charapter 8_(dictionarys):

print('Ejercice-01:')
D = {'spam': 2, 'ham': 1, 'eggs': 3}    # Make a dictionary
D['spam']                               # Fetch a value by key
print(D)                                # Order is "scrambled"


print('\n\nEjercice-02:')
print(len(D))                           # Number of entries in dictionary
print('ham' in D)                       # Key membership test alternative
print(list(D.keys()))                   # Create a new list of D's keys


print('\n\nEjercice-03:')
print(D)
D['ham'] = ['grill', 'bake', 'fry']     # Change entry (value=list)
print(D)
del D['eggs']                           # Delete entry
print(D)
D['brunch'] = 'Bacon'                   # Add new entry
print(D)


print('\n\nEjercice-04:')
D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(list(D.values()))
print(list(D.keys()))#Extra, it's not in the book.
print(list(D.items()))


print('\n\nEjercice-05:')
print(D.get('spam'))                    # A key that is there
print(D.get('toast'))                   # A key that is missing
print(D.get('toast', 88))
print(D)


print('\n\nEjercice-06:')
print(D)
D2 = {'toast':4, 'muffin':5}            # Lots of delicious scrambled order here
D.update(D2)
print(D)


print('\n\nEjercice-07:')
# pop a dictionary by key
print(D)
print(D.pop('muffin'))
print(D.pop('toast'))                   # Delete and return from a key
print(D)

# pop a list by position
L = ['aa', 'bb', 'cc', 'dd']
print(L.pop())                          # Delete and return from the end


print('\n\nEjercice-08:')
table = {'1975': 'Holy Grail',          # Key: Value
         '1979': 'Life of Brian',
         '1983': 'The Meaning of Life'}
year = '1983'
movie = table[year]                     # dictionary[Key] => Value
print(movie)
for year in table.keys():               # Same as: for year in table.keys()
    print(year + '\t' + table[year])


print('\n\nEjercice-09:')
table = {'Holy Grail': '1975',          # Key=>Value (title=>year)
         'Life of Brian': '1979',
         'The Meaning of Life': '1983'}
print(table['Holy Grail'])
print(list(table.items()))              # Value=>Key (year=>title)
print([title for (title, year) in table.items() if year == '1975'])


print('\n\nEjercice-10:')
K = 'Holy Grail'
print(table[K])                         # Key=>Value (normal usage)
V = '1975'
print([key for (key, value) in table.items() if value == V]) # Value=>Key
print([key for key in table.keys() if table[key] == V])      # Ditto


print('\n\nEjercice-11:')
#This exercise is not in the book.
Matrix = {}
Matrix[(2, 3, 4)] = 88
print(Matrix.get((2, 3, 344), 'Uohohoi')) #the 'Uohohoi' is the output if the key is not in the dictionary.


print('\n\nEjercice-12:')
{'name': 'Bob', 'age': 40}              # Traditional literal expression
D = {}                                  # Assign by keys dynamically
D['name'] = 'Bob'
D['age'] = 40
dict(name='Bob', age=40)                # dict keyword argument form
dict([('name', 'Bob'), ('age', 40)])    # dict key/value tuples form

print('\n\nEjercice-13:')
#This exercise is not underlined in the book.
D = dict.fromkeys(['a', 'b', 'c'], 0)
print(D)

D = dict.fromkeys('spam')               # Other iterables, default value
print(D)


print('\n\nEjercice-14:')
D = dict(a=1, b=2, c=3)
print(D)

K = D.keys()                            # Makes a view object in 3.X, not a list
print(K)
print(list(K))                          # Force a real list in 3.X if neede


print('\n\nEjercice-15:')
D = {'a': 1, 'b': 2, 'c': 3}
Ks = D.keys()                           # Or you can use sorted() on the keys

for k in sorted(Ks): print(k, D[k])     # sorted() accepts any iterable
                                        # sorted() returns its result
