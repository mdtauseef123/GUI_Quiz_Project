from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
"""
To specify the type of the variable quiz_brain we use the syntax quiz_brain: QuizBrain that the type of the quiz_brain
is of QuizBrain class.
"""


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score:0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        """
        We have set the width property to 280 because the question is not properly visible in the canvas as the question 
        is being hidden due to the large size of the question. In order to avoid this we can call the width property and
        set it to less than the size of the canvas which will help in changing the line for the question instead of 
        filling the question in the same line.
        """
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Some Question Text",
                                                     fill=THEME_COLOR,
                                                     font=FONT
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50, padx=20)
        correct_image = PhotoImage(file="images/true.png")
        self.correct_img = Button(image=correct_image, highlightthickness=0, command=self.correct_answer)
        self.correct_img.grid(row=2, column=0)
        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_img = Button(image=wrong_image, highlightthickness=0, command=self.wrong_answer)
        self.wrong_img.grid(row=2, column=1)
        #In order to put the question for the very first time on the screen we have used the following syntax
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        """
        Since we have only put 10 questions so once we reached to the end of the question then we shouldn't access the
        question as we have iterated all the questions and reach end of the list, so we have to check an if condition
        that, if there is any question left then only next question will take place and all otherwise we will pop up the
        message that the user have reached the end of the quiz, and also we will disable the right and wrong buttons.
        :return:
        """
        #We want everytime our canvas to be white background
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You\'ve reached the end of the Quiz.")
            #To disable the correct and wrong buttons
            self.correct_img.config(state="disabled")
            self.wrong_img.config(state="disabled")

    def correct_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(2000, func=self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(2000, func=self.get_next_question)
