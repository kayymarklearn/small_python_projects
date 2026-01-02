from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def clock_wise():
    tim.right(10)

def anti_clock_wise():
    tim.left(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="a", fun=anti_clock_wise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()