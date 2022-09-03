#Libraries
from turtle import *
import time
from snake import Snake
from food import Food
from scoreboard import Score

#Turtle window
wn = Screen() 
wn.setup(width = 600, height = 600)
wn.title("Snake Game")
wn.tracer(0)
wn.bgcolor("black")

#Class instances
snake = Snake()
food = Food()
scores = Score()
game_state = True
wn.listen()

#Key bindings
wn.onkey(snake.left, "Left")
wn.onkey(snake.right, "Right")
wn.onkey(snake.up, "Up")
wn.onkey(snake.down, "Down")

#Game/Program loop
while game_state:
    wn.update()
    time.sleep(0.2) 
    snake.move()

    # Detect collision with food 
    if snake.head.distance(food) < 15:
        food.refresh()
        scores.counter()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scores.reset()
        snake.reset()
       
    # Detect collision with snake
    for item in snake.snk_container:
        if item == snake.head:
            pass
        elif snake.head.distance(item) < 10:
            scores.reset()
            snake.reset()
            
           







