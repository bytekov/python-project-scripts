from  turtle import Turtle 

class Score(Turtle):
    def __init__(self):
        # Calls this module as a turtle object
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.write("Score: 0", align="center", font=("Courier", 24, "normal"))
        self.score = 0
        # Read high score from file
        with open("data.txt") as data:
            self.high_score = int(data.read())
    
    # Updates the score on the screen
    def update(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align="center", font=("Courier", 24, "normal"))
    
    # Increases the score by 1
    def counter(self):
        self.score += 1
        self.update()

    # Update/Resets the score file/value
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt" , mode="w") as old_data:
                old_data.write(str(self.score))
        self.score = 0
        self.update()

    
            
    