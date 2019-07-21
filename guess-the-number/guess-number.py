
def guessNumber():
    #import random library
    import random

    #generate a random from 20 to 50 in step 1
    number = int(random.randrange(1,4))
    #get user input
    print("Program has user guess a number that is generated randomly")
    guess = int(input("Enter another guess: "))

    while guess != number:

        if guess < number:
            print("Guess is too low")
        elif guess > number:
            print("Guess is too high")

        guess = int(input("Enter another guess: "))

    if guess == number:
        print("You guessed the right number")

guessNumber()