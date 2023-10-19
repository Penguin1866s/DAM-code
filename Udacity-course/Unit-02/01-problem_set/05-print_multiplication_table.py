#This quiz has two star for dificulty
def print_multiplication_table (n_input):
#        global n_input 
    n1 = n_input
    n2 = n1
    while n1 >= 1:
        print(n1 , ' x ' , n2 , '= ' , n1 * n2)
        if n2 > 1:
            n2 = n2 -1
        else:
            n1 = n1 -1
            n2 = n_input
    return True
#return 'The table of ' , str(n_input)
print(print_multiplication_table(2))

#It outputs the "None" at the end of de function, because I didn't put any "return" in the procedure/ function.

#Attempt to invert the multiplication list:
'''
def print_multiplication_table (n_input):
    n_input_sum = 1
    n_input_min = 0
    
    while n_input:
        if n_input_sum <= n_input:
            n_input_min = n_input_min + n_input_sum
            n_input_sum = n_input_sum + 1
        else:
            break
        
        n1 = n_input_min
        n2 = n1

        if n1 >= 1:
            print(n1 , ' x ' , n2 , '= ' , n1 * n2)
            if n2 > 1:
                n2 = n2 -1
            else:
                n1 = n1 -1
                n2 = n_input
        else:
            break

print(print_multiplication_table(3))'''

#The reasoning on how I came to the conclusion on which algorithm to use:
'''
image reference = #In the image referente, it put the next:
1*1 = 1
1*2 = 2
2*1 = 2
2*2 = 2

result = 2
n1 * n2(while n2 < 1) = result
n1 * (n2 - 1(while n2 < 1)) = result
(n1 - 1) * (n2  (while n2 < 1))
(n1 - 1) * n2
(n1 - 1) * (n2 -1)

if n2 >= 1:
    n2 = n2 -1
else:
    n1 = n1 -1
    n2 = n_input
'''

#How to do it according to the video-tutorial(but it doesn't work):
'''def print_multiplication_table(n):
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            print str(i) + "*" + str(j) + "=" + str(i*j)
            j = j + 1
        i = i + 1

print(print_multiplication_table(2))'''
