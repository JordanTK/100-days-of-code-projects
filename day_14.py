# Import the logo and the game data plus a function for picking a random integer in a given range
from art_14 import logo, vs
from game_data_14 import data
from random import sample

# Getting a random dictionary from the data
datas = sample(data, 2)
data_A = datas[0]
data_B = datas[1]

# Start of the game
keep_going = True
print(logo)
score = 0

while keep_going:

    print(f"Compare A: {data_A['name']}, a {data_A['description']}, from {data_A['country']}.")
    print(vs)
    print(f"Against B: {data_B['name']}, a {data_B['description']}, from {data_B['country']}.")
    higher_lower = input("Who has more followers? Type 'A' or 'B': ").lower()

    if data_A["follower_count"] > data_B["follower_count"]:
        answer = "a"
    else:
        answer = "b"

    if higher_lower == answer:
        score+=1
        data_A = data_B
        data_B = sample(data, 1)[0]
        print(logo)
        print(f"You're right  Current score: {score}.")
    
    else:
        break
print(logo)
print(f"Sorry, that's wrong. Final score: {score}")