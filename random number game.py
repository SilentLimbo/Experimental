##1) computer generates random number between
##   1 - 100.
##2) and the user enters in a guess
##   as to what the number is.
##3) Compare the numbers.

import random

print("Guess my number game!")
randomNum = random.randint(1,100)
guess = int(input("Enter a guess: "))
counter = 1
while guess != randomNum:
    if guess > randomNum:
        print("Lower")
        guess = int(input("Enter the next guess: "))
        counter += 1
    else:
        print("Higher")
        guess = int(input("Enter the next guess: "))
        counter += 1

    
print("You guessed it in% d! the number is% d" % (counter, randomNum))
