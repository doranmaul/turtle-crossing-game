import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

screen.listen()
cars = CarManager()
player = Player()
score = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.car_move()
    cars.add_cars()

    # Detect player crossing successfully

    if player.reset_player():
        score.update_score()
        cars.update_speed()

    # Detect player collision with car

    for all_cars in cars.car_list:
        if player.distance(all_cars) < 20:
            game_is_on = False
            score.game_over()











screen.exitonclick()

