from turtle import Turtle,Screen
import time
MOVE_DISTANCE = 20
class Snake:
     def __init__(self):
        self.body = []
        self.create_snake()

     def create_snake(self):
        for position in range(3):
            square = Turtle()
            square.shape("square")
            square.color("white")
            square.penup()
            square.goto((-position*20,0))
            self.body.append(square)
     
     def move_forward(self):
         for part in self.body:
             part.forward(MOVE_DISTANCE)
     
     def move_backward(self):
         for part in self.body:
             part.backward(MOVE_DISTANCE)
     
     def turn_left(self):
         turning_segment = 0
         for _ in range(len(self.body)):
            for index in range(len(self.body)):
                if index == turning_segment:
                    self.body[index].left(90)
                    self.body[index].forward(MOVE_DISTANCE)
                else:
                    self.body[index].forward(MOVE_DISTANCE)
            turning_segment+=1
            
             
     def turn_right(self):
         turning_segment = 0
         for _ in range(len(self.body)):
            for index in range(len(self.body)):
                if index == turning_segment:
                    self.body[index].right(90)
                    self.body[index].forward(MOVE_DISTANCE)
                else:
                    self.body[index].forward(MOVE_DISTANCE)
            turning_segment+=1
