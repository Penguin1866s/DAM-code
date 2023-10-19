print('Example-01')
def print_numbers (n):
    x = 1
    while x <= n:
        print(x)
        x = x + 1
print(print_numbers(13))

#Equal:
print('\nEqual to:\n')

def print_numbers (n):
    i = 1
    while True:
        if i > n:
            break
        print(i)
        i = i + 1
print(print_numbers(13))

print('\n\n\nExample-02')

a = 3
while a > 0:
    print('2 is bigger than 1')
    a = a - 1

#Equal to:
print('\nEqual to:\n')

a = 3
while a > 0:
    print('2 is bigger than 1')
    a = a -1
    if a > 0:
        print('2 is bigger than 1')
        a = a -1
    else:
        break
        