#The pseudocode:
'''days = 0
while date1 is before date2:
    date1 = day after date1
    days += 1
return days'''


#Previously created functions:
def nextDay (year , month , day):
    '''Warning: this version incorrectly assumes all months have 30 days!'''
    day += 1
    if day > 30:
        day = day - 30
        month += 1
    if month > 12:
        month = month - 12
        year += 1
    return year , month , day
#print(nextDay(1992 , 12 , 30))



def dateIsBefore (year1 , month1 , day1 , year2 , month2 , day2):
    if (year1 , month1 , day1) <= (year2 , month2 , day2):
        return True
    else:
        return False



def daysBetweenDates ( year1 , month1 , day1 , year2 , month2 , day2):
    total_days = 0
    if dateIsBefore(year1 , month1 , day1 , year2 , month2 , day2):
        while (year1 , month1 , day1) != (year2 , month2 , day2):
            year1 , month1 , day1 = (nextDay(year1 , month1 , day1))
            total_days += 1
        return total_days
    else:
        return 'Incorret date!\nThe firts date, it must be before the second date.'

print(daysBetweenDates(1992 , 12 , 30 ,1992 , 12 , 30))

#This code, is unfinished, and I won't finish it. I will continue with the next video tutorial. Bye.