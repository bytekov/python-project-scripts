from turtle import Turtle
import random
from scoreb import TEXT_DATA, FONT_DATA

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.box = ["h","e","l","l","o",]
        self.penup()
        self.shapesize(0.5 , 0.5)
        self.color("blue")
        self.speed("fastest")
        self.hideturtle()
        self.refresh()
    def refresh(self):
        self.clear()
        self.goto(random.randint(-320,320) , random.randint(-320,320))
        self.write("h", align= TEXT_DATA, font = FONT_DATA)
    def make_f(self):
        pass
        
            
            
            
