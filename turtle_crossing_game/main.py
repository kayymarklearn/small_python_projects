import time
from turtle import Screen
from player import Player
from car_manager import CarManager, MOVE_INCREMENT
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = []

screen.listen()
screen.onkey(player.move, "Up")
speed_of_car = 0
gen_car = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    gen_car += 1

    # Create a new car for each sixth iteration of the while loop
    if gen_car == 0 or gen_car % 6 == 0:
        car = CarManager(speed_of_car)
        cars.append(car)


    for car in cars:
        car.car_move()
        
        # Detect when car collides with a player
        for car in cars:
            if car.distance(player) < 20:
                scoreboard.game_over()
                game_is_on = False


    # Check player collision with finish line
    if player.check_collisions():
        scoreboard.level += 1
        speed_of_car += 10
        scoreboard.update_board()

screen.exitonclick()