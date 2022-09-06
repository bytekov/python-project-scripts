from faulthandler import disable
from tkinter import *   
from Question_Mngr import Question_Mngr

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self , question_mngr_object: Question_Mngr):
        self.question_mngr = question_mngr_object
        
        # Create tkinter window with canvas
        self.window = Tk()
        self.window.title("question_mngr Script")
        self.window.config(padx=10, pady=10 , bg=THEME_COLOR)
        self.score_label = Label(self.window, text="Your Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.app_canvas = Canvas(self.window, width=300, height=250)
        self.question_txt = self.app_canvas.create_text(
            150, 
            125, 
            width=280,
            text="Some text will come here ", 
            font=("Arial", 20), 
            fill=THEME_COLOR)
        self.app_canvas.grid(row=1, column=0 , columnspan=2 , pady=40)
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_btn = Button(self.window, image=true_img ,highlightthickness=0 , command=self.true_func)
        self.true_btn.grid(row=2, column=0)
        self.false_btn = Button(self.window, image=false_img ,highlightthickness=0 , command = self.false_func)
        self.false_btn.grid(row=2, column=1)
        
        self.get_question()
        self.window.mainloop()
       
    # Get the next question from the question_mngr object if there is more 
    def get_question(self):
        if self.question_mngr.still_has_questions():
            self.app_canvas.config(bg='white') 
            next_question = self.question_mngr.next_question()
            self.app_canvas.itemconfig(self.question_txt, text=next_question) 
        else:
            self.app_canvas.itemconfig(self.question_txt, 
            text =f"question_mngr Done \n Your final score was: {self.question_mngr.score}/{self.question_mngr.question_number}")
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')
            
    # Checks if true is equal to question answer value
    def true_func(self):
        if "True" == self.question_mngr.check_answer():
            self.question_mngr.score += 1
            self.app_canvas.config(bg='green')     
        else:
            self.app_canvas.config(bg='red')
        self.window.after(400 , self.get_question)

    # Checks if false is equal to question answer value
    def false_func(self):
        if "False" == self.question_mngr.check_answer():
            self.question_mngr.score += 1
            self.app_canvas.config(bg='green')     
        else:
            self.app_canvas.config(bg='red')
        self.window.after(400 , self.get_question)
        

