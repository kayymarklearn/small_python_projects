from turtle import Turtle
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 1


class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.x_position = x_position
        self.y_position = y_position
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.goto(self.x_position, self.y_position)

    
    def move_up(self):
        self.goto(x=self.x_position, y=self.ycor()+20)
    
    def move_down(self):
        self.goto(x=self.x_position, y=self.ycor()-20)
