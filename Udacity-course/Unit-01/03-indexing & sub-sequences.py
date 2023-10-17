yes = 'homunculus'[5]
print(yes)

no = 'homunculus'
print(no[4 + 1])

it_can_be = 'homunculus'
print(it_can_be[-5] + it_can_be[-10] + it_can_be[2 + 6] + it_can_be[9 - 0] * 3)


#Sub-Sequences start from here
or_mabey_not = 'homunculus'
print(or_mabey_not[2 : 5])
print(or_mabey_not[5 : ])
print(or_mabey_not[-5 : ])
print(or_mabey_not[2 : ])
print(or_mabey_not[ : -7] + or_mabey_not[1])
print(or_mabey_not[5 : 8] + or_mabey_not[1] * 15 + or_mabey_not[-1] * 15 *3)
print(or_mabey_not[5] + or_mabey_not[-2] *3 *3 *2 + or_mabey_not[-3] + or_mabey_not[1] * 15 + or_mabey_not[-1] * 15 *3 + '!!!' *3)



#The quiz of de video-tutorial
something = 'udacity'
print(something[2] + something[0] + something[1 : ])