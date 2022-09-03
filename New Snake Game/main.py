#project imports
from turtle import Turtle , Screen
from snake import Snake
from metadata import  Food
from scoreb import Score
import time

# Turtle screen setup
wn = Screen()
wn.setup(650 , 650)
wn.title("Snake Game")
wn.bgcolor("black")
wn.tracer(0)


# Takes player name as snake food elements
player_name = wn.textinput(title = "Player Name" , prompt="Type in your name")

# Class instances
snake = Snake()
food = Food(player_name)
scores = Score(player_name)
game_state = True
wn.listen()

# Key bindings
wn.onkey(snake.left, "Left")
wn.onkey(snake.right, "Right")
wn.onkey(snake.up, "Up")
wn.onkey(snake.down, "Down")

# Game loop
while game_state:
    wn.update()
    time.sleep(0.2) 
    snake.move()
    
    # Detect collision      
    for item in food.all_food:  
        
        # Detects collision with food
        if snake.head.distance(item) < 15 and snake.head.xcor() <= item.xcor() + 15 and snake.head.ycor() <= item.ycor() + 15:
            
            # Removes found food from correct_food list 
            if item.letter in food.correct_food:
                found_food = food.all_food[food.all_food.index(item)]
                found_food.clear()
                food.correct_food.remove(found_food.letter)
                scores.update_score()
                snake.extend()
            
            # Game over if wrong food is found
            else:
                game_state = False
                scores.game_lost()
        
        # Detects if all lettters has been found 
        elif len(food.correct_food) == 0:
                game_state = False
                scores.game_won()
                
                
    #detect collision with wall
    if snake.head.xcor() < -330 or snake.head.xcor() > 330 or snake.head.ycor() < -330 or snake.head.ycor() > 330:
        game_state = False
        scores.game_lost()
        
    
    # Detect collision with tail
    for item in snake.snk_container[1:]:
        if snake.head.distance(item) < 1:
            game_state = False
            scores.game_lost()

            
    






























