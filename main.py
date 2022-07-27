from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
"""
Tkinter works by having these endless loop essentially that's called main loop and this is like never ending while loop.
It is constantly checking to see if it needs update something in the GUI or if the user has interacted in some sort of
way so it will get confused if we have another while loop somewhere near it  So we actually have to comment out this 
while loop if we want this user interface to work properly.
"""

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

