from turtle import Turtle

PLAYER_POST = (370, 0)
ENEMY_POST = (-370, 0)
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.color("white")
        self.pu()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        new_x = self.xcor()
        self.goto(new_x, new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        new_x = self.xcor()
        self.goto(new_x, new_y)
