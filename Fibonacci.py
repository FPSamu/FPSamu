def fib(int):
    prev = 0
    curr = 0
    print(curr)
    curr += 1
    for x in range(int):
        print(curr)
        curr += prev
        prev = curr - prev
        
fib(3)        