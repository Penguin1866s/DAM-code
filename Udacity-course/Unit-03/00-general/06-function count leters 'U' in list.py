def measure_udacity(list):
    sum_strings_list = ''
    for i in list:
        sum_strings_list += i 
    result = sum_strings_list.count('U')
    return result
print(measure_udacity(['Udacity' , 'yes' , 'nain you nain' , 'YOU are something... you are...']))
