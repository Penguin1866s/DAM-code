# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(list):
    counter = 0
    if len(list) == 0:
        mult_nums_list = 1
    else:
        for j in list:
            counter += 1
            if counter > 1:
                mult_nums_list = mult_nums_list * j
            else:
                mult_nums_list = j * 1
    return mult_nums_list

print(product_list([9]))
print(product_list([1 , 2 , 3 , 4]))
print(product_list([]))

#Test:
#print product_list([9])
#>>> 9

#print product_list([1,2,3,4])
#>>> 24

#print product_list([])
#>>> 1
