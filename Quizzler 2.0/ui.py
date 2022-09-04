THEME_COLOR = "#375362"
from faulthandler import disable
from tkinter import *   
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self , quiz_obj:QuizBrain):
        self.quiz = quiz_obj
        self.window = Tk()
        self.window.title("Quizzler")
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
    def get_question(self):
        if self.quiz.still_has_questions():
            self.app_canvas.config(bg='white') 
            q_text = self.quiz.next_question()
            self.app_canvas.itemconfig(self.question_txt, text=q_text) 
        else:
            self.app_canvas.itemconfig(self.question_txt, 
            text =f"Quiz Done \n Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')
            
        
    def true_func(self):
        if "True" == self.quiz.check_answer():
            self.quiz.score += 1
            self.app_canvas.config(bg='green')     
        else:
            self.app_canvas.config(bg='red')
        self.window.after(400 , self.get_question)

    def false_func(self):
        if "False" == self.quiz.check_answer():
            self.quiz.score += 1
            self.app_canvas.config(bg='green')     
        else:
            self.app_canvas.config(bg='red')
        self.window.after(400 , self.get_question)
        

