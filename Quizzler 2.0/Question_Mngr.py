from cgitb import html
import html

class Question_Mngr:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    # Returns a boolean if there is no/more answers
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Returns a next question
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        
        self.question_number += 1
        
        question_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {question_text} (True/False): "

    # Returns boolean of correct answer from current question
    def check_answer(self):
        correct_answer = self.current_question.answer
        return correct_answer

    
