# This is a Guess the Number program in python. 

# Random Module
import random

# Global Variables
number = 0
guess = 0

# picking a random number
def generateRandomNumber():
    global number
    number = random.randint(0, 9)
    return number

# guessing a number and telling the user whether its correct
def guessNumber():
    guesscount = 0
    try: 
        guess = int(input("Enter a number from 0,9 here:"))
        if guess == number:
            print("You got it right!")
            print("Total Attempts: 1")
        elif guess > 9:
            print("Thats greater than 9.")
            exit()
        while guess != number: 
            print("Sorry, thats not right.")
            guess = int(input("Enter a number from 0,9 here:"))
            guesscount = guesscount + 1
            if guess == number:
                print("You got it right!")
                print ("Total # of attempts: ", guesscount)
            elif guess > 9:
                print("Thats greater than 9.")
                exit()
        
    except ValueError:
        print("Not a Valid Input")

# Code Execution begins
if __name__ == "__main__":
    generateRandomNumber()
    guessNumber()
