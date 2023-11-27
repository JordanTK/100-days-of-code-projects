from turtle import Turtle, Screen
from random import randint

def set_race(index):
    pesho = Turtle(shape = "turtle")
    pesho.penup()
    pesho.goto(x = -230, y = -75+index*25)
    pesho.color(colors[index])
    return pesho

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which colored turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
racers = [set_race(i) for i in range(6)]


if user_bet:
    is_race_on = True

while is_race_on:
    for racer in racers:
        racer.pendown()
        paces = randint(0,10)
        racer.forward(paces)
        if racer.xcor() >= 200:
            is_race_on = False
            winner = racer.color()
            break

print(f"The winner is the {winner[1]} turtle.")
if winner[1] == user_bet:
    print("You are correct. You won")
else:
    print("You didn't get it right. Better luck next time")


screen.exitonclick()