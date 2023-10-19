def countdown (n):
    if n < 0:
        n = None
        return 'Invalid value!'
    else:
        while n or n == 0:
            if n > 0:
                print(n)
                n = n -1
            else:
                if n == 0:
                    print(n)
                break
    return 'Blastoff!'

#print(countdown(3))
print(countdown(10))




#The way from the video tutorial:
print('\n\n\nThe way from the video tutorial:')
def countdown (n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')

print(countdown(3))
