from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(n = 0)

pesho = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    screen.listen()
    screen.onkey(key="Left", fun = pesho.turn_left)
    screen.onkey(key="Right", fun = pesho.turn_right)
    screen.onkey(key="Up", fun = pesho.move_forward)
    screen.onkey(key="Down", fun = pesho.move_backward)
    

screen.exitonclick()