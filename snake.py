from turtle import Turtle,Screen
import time
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
     def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

     def create_snake(self):
        for position in range(3):
            square = Turtle()
            square.shape("square")
            square.color("white")
            square.penup()
            square.goto((-position*20,0))
            self.body.append(square)
     
     def move(self):
        for part in range(len(self.body) - 1, 0, -1):
            new_x = self.body[part - 1].xcor()
            new_y = self.body[part - 1].ycor()
            self.body[part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

     def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

     def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

     def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

     def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
