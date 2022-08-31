import pandas
import turtle

# Set up turtle window object
wn = turtle.Screen()
wn.title("U.S States Game")
image = "blank_states_img.gif"
wn.addshape(image)
turtle.shape(image)

# List to keep track of user's typed states
typed_states = []

# Keep game running while user hasn't typed all states
while len(typed_states) < 50:
    # Read states data from csv file
    data = pandas.read_csv("50_states.csv")
    answer = wn.textinput("Guess the state", "What is the capital of the state?").capitalize()
    
    # Updates global list if answer is correct | Program exits if answer='EXIT' or pass if wrong  
    if answer == "Exit":
        break
    elif data[data.state == answer].empty:
        pass 
    else :
        current_row = data[data.state == answer]
        typed_states.append(answer)
        tur = turtle.Turtle()
        tur.hideturtle()
        tur.penup()
        tur.goto(int(current_row.x) , int(current_row.y))
        tur.write(current_row.state.item())
        
# Get mouse click events
def get_mouse_click(x,y):
    print(x,y)
    
# Keep turtle window on while game is running
turtle.onscreenclick(get_mouse_click)
turtle.mainloop()