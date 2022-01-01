# TODO
# Create the screen
# Create and move a paddle
# Create another paddle
# Create the ball and make it move
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses
# Keep score
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

PLAYER_POST = (380, 0)
ENEMY_POST = (-380, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.tracer(0)
screen.listen()

r_paddle = Paddle(PLAYER_POST)
l_paddle = Paddle(ENEMY_POST)
ball = Ball()
l_score = Scoreboard((200, 260), "left")
r_score = Scoreboard((-220, -270), "right")

# controls
screen.onkey(key="w", fun=r_paddle.move_up)
screen.onkey(key="s", fun=r_paddle.move_down)

screen.onkey(key="p", fun=l_paddle.move_up)
screen.onkey(key=";", fun=l_paddle.move_down)
game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(.1)

    ball.move()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 45 and ball.xcor() > 320 or ball.distance(l_paddle) < 45 and ball.xcor() < -320:
        print("You hit")
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        r_score.add_score((-220, -270), "right")

    if ball.xcor() < -380:
        ball.reset_position()
        l_score.add_score((200, 260), "left")

screen.exitonclick()
