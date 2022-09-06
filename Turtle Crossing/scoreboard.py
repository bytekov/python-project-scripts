from turtle import Turtle

FONT_FORMATTING = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        # Call this module as an instace of turtle
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.write("Score: 0", align="center", font=("Courier", 24, "normal"))
        self.score = 0
        
    # Updates whole module text 
    def update(self):
        self.clear()
        self.write("Score: {}".format(self.score), align="center", font= FONT_FORMATTING)
    
    # Updates game score 
    def count_score(self):
        self.score += 1
        self.update()
        
    # Stops game 
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT_FORMATTING)