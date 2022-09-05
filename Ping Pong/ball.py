from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        # Calls this module as turtle instance
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.goto(0,0)
        self.speed("fastest")
        self.x_dir_catalyst = 10
        self.y_dir_catalyst = 10 
    
    # Moves object to y or x direction incrementally by x/y_dir_catalyst
    def  move(self):
        self.goto(self.xcor() + self.x_dir_catalyst, self.ycor() + self.y_dir_catalyst)
    
    def reset(self):
        self.goto(0,0)
        self.x_dir_catalyst *= -1