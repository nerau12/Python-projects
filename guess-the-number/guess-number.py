#import random library
import random

#generate a random from 20 to 50 in step 1
number = int(random.randrange(1,2))

#get user input
print("Program has user guess a number that is generated randomly")
guess = int(input("Enter another guess: "))

while guess != number:
    print("Not the correct number")
    guess = int(input("Enter another guess: "))

if guess == number:
    print("you guessed the right number")