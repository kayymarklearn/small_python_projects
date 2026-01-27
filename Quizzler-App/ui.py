from tkinter import * # type: ignore
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
SCORE_FONT = ("Firacode Nerd Font", 16, "bold")
QUESTION_FONT = ("Firacode Nerd Font", 16, "italic")

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=0, bg=THEME_COLOR)

        self.score_label = Label()
        self.score_label.config(text="Score: 0", fg="white", bg=THEME_COLOR, font=SCORE_FONT)    
        self.score_label.grid(row=0, column=1, pady=(0, 7))

        self.question_canvas = Canvas(width=300, height=250)
        self.question_text = self.question_canvas.create_text(150, 
                                                              125,
                                                              width=280,
                                                              text="questions here!", 
                                                              fill=THEME_COLOR, 
                                                              font=QUESTION_FONT) # type: ignore
    
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=15)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, borderwidth=0, highlightthickness=0, command=self.check_true)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, borderwidth=0, highlightthickness=0, command=self.check_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()



        self.window.mainloop()   

    def get_next_question(self):
        self.question_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text) # type: ignore
        else:
            self.question_canvas.itemconfigure(self.question_text, text="You have reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True")) # pyright: ignore[reportUnknownMemberType]

    def check_false(self):
        self.give_feedback(self.quiz.check_answer("False")) # type: ignore
    
    def give_feedback(self, is_right: bool):
        if is_right:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        
        self.window.after(1000, self.get_next_question)