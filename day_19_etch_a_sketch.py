from turtle import Turtle, Screen

# Initializing a turtle named zoro and a screen 
zoro = Turtle()
screen = Screen()

# Create the function to bind to
def move_forwards():
    zoro.fd(10)
def move_backwards():
    zoro.bk(10)
def clockwise():
    zoro.right(5)
def anticlockwise():
    zoro.left(-5)
# Start listening for events
screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "d", fun = clockwise)
screen.onkey(key = "a", fun = anticlockwise)
screen.exitonclick()