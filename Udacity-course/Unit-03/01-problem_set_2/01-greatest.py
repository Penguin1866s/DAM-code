# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list):
    if len(list) != 0 and all(isinstance(x , int) for x in list):
        return max(list)
    elif len(list) == 0:
        return 0

print(greatest([2 , 4 , 3 , 8 , 18 , 2 , 0]))
print(greatest([4 , 23 , 1]))
print(greatest([]))

#Test:
#print greatest([4,23,1])
#>>> 23
#print greatest([])
#>>> 0