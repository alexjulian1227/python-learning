import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()
player = Player()
car = CarManager()
screen.listen()
screen.onkey(key="w", fun=player.move)

game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    player.next_level()
    score.player_score.clear()
    for car_group in car.all_cars:

        if player.distance(car_group) < 20:
            game_is_on = False
            score.hit_car()

screen.exitonclick()
