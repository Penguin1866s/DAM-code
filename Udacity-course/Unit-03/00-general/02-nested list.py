beatles = [['John' , 1940] , ['Paul' , 1942] , 
           ['George' , 1943] , ['Ringo' , 1940]]
print(beatles)
print(beatles[1][0])

print('\nQuiz:')
#Quiz a:
countries = [['China' , 'Beijing' , 1350] ,
             ['India' , 'Delhi' , 1210] ,
             ['Romania' , 'Bucharest' , 21] ,
             ['United States' , 'Washington' , 309]]
print(countries[1][1])

print('\nQuiz b:')
#Quiz b:
multiple_romanians_pop_china = countries[0][2] / countries[2][2]
print(multiple_romanians_pop_china)
print( 21 * multiple_romanians_pop_china)
