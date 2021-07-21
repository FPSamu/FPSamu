def calendar(day,month,year):
    # Calcular los dias que han pasado desde el inicio del año
    total_month_days = 0
    month_days = 0
    for x in range(month):
        if x in(1, 3, 5, 7, 8, 10, 12):
            month_days = 31
        elif x == 2:
            month_days = 28
        elif x in(4, 6, 9, 11):
            month_days = 30
            
        total_month_days += month_days
            
            
            
    # Calcular dias desde el 1/1/1 hasta el año que le di
    if year%4 == 0 and month in(1,2):
        days_appart = (year*365) + total_month_days + day + 5
    else:
        days_appart = (year*365) + int(year/4) + total_month_days + day + 5
    # Pasar dias de la semana
    week_days = 0
    for x in range(days_appart):
        week_days += 1
        if week_days > 6:
            week_days = 0
      
    
    # Nombrar que dia de la semana es     
    if week_days == 1:
        name_week_days = 'lunes'
    if week_days == 2:
        name_week_days = 'martes'    
    if week_days == 3:
        name_week_days = 'miercoles'
    if week_days == 4:
        name_week_days = 'jueves'
    if week_days == 5:
        name_week_days = 'viernes'
    if week_days == 6:
        name_week_days = 'sabado'
    if week_days == 0:
        name_week_days = 'domingo'
        
        
    return(name_week_days)    
    
print(calendar(19,7,2021))