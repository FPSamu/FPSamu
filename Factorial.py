def fact(n):
    factorial = 1
    for x in range(n):
        x += 1
        factorial = factorial*x
    print(factorial)
        
fact(9)        