from tkinter import *
import pandas
import random

# Keeps words to learn as a dict
words_to_learn = {}

# Applies background color to the window
BACKGROUND_COLOR = "#B1DDC6"

try:
    # Try if there are words to learn by user
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    # If false read actuall data into wordstolearn dict
    actuall_data = pandas.read_csv('data/french_words.csv')
    words_to_learn = actuall_data.to_dict(orient="records")
else:
    # If true read words to learn into wordstolearn dict
    words_to_learn = data.to_dict(orient="records")


#***************************** Display English func     *******************************#
# Keeps current word to be display in canvas
current_word = None

# Switches back image | Displays english word of the displayed french word
def english_func():
    global current_word
    
    app_canv.itemconfig(bg_photo , image=card_back)
    current_word = random.choice(words_to_learn)
    app_canv.itemconfig(card_title , text = "English")
    app_canv.itemconfig(card_word , text = current_word["English"])

#***************************** Display French Func   ************************#

# Switches back image | Displays french word

def actuall_word_func():
    global current_word , func_timer
    
    # Terminates the running english_func 
    window.after_cancel(func_timer)
    
    app_canv.itemconfig(bg_photo , image=card_front)
    current_word = random.choice(words_to_learn)
    app_canv.itemconfig(card_title , text = "French")
    app_canv.itemconfig(card_word , text = current_word["French"])
    
    # Runs english_func after 3000ms of running french_func 
    func_timer = window.after(3000 , english_func)
    
#***************************** Manage words     *******************************#

def known_word_func():
    # Removes recognized words
    words_to_learn.remove(current_word)
    actuall_word_func()
    

# Create user interface
window = Tk()
window.title("Flash App")
window.config(padx=50,pady=20 ,bg=BACKGROUND_COLOR)

# Sets timer to run english_func after 3000ms
func_timer = window.after(3000 , english_func)

card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
green_btn = PhotoImage(file='images/right.png')
red_btn = PhotoImage(file='images/wrong.png')

app_canv = Canvas(width=800,height=526,background=BACKGROUND_COLOR,highlightthickness=0)
bg_photo = app_canv.create_image(400,263 , image = card_front)
app_canv.grid(row=0,column=0 , columnspan=2)
card_title = app_canv.create_text(400,150 , font=("Ariel" , 30,"italic"))
card_word = app_canv.create_text(400,263 , font=("Ariel" , 60,"italic"))
known_btn = Button(image = green_btn,highlightthickness=0 , command = known_word_func)
unknown_btn = Button(image=red_btn,highlightthickness=0 , command= actuall_word_func())
known_btn.grid(row=1,column =0)
unknown_btn.grid(row=1,column =1)

if True:
    actuall_word_func()

window.mainloop()

unknown_words_data = pandas.DataFrame(words_to_learn)
unknown_words_data.to_csv('data/words_to_learn.csv' , index=False)