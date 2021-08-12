# This is a Guess the Pokemon program in python. 

# Random Module
import random

# Global Variables
pokemon = ""
guess = 0

# picking a random pokemon
def generateRandomPokemon():
    global pokemon
    list_of_pokemon = ['Bulbosaur', 'Ivysaur', 'Venusaur', 'Squirtle', 'Wartortle', 'Blastoise', 'Charmander', 'Charmeleon', 'Charizard', 'Pikachu']
    pokemon = random.choice(list_of_pokemon)
    return pokemon

# guessing a pokemon and telling the user whether its correct

def guessPokemon():
    guesscount = 0
    print("Here is the list of pokemon: Bulbosaur, Ivysaur, Venusaur, Squirtle, Wartortle, Blastoise, Charmander, Charmeleon, Charizard, Pikachu.")
    find_pokemon = True
    while find_pokemon: 
        guess = str(input("Guess pokemon: "))
        guess = guess.lower().title()
        guesscount = guesscount + 1
        if guess == pokemon:
            print("You got it right!")
            print ("Total # of attempts: ", guesscount)   
            find_pokemon = False  
        elif guess != pokemon:
            print("Sorry, thats not right.")

# Code Execution begins
if __name__ == "__main__":
    generateRandomPokemon()
    guessPokemon()
