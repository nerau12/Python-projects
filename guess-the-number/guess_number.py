#import random library
from random import randrange

class Guess_Number:

    def __init__(self):
        #generate a random from 1 to 10
        self.number = int(randrange(1,100))
        self.guess = 0
        self.num_of_guesses = 0
        self.max_num_of_guess = 5
    
    #plays game
    def guess_number(self):
        print("Program has user guess a number that is generated randomly from 1 to 100\n You have 5 guesses")
        self.get_number()

        while (self.guess != self.number) and (self.num_of_guesses != self.max_num_of_guess):
        
            #tell user if guess is too high or low
            if self.guess < self.number:
                print("Guess is too low")
            elif self.guess > self.number:
                print("Guess is too high")
            
            #tell user how many guesses left
            print('You have ' + str(self.max_num_of_guess - self.num_of_guesses) + ' left')

            #get user input on wrong guess
            self.get_number()
        
        self.results()

    #gets guesses from user
    def get_number(self):
        try:
            self.guess = int(input("Please enter a guess: "))
            self.num_of_guesses += 1
        except ValueError:
            print('Not a number')
            return self.get_number()
    
    #prints results
    def results(self):
        if self.guess == self.number:
            print("You guessed the right number")
        else:
            print('You ran out of guesses. The number was: ' + str(self.number))


if __name__ == '__main__':
    guess_number = Guess_Number()
    guess_number.guess_number()
