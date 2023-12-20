from turtle import Turtle,Screen
import time
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
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

     
     def add_square(self, position):
         square = Turtle()
         square.shape("square")
         square.color("white")
         square.penup()
         square.goto(position)
         self.body.append(square)

     def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)
            
             
     def extend(self):
         self.add_square(self.body[-1].position())
         
         
     
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
