from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(n = 0)

pesho = Snake()

screen.listen()
screen.onkey(key="Left", fun = pesho.left)
screen.onkey(key="Right", fun = pesho.right)
screen.onkey(key="Up", fun = pesho.up)
screen.onkey(key="Down", fun = pesho.down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    pesho.move()
    

screen.exitonclick()