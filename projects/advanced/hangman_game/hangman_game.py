# This is program for the game, Hangman. 
# This program generates a random word and you have 6 attempts to guess it.

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# This function makes a random program. 
def makeRandomWord():
    words = ['random', 'human', 'tree', 'vegetable', 'fruit', 'hello', 'world']
    random_word = random.choice(words)
    print("\n")
    return random_word

# This function takes the user input and calculates the length of the word. 
def playHangman(random_word):
    guess_word = []
    game_over = True
    random_word_length = len(random_word)
    lives = 6
    print (f"You have {lives} attempts to guess this word.")

    for i in (random_word):
        guess_word.append('_')
    print("Guess word", guess_word)
    
    while game_over:
        user_letter = input("Enter a letter:").lower()

        if user_letter in guess_word:
            print ("You already guess this letter.")

        for position in range(random_word_length):
            if user_letter == random_word[position]: 
               guess_word[position] = user_letter 
               print(guess_word)

        if user_letter not in random_word:
            print("Letter is not there.")
            lives-=1
            if lives == 0:
                print("You have lost all your lives. You lose.")
                game_over = False

        if '_' not in guess_word:
            print("You won the game.")
            game_over = False
    
        print(stages[lives])

    print(guess_word)
    print(random_word)

# Code Execution Begins
if __name__ == "__main__":
    random_word = makeRandomWord() 
    playHangman(random_word)

