import turtle
import pandas

# Sets up turtle window with background image
wn = turtle.Screen()
wn.title("Ghana States Game")
image = "ghana.gif"
wn.addshape(image)
wn.setup(width=800, height=600)
turtle.shape(image)

#  Reads csv data sets gameplay variables 
states_data = pandas.read_csv("data.csv")
states_list = states_data.state.to_list()
score = 0
typed_states = []

# Keeps game running while user hasnt typed all states
while score < 16:
    answer = wn.textinput(title = f"{score} regions correct", prompt="Guess a region in Ghana")

    try:
        answer.title()
    except AttributeError:
        answer = "no value"
        break
    else:
        pass
    finally:
        answer = answer.title()
        
    if answer == "End":
        # Creates a csv file with user missed states | end the game if answer == 'END'
        untyped_states = [state for state in states_list if state not in typed_states]
        missed_states = pandas.DataFrame(untyped_states)
        missed_states.to_csv("missing_states.csv")
        break
    elif answer in states_list:
        # Updates global answered_list , score if answer is correct
        score += 1
        typed_states.append(answer)
        # Create and send turtle to cordinate using typed-state meta
        tur = turtle.Turtle()
        tur.hideturtle()
        tur.penup()
        tur.goto(int(states_data[states_data.state == answer].x) , int(states_data[states_data.state == answer].y))
        tur.write(states_data[states_data.state == answer].state.item())

# Turtle object writes down all correct answers on screen
end_tur = turtle.Turtle()
end_tur.shape("arrow")
end_tur.penup()
end_tur.shapesize(0.5,0.5)
end_tur.speed("slow")
x = -380 
y =  250
for item in states_list:
    end_tur.goto(x , y)
    end_tur.write(item , font=("Arial", 10, "normal"))
    y -= 20    
end_tur.goto(x , y - 20) 
end_tur.write("THESE REGIONS OF GHANA." , font=("Arial", 15, "normal"))

# Keep turtle window on while game is running
wn.mainloop()
