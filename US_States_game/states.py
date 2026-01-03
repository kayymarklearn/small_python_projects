import turtle

FONT = ("Courier", 24, "bold")

class State(turtle.Turtle):
    def __init__(self, name, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.hideturtle()
        self.name = name
        self.penup()
        self.goto(self.x, self.y)
        self.write(f"{self.name}", align="center", font=FONT)