from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.x_position = 0
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    
    def add_segment(self, position):
        _ = Turtle(shape="square")
        _.color("white")
        _.penup()
        _.goto(position)
        self.segments.append(_)


    def extend(self):
        # add a new segment to the code
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.new_x = self.segments[seg_num - 1].xcor()
            self.new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(self.new_x, self.new_y)
        self.head.forward(20)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)