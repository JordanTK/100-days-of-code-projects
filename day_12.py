# Number guessing game
from random import randint

# Introduction
print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100.")

# Picking the difficulty level
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "hard":
    attempts = 5
elif difficulty == "easy":
    attempts = 10
else:
    print("Pick a correct difficulty.")
    attempts = -1

# Generate a random number between 1 and 100
number = randint(1,100)

# Start the game
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
    # Keep going until you hit the number or run out of attempts 
    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print(f"You got it! The answer was {number}.")
        break
    attempts -=1

# What happens if you lose
if attempts == 0:
    print("You've run out of guesses, you lose.")
