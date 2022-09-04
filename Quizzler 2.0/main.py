from question_module import Question
from data import question_data
from Question_Mngr import Question_Mngr
from ui import QuizInterface

# Create a list of question objects
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create a QuizBrain object
quiz = Question_Mngr(question_bank)

# Create a QuizInterface object
interface = QuizInterface(quiz)


