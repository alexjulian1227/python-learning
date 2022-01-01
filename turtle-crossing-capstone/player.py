from turtle import Turtle

import scoreboard
from scoreboard import *

import car_manager
from car_manager import *
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 30
FINISH_LINE_Y = 280

score = Scoreboard()


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.pu()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def next_level(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT
            score.player_score.clear()
            score.update_score()

