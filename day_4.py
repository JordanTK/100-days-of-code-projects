# Rock, paper, scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)
else:
    print(f"You can only choose between rock paper and scissors. Please type in {0}, {1}, or {2}")

computer_choice = random.randint(0,2)

print("Computer chose:")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if player_choice == computer_choice:
    print("It is a draw.")
else:
    if abs(player_choice-computer_choice) == 1:
        if player_choice < computer_choice:
            print("You lose")
        else:
            print("You win")
    else:
        if player_choice < computer_choice:
            print("You win")
        else:
            print("You lose")