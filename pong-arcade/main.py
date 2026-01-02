from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
# Setup our game screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Setup both paddles
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

# Move paddles: Left uses up and down arrow keys, Right uses 'w' and 's' keys.
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

# Setup Ball
ball = Ball()

# Setup Scoreboard
scoreboard = ScoreBoard()


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collisions with wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()
    # Detect collision with wall

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect if Right paddles misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    # Detect if Left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()