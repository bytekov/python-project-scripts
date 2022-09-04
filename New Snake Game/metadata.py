from turtle import Turtle
import random

from scoreb import TEXT_FORMAT, FONT_DATA

class Mood(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(0.5 , 0.5)
        self.color("blue")
        self.speed("fastest")
        #self.hideturtle()
        self.refresh()
    def refresh(self):
        self.clear()
        self.goto(random.randint(-320,320) , random.randint(-320,320))
        self.write("h", align= TEXT_FORMAT, font = FONT_DATA)
    
class Food:
    def __init__(self , name_string):
        # Create a list of wrong/void letters
        self.wrong_food = ["m","e","r","a"]
        self.all_food = []
        
        # Create a list of the actuall letters
        self.correct_food = list(name_string)
        
        # A list of mixed correct and wrong letters
        self.mixed_food = [*self.correct_food ,*self.wrong_food]
        self.create_food()
    
    # Create food objects and append to main list 
    def create_food(self):
        for food_letter in self.mixed_food:
            food_item = Turtle()
            food_item.penup()
            food_item.shapesize(0.8 , 0.8)
            food_item.color("blue")
            food_item.letter = food_letter
            food_item.speed("fastest")
            
            # Sets a random position for food item and writes the letter strapped to it
            food_item.goto(random.randint(-300,300) , random.randint(-300,300))
            food_item.write(f"{food_letter}", align= TEXT_FORMAT, font = FONT_DATA)
            #food_item.hideturtle()          
            self.all_food.append(food_item)

        
            
            
            
