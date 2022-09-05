from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        # Calls this module as turtle instance
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        
        self.l_player_score = 0 
        self.r_player_score = 0
        
        self.goto(-100 , 200)
        self.write(self.l_player_score , align = "center" , font = ("Courier" , 80 ,"normal"))
        self.goto(100 , 200)
        self.write(self.r_player_score , align = "center" , font = ("Courier" , 80 ,"normal"))
    
    def update_s(self):
        self.goto(-100 , 200)
        self.write(self.l_player_score , align = "center" , font = ("Courier" , 80 ,"normal"))
        self.goto(100 , 200)
        self.write(self.r_player_score , align = "center" , font = ("Courier" , 80 ,"normal"))

    def r_point(self):
        self.clear()
        self.r_player_score += 1
        self.update_s()


    def l_point(self):
        self.clear()
        self.l_player_score += 1
        self.update_s()
        