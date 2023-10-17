#01-Make a 4-character string, and assign it to a name.
print('#01')
S = 'Spam'
print(S)

#02-Length.
print('#02')
print(len(S))

#03-The first item in S, indexing by zero-based position.
print('#03')
print(S[0])

#04-The second item from the left.
print('#04')
print(S[1])

#05-The last item from the end in S
print('#05')
print(S[-1])

#06-The second-to-last item from the end
print('#06')
print(S[-2])

#07-The last item in S
print('#07')
print(S[-1])

#08-Negative indexing, the hard way
print('#08')
print(S[len(S)-1])

#09-A 4-character string
print('#09')
print(S)

#10-Slice of S from offsets 1 through 2 (not 3)
print('#10')
print(S[1 : 3])

#11-Everything past the first (1:len(S))
print('#11')
print(S[1 : ])

#12-S itself hasn't changed
print('#12')
print(S)

#13-Everything but the last
print('#13')
print(S[0 : 3])

#14-Same as S[0:3]
print('#14')
print(S[ : 3])

#15-Everything but the last again, but simpler (0:-1)
print('#15')
print(S[ : -1])

#16-All of S as a top-level copy (0:len(S))
print('#16')
print(S[ : ])

#17-Concatenation
print('#17')
print(S + 'something')

#18-S is unchanged
print('#18')
print(S)

#19-Repetition
print('#19')
print(S * 5)

#20-Immutable objects cannot be changed
#S[0] = 'w'
print('#20')
print(S)

#21-But we can run expressions to make new objects
S = 'z' + S[1 : ]
print('#21')
print(S)

#22-Expand to a list: [...]
print('#22')
S = 'strubbery'
L = list(S)
print(L)

#23-Change it in place
print('#23')
L[1] = 'c'
print(L)

#24-Join with empty delimiter
print('#24')
print(''.join(L))

#25-A bytes/list hybrid (ahead)
print('#25')
B = bytearray(b'spam') #I don't understand this function-01.#Don't understand-00
print(B)
print(list(B))

#26-'b' needed in 3.X, not 2.X
print('#26')
B.extend(b'eggs')
print(B)

#27-B[i] = ord(c) works here too
print('#27')
print(B)

#28-Translate to normal string
print('#28')
print(B.decode()) #I don't understand this function-02.##Don't understand-01

#29-Find the offset of a substring in S
print('#29')
S = 'Spam'
print(S.find('pa'))

#30-Replace occurrences of a string in S with another
print('#30')
print(S.replace('pa', 'REPLACED'))

#31-Split on a delimiter into a list of substrings
print('#31')
line = 'aaahbbbhccccchdd'
print(line.split('h'))

#32-Upper- and lowercase conversions
print('#32')
S = 'sPam'
print(S.upper())
print(S.lower())

#33-Content tests: isalpha, isdigit, etc.
print('#33')
S = 'Spam'
print(S.isalpha() , S.isdigit())
S = '354'
print(S.isalpha() , S.isdigit())
S = 'Spam2'
print(S.isalpha() , S.isdigit())

#34-Remove whitespace characters on the right side
print('#34')
line = " aaa,bbb,ccccc,dd\n"
print(line)
print(line.rstrip())
print(line.lstrip())

#35-Combine two operations
print('#35')
print(line.rstrip().split(','))

#36-Formatting expression (all)
print('#36')
print('%s, eggs, and %s' % ('spam', 'SPAM!'))

your_name_or_strings = 'Jon Arbukle'
your_age_or_decimal_integers = 42.6
your_failure_rate_or_floating_points_number = 30.2

print('\n\nThe formating in Python is like this:\nName: %s \nAge: %d \nFailture Rate: %.2f \n\n' % (your_name_or_strings, your_age_or_decimal_integers, your_failure_rate_or_floating_points_number))

#37-Formatting method (2.6+, 3.0+)
print('#37')
print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))
print('{1}, eggs, and {0}'.format('spam', 'SPAM!'))
print('{0}, eggs, and {0}'.format('spam'))#the original it works, but it has arguments that will not be used_(original: "print('{0}, eggs, and {0}'.format('spam', 'SPAM!'))").
print('{0}, eggs, and {0}'.format('SPAM!'))#the original it works, but it has arguments that will not be used_(original: "print('{1}, eggs, and {1}'.format('spam', 'SPAM!'))").

#38-Numbers optional (2.7+, 3.1+)
print('#38')
print('{}, eggs, and {}'.format('spam', 'SPAM!'))

#39-Separators, decimal digits
print('#39')

#40-Digits, padding, signs
print('#40')

#41-Extra-Class___(For now, this function will not be explained because it is too advanced at the moment.)
print('\n\n#41')
print('Too advanced for now(Python Classes).')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Person = Person('John', 36)
print(Person.name)
print(Person.age)



#The new functions learned in this exercises are:
##
##1-len('The value in number, of the longitude of a string').
##2-list('Displays the string value character by character').
##3-''.join('Transforms a list into a string, joining them with the string you specify.').
######4- bytearray('Transforms a string into a list of bytes').
######5-.decode('Transforms a list of bytes into a string').
##6-variable.extend(variable for join'join the values of variables with another variable').
##7-.replace("string to be replaced" , "string substitute"'Replace only the sub-strings for other sub-strings that you specify').
##8-.split("the caracter to decide where will be going to be de separations" 'Split a string into a list of sub-strings, using the string you specify as a separator').
##9-.upper('Transforms a string into uppercase').
##10-.lower('Transforms a string into lowercase').
##11-.isalpha('Returns True if the string contains only letters').
##12-.isdigit('Returns True if the string contains only numbers').
##13-.rstrip('Removes the spaces to the right of the string').
##14-.lstrip('Removes the spaces to the left of the string').
##15-Escape sequences: \n(newline), \t(tab), \\(backslash), \'(single quote), \"(double quote), \xNN(hexadecimal value).
##16-Formatting expression (all): %s(string), %d(decimal integer), %f(floating-point number)._(Example: "'%s, eggs, and %s' % ('spam', 'SPAM!')").
##17-Formatting method (2.6+, 3.0+): {0}(first argument), {1}(second argument)._(Example: "'{0}, eggs, and {1}'.format('spam', 'SPAM!')").
##18-Numbers optional(The same as the last new function learned) (2.7+, 3.1+): {}(first argument), {}(second argument)._(Example: "'{}, eggs, and {}'.format('spam', 'SPAM!')").



#new_functions_learned = "len(The value in number, of the longitude of a string)" + "list(Displays the string value character by character)"
#print(new_functions_learned)