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

print(nextDay(1992 , 12 , 30))