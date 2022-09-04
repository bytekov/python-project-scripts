from turtle import Turtle

# Text formattings
TEXT_FORMAT = "center"
FONT_DATA = ("Courier" , 20, "normal")

class Score(Turtle):
    def __init__(self , name):
        # Calls this module as a turtle object
        super().__init__()
        self.username = name
        self.scored = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write_score()

    # Writes the score to the screen
    def write_score(self):
        self.write(f"Name:{self.username} Found: {self.scored}", align= TEXT_FORMAT, font = FONT_DATA)

    # Display game over 
    def game_lost(self):
        self.goto(0,0)
        self.write(f"GAME OVER You lost!", align= TEXT_FORMAT, font = FONT_DATA)
        
    
    # Display game owon
    def game_won(self):
        self.goto(0,0)
        self.write(f"Congratulations!", align= TEXT_FORMAT, font = FONT_DATA)

    # Update score data  
    def update_score(self):
        self.scored += 1
        self.clear()
        self.write_score()
    
        
