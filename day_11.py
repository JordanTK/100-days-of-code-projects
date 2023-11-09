# Simplified Blackjack

#import the logo,the random package,emoji package,  and os.system to clear the console
from art_11 import logo
import random
from os import system
import emoji

# list of cards without replacement
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Choosing a card
def choose_card():
    return random.choice(cards)

# Starting the game
start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while start == "y":
    #show the logo
    print(logo)
    # List data structure to store player cards-hand
    player_cards = []
    computer_cards = []

    # Picking two cards for the player and the computer
    player_card_1 = choose_card()
    computer_card_1 = choose_card()
    player_card_2 = choose_card()
    computer_card_2 = choose_card()

    # Allow the player or computer to continue in the rare case they draw two aces
    if player_card_1 == 11 and player_card_2 ==11:
        player_card_2 = 1

    if computer_card_1 == 11 and computer_card_2 ==11:
        computer_card_2 = 1
    
    # Add the player cards to his hand
    player_cards.append(player_card_1)
    player_cards.append(player_card_2)

    # Add the computer cards to the computer's hand
    computer_cards.append(computer_card_1)
    computer_cards.append(computer_card_2)

    # Get the score of player
    player_score = sum(player_cards)
    computer_score = sum(computer_cards)

    # Establish the computer gameplay
    while computer_score < 17:
        computer_cards.append(choose_card())
        computer_score = sum(computer_cards)

    # Player gameplay and prompt
    while player_score <21: 
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_card_1}")
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "y":
            player_cards.append(choose_card())
            player_score = sum(player_cards)
        else:
            break
    
    # What happens if you hit a blackjack
    if player_score == 21:
        print(f"Your cards: {player_cards}, current score: {0}")
        print(f"Computer's first card: {computer_card_1}")
    
    # Showing the final results
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    # Establish the results and output
    if player_score > 21:
        print(emoji.emojize("You went over. You lose :loudly_crying_face:"))
    elif player_score == 21 and computer_score != 21:
        print(emoji.emojize("Win with a Blackjack :smiling_face_with_sunglasses:"))
    elif computer_score < 21 and player_score < 21 and player_score > computer_score:
        print(emoji.emojize("You win :grinning_face_with_big_eyes:"))
    elif computer_score <= 21 and player_score < 21 and player_score < computer_score:
        print(emoji.emojize("You lose :face_with_steam_from_nose:"))
    elif computer_score > 21 and player_score < 21:
        print(emoji.emojize("Oponent went over. You win :beaming_face_with_smiling_eyes:"))
    else:
        print(emoji.emojize("It is a draw :man_shrugging:"))
    
    
    # Ask again whether to keep going or stop after this game
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start == "y":
        system("clear")






