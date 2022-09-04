
from turtle import Turtle , Screen
from player import Player
from object_manager import CarMng
from scoreboard import Scoreboard
import time
import random

# Turtle screen setup
wn = Screen()
wn.setup(width=800 , height=600)
wn.title("Turtle Crossing")
wn.bgcolor("black")
wn.tracer(0)
wn.listen()

# Class instances
game_state = True
game_turtle = Player()
crossing_items = CarMng()
game_score = Scoreboard()

wn.onkey(game_turtle.move, "Up")

# Game loop
while game_state:
    wn.update()
    time.sleep(0.1)

    crossing_items.create_cars()
    crossing_items.move()

    for car in crossing_items.all_cars:
        if car.distance(game_turtle) < 20:
            game_score.game_over()
            game_state = False

    if game_turtle.finished():
        game_score.count_score()
        game_turtle.goto_start()
        

wn.exitonclick()













