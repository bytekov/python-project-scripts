from turtle import Turtle
import random

# Crossing turtle/object parameters
COLORS = ["red","orange","yellow","green","blue","purple"]
MOVE_PACE = 10
MOVE_INCREMENT = 10

class CarMng:
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_PACE
        
    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            ran_y = random.randint(-240,240)
            new_car.goto(300,ran_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(MOVE_PACE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
    