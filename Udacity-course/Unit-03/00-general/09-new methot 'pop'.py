a = [1 , 2 , 3 , 4 , 5 , 6]
result_poping_a =a.pop()
print(a)
print(result_poping_a)

print('\n')

b = ['B' , 'N' , 'A']
c = b[:]#How to copy list.
result_poping_b = b.pop()
print(result_poping_b)
print(b,'\n')

print(c)
d = ['B' , 'N' , 'A']
result_poping_d1 = d.pop()
result_poping_d2 = d.pop()
print(d)
d.append(result_poping_d2)
d.append(result_poping_d1)
print(d)
