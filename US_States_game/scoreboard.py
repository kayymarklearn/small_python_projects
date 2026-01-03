from turtle import Turtle
FONT = ("Courier", 40, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-250, -230)
        self.write_score()
    
    def write_score(self):
        self.write(f"{self.score}/50 States Correct", align="center", font=FONT)

    
    def update(self):
        self.clear()
        self.score += 1
        self.write_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
    
