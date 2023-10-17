yes = str(34)
print(yes + ' is a number in the value of a string')

input_number = 6.49
rounding_number = input_number + 0.555555555
print(input_number)

number_decimals = str(rounding_number) #the function of "str()" is to transform the value of a number into a value of string.


separator_decimals = number_decimals.find('.')
print(number_decimals[ : separator_decimals])