#This quiz has one star for dificulty
def median (a , b , c):
    if a > b:
        if a < c:
            return a
        else:
            if b > c:
                return b
            else:
                return c
    else:
        if b < c:
            return b
        else:
            if a > c:
                return a
            else:
                return c
print(median(30 , 20 , 10))
print(median(20 , 10 , 30))
print(median(10 , 30 , 20))
