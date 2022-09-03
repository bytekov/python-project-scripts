from turtle import Turtle 

class Snake:
    def __init__(self):
        self.snk_container = []
        self.part_positions = [(0,0), (-20,0), (-40,0)]
        self.create_snk_parts()
        self.head = self.snk_container[0]   
   
    # Uses turtle-shapes to construct a snake 
    def create_snk_parts(self):
        for position in self.part_positions:
            part = Turtle(shape="square")
            part.color("green")
            part.penup()
            part.goto(position)
            self.snk_container.append(part)
    
    # Moves snake forward bound by the heading parts position     
    def move(self):
        # Iterates backwards from the length of the snake container
        for target in range(len(self.snk_container) - 1, 0, -1):
            # Sets/Moves current part to the position of the part ahead of it
            x_pos = self.snk_container[target - 1].xcor()
            y_pos = self.snk_container[target - 1].ycor()
            self.snk_container[target].goto(x_pos, y_pos)
        # Moves the head part forward
        self.head.fd(20)
    
    # Changes direction of the snake
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    # Resets and create a new snake shape    
    def reset(self):
        for item in self.snk_container:
            item.goto(1000,1000)
        self.snk_container = []
        self.create_snk_parts()
        self.head = self.snk_container[0]
        