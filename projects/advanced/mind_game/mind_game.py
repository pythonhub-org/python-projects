# This program is a computer mind game.

# Importing random module to generate numbers
import random

# global variables 
final_computer_number = 0
final_user_number = 0

# generates random numbers for computer and user
def generateRandomNumber():
    global final_computer_number, final_user_number
    computer_number_1 = random.randint(0, 25)
    computer_number_2 = random.randint(0, 25)
    final_computer_number = computer_number_1 + computer_number_2
    user_number_1 = random.randint(0, 25)
    user_number_2 = random.randint(0, 25)
    final_user_number = user_number_1 + user_number_2
    print("Computer has generated its numbers.")
    print ("This is total of your two numbers:",final_user_number)

# Takes user inputs on whether to increase their number
def play_game():
    global final_computer_number, final_user_number
    random_user_number = 0
    user_adds_number = True
    while user_adds_number: 
        enter_number = input("Would you like to add another number (yes/no): ")
        enter_number = enter_number.lower()
        if enter_number == "no":
            print(final_user_number, "is your final number")
            if final_computer_number > final_user_number: 
                print("You lose.")
                print("Computer Number:", final_computer_number)
                print("Your Number: ", final_user_number)
                user_adds_number = False
            elif final_computer_number < final_user_number: 
                print("You win.")
                print("Computer Number:", final_computer_number)
                print("Your Number: ", final_user_number)
                user_adds_number = False
            else:
                print("You tied with the computer.")
                user_adds_number = False
        elif enter_number == "yes":
            random_user_number = random.randint(0, 25)
            final_user_number = final_user_number + random_user_number
            print("This is your new number: ", final_user_number)
            if final_user_number > 50:
                print("Your number exceeded 50. You lose")
                print("Computer Number: ", final_computer_number)
                user_adds_number = False
        else: 
            print("Make sure to enter Yes or No.")

# Code Execution Begins
if __name__ == "__main__":
    generateRandomNumber()
    play_game()
