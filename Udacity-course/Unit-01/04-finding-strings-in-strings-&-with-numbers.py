inmortality_definition = "Iis  Tthe ability to preserve its entity in the face of the adversity of time."
print(inmortality_definition.find('adversity'))
print(inmortality_definition[57 : ])

print('version code result advance:')

inmortality_definition = 'is the ability to preserve its entity in the face of the adversity of time.'
the_result_searching_strings_in_strings = inmortality_definition.find('adversity')
print(inmortality_definition[the_result_searching_strings_in_strings : ])

print(inmortality_definition.find('face'))
print(inmortality_definition.find('o'))
#I don't know why the following strings are missing in the main chain
#print(inmortality_definition.find('I'))
#print(inmortality_definition.find("I"))
#print(inmortality_definition.find("T"))

print('test'.find('e'))
print(inmortality_definition.find('wabalabadingdong') + 1) #Olthough the result be "-1" yo can change the result with por example a sum like "+1" or other operation.



#WITH NUMBERS NOW:
finding_strings = 'When you are finding strings in other strings, you are finding substrings'
print(finding_strings.find('string' , 0))
print(finding_strings.find('string' , 22))
print('here '* 3)
print(finding_strings.find('string' , 39))
print(finding_strings.find('string' , 40))
print(finding_strings.find('string' , -12))

print(finding_strings[22:].find('string'))



#The quiz of the video-tutotiral

s = 'udacity'
t ='city'
i = 3
print(s.find(t , i))
print(s[ i : ].find(t))