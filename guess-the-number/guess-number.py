#import random library
from random import randrange

def guessNumber():
    #generate a random from 1 to 10
    number = int(randrange(1,10))

    #get user input
    print("Program has user guess a number that is generated randomly from 1 to 10")
    guess = int(input("Please enter a guess: "))

    while guess != number:
        
        #tell user if guess is too high or low
        if guess < number:
            print("Guess is too low")
        elif guess > number:
            print("Guess is too high")

        #get user input on wrong guess
        guess = int(input("Enter another guess: "))


    print("You guessed the right number")


if __name__ == '__main__':
    guessNumber()