def dateIsBefore (year1 , month1 , day1 , year2 , month2 , day2):
    if (year1 , month1 , day1) < (year2 , month2 , day2):
        return True
    else:
        return False
    
print(dateIsBefore(1992 , 9 , 20 , 1993 , 9 , 1))
