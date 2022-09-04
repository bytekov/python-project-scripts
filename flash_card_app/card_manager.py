
from main import english_func
from main import window , app_canv , bg_photo , words_to_learn , card_back , card_title , card_word , card_front
import random

class CardManager:
    def __init__(self):
        self.current_word = None
        self.function_timer = window.after(3000 , english_func)
    
    # Switches back image | Displays english word of the displayed french word
    def english_func(self):
        global current_word
        app_canv.itemconfig(bg_photo , image=card_back)
        current_word = random.choice(words_to_learn)
        app_canv.itemconfig(card_title , text = "English")
        app_canv.itemconfig(card_word , text = current_word["English"])

#***************************** Display French Func   ************************#
    def next_card(self):
        global current_word , func_timer
        window.after_cancel(func_timer)
        app_canv.itemconfig(bg_photo , image=card_front)
        current_word = random.choice(words_to_learn)
        app_canv.itemconfig(card_title , text = "French")
        app_canv.itemconfig(card_word , text = current_word["French"])
        func_timer = window.after(3000 , english_func)