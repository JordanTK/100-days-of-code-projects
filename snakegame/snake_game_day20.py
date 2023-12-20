from turtle import Turtle, Screen
import time
from snake import Snake
from snake_food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(n = 0)

pesho = Snake()
popcorn = Food()
board = Scoreboard()


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
    # Detect collision with popcorn
    if pesho.head.distance(popcorn) < 15:
        popcorn.refresh()
        pesho.extend()
        board.score_food()

    
    # Detect collision with wall.
    if abs(pesho.head.xcor()) > 280 or abs(pesho.head.ycor()) > 280:
        game_is_on = False
        board.game_over()
    
    # Detect collision with tail.
    for square in pesho.body[1:]:
        if pesho.head.distance(square) < 10:
            game_is_on =False
            board.game_over()  

screen.exitonclick()
