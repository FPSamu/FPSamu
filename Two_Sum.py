def two_sum(numbers,target):
    numbers = list(str(numbers))
   
    for x in numbers:
        remain = target - int(x)
        
        if str(remain) in numbers:
            position_1 = [numbers.index(x)]
            position_2 = [numbers.index(str(remain))]
            if position_1 != position_2:
                status = True
                break
        else:
            status = "I couldn't find a sum"
            
    
    if status == True:
        return position_1 + position_2
    else:
        return status

print(two_sum(1253,6))