from turtle import Turtle

# Crossing turtle/object parameters
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        # Calls this module as a turtle instance
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.goto_start()
        self.setheading(90)
        self.speed("fastest")

    def move(self):
        self.fd(MOVE_DISTANCE)
    
    def finished(self):
        if self.ycor() > FINISH_LINE:
            return True
    def goto_start(self):
        self.goto(STARTING_POSITION)
    
    