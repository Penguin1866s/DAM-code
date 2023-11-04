#It can do like this:
population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}
print(population['Mumbai'])

#or like this:

population = {}
population['Shanghai'] = 17.8
population['Istanbul'] = 13.3
population['Karachi'] = 13.0
population['Mumbai'] = 12.5
print(population['Mumbai'])


#Other practices:
elements = {}
elements['H'] = {'name': 'Hydrogen', 'number': 1, 'weight': 1.00794}
elements['I'] = False
print(elements)
print('\n')
print(elements['H'])
print(elements['H']['name'])
