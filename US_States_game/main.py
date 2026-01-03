import turtle
import pandas
import time
from states import State
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.tracer(0)

scoreboard = Scoreboard()
game_on = True

named_states = []

state_names = pandas.read_csv("50_states.csv")

state_list = state_names.state.to_list()

while game_on:
    time.sleep(0.1)
    screen.update()
    answer_state = screen.textinput(title=f"{scoreboard.score}/50 States Correct", prompt="What's another state name?").lower()
    for state in state_list:
        if state.lower() == answer_state:
                if answer_state not in named_states:
                    x = (state_names[state_names.state == f"{state}"]).x
                    y = (state_names[state_names.state == f"{state}"]).y
                    new_state = State(name=answer_state, x=int(x), y=int(y))
                    named_states.append(answer_state)
                    scoreboard.update()
                    if scoreboard.score >= 50:
                        scoreboard.game_over()
                        game_on = False

screen.exitonclick()
