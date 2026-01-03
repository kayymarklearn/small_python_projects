from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "cyan", "magenta", "teal", "lime", "maroon", "navy", "purple", "brown", "black", "gray", "gold"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, car_speed=0):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.color(choice(COLORS))
        self.setheading(180)
        self.goto(300, randint(-250, 250))
        self.speed("fastest")
        self.car_speed = car_speed
        self.car_speed += STARTING_MOVE_DISTANCE
        self.car_move()
    
    def car_move(self):
        self.forward(self.car_speed)