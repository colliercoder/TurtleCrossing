import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move_cars()
    all_cars = car_manager.all_cars
    for car in car_manager.all_cars:
        if player.distance(car)<25:

           game_is_on = False
           scoreboard.game_over()

    if player.is_at_finishline():
        scoreboard.point()
        player.reset_player()
        car_manager.increase_speed()
screen.exitonclick()

