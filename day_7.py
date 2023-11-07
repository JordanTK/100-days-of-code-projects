# Hangman game

import random
from hangman_words import word_list
from hangman_art import *

print(logo)
# Picking a random word from a list of words
word = random.choice(word_list)

# Creating an empty word container

display = []
for word_count in range(len(word)):
    display.append("_")

# Continue guessing until you have guessed all the letters- you win.

end_of_game = False

# Creating a variable to store the remaining life points with an initial value of 6
lives = 6

# Starting the game
while not end_of_game:

# Making a guess, user types in a letter
    guess = input("Guess a letter! ").lower()

# Let the user know if they have guessed the letter already
    if guess in display:
        print("You have already tried this letter.")

# Checking if the guess matches any letter in the word 

    for index in range(len(word)):
        if guess == word[index]:
            display[index] = guess
    if guess not in word:
        print(f"{guess} is not in the word.")
        lives-=1
        if lives == 0:
            end_of_game = True
            print("You lose.")


    # Checking the status of the display
    print(f"{' '.join(display)}")

# All the letters ar filled
    if "_" not in display:
        end_of_game = True
        print("You win.")

# Show the hanging process
    print(stages[lives])


