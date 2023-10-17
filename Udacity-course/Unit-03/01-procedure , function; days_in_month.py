def days_in_month(n):
    i = [31 , 28 , 31 , 30 , 31 , 30, 
         31 , 31 , 30 , 31 , 30 , 31]
    return i[n - 1]

print(days_in_month(2))