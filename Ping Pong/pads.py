from turtle import Turtle

class Pad(Turtle):
    def __init__(self , pos):
        # Calls this module as turtle instance
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.shapesize(5,1)
        self.goto(pos , 0)
    
    def pad_up(self):
        new = self.ycor() + 20
        self.sety(new)

    def pad_down(self):
        new = self.ycor() - 20
        self.sety(new)
