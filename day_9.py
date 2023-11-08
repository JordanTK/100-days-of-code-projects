# Secret auction

# Getting the logo 
from art_9 import logo
 
# Clearing the console after each step
from os import system

# Logo and greeting
print(logo)
print("Welcome to the secret auction program.")

# Creating the data structure namely a dictionary to store the bidders and their bid
bidders = {}

# Keeps asking for the name of the bidder and the amount of the bid until there is no one left
other_bidders = True
while other_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid? ").replace("$", ""))
    bidders[name] = bid
    other = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    system("clear")
    if other == "no":
        other_bidders = False

# Determines the winner of the auction
best_bid = max(bidders.values())
for key in bidders:
    if bidders[key] == best_bid:
        best_bidder = key
        break

print(f"The winner is {best_bidder} with a bid of ${best_bid}.")