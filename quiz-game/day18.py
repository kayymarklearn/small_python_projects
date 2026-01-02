import turtle
import random
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270]
tim = turtle.Turtle()
tim.speed("fastest")
tim.shape("triangle")
tim.pensize(2)

def draw_spirograph(size_of_gap):
    for _ in range((int(360/size_of_gap))):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)

draw_spirograph(2)

screen = turtle.Screen()
screen.exitonclick()