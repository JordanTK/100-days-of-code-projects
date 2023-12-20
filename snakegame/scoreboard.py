from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.goto(0,280)
        self.color("white")
        self.write(arg= f"Score: {self.score}", align= "center", font= ("Calibri",10,"bold"))




    def score_food(self):
        self.clear()
        self.score+=1
        self.write(arg= f"Score: {self.score}", align= "center", font= ("Calibri",10,"bold"))
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg= "GAME OVER", align= "center", font= ("Calibri",10,"bold"))