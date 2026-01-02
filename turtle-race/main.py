from turtle import Turtle, Screen
import random
import sys

# colors to use for turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# setup the screen
screen = Screen()
screen.setup(width=500, height=400)

# ask user to place a bet
is_race_on = False
good_color = True
while good_color:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (rainbow colors only): ").lower()
    if user_bet not in colors:
        pass
    else:
        good_color = False

#Create six turtles for race use colors of rainbow
# tim
# tim = Turtle(shape="turtle")
# tim.color("red")
# tim.penup()
# tim.goto(x=-230, y=-180)

# # tom
# tom = Turtle(shape="turtle")
# tom.color("orange")
# tom.penup()
# tom.goto(x=-230, y=-150)

# # tam
# tam = Turtle(shape="turtle")
# tam.color("yellow")
# tam.penup()
# tam.goto(x=-230, y=-120)

# # tems
# tems = Turtle(shape="turtle")
# tems.color("green")
# tems.penup()
# tems.goto(x=-230, y=-90)

# # tum
# tum = Turtle(shape="turtle")
# tum.color("blue")
# tum.penup()
# tum.goto(x=-230, y=-60)

# # tym
# tym = Turtle(shape="turtle")
# tym.color("blue")
# tym.penup()
# tym.goto(x=-230, y=-30)
all_turtles = []

y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            sys.exit
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
    