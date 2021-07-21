import random

start = 0
finish = 100
ask = str()
tries = 0

print('Please think of a number between 0 and 100!')
confirm = input("Enter 'yes' when you decide your number: ")

while confirm != 'yes':
    print("Please Enter 'yes' when you are ready")
    confirm = input("Enter 'yes' when you decide your number: ")
    
while ask != 'c':
    guess = int(random.randrange(start,finish))
    print('')
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    print('')
    ask = input('Is your secret number ' + str(guess) + '? ')
    tries += 1
    
    while ask != 'c':
        if ask == 'l':
            start = guess
            break
        elif ask == 'h':
            finish = guess
            break
        else:
            print('Sorry, I did not understand your input.')
            ask = input('Is your secret number ' + str(guess) + '? ')
        
if ask == 'c':
    print('')
    print('')
    print('Game over, your secret number is: ' + str(guess))
    print('I guessed it in ' + str(tries) + ' tries')
    