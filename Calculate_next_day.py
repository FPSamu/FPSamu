def next_Day(day,month,year):

    if year%4 == 0:
        leap = True
    else:
        leap = False
        
    if month in(1, 3, 5, 7, 8, 10, 12):
        month_days = 31
    elif month == 2:
        if leap == True:
            month_days = 29
        else:
            month_days = 28
    elif month in(4, 6, 9, 11):
        month_days = 30
        
    if day < month_days:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1     
            
    return(day,month,year)



print(next_Day(1,1,1))    
    
    