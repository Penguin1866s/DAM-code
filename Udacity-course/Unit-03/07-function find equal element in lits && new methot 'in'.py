def find_element(list , tarjet):
    counter = -1
    for element in list:
        counter += 1
        if element == tarjet:
            return list[counter]
        else:
            if element == list[len(list) -1]:
                return -1
            else:
                continue

print(find_element([1 , 2 , 3] , 3))
print(find_element(['alpha' , 'beta'] , 'gamma'))

#Now, find_elemnt using index
print('\nNow with index:')
def fin_element(list , tarjet):
    if tarjet in list:
        list.index(tarjet)
    else:
        return -1
print(find_element([1 , 2 , 3] , 3))
print(find_element(['alpha' , 'beta'] , 'gamma'))