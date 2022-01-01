from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
snake = Snake()


food = Food()
screen.onkey(key="w", fun=snake.move_up)
screen.onkey(key="s", fun=snake.move_down)
screen.onkey(key="a", fun=snake.move_left)
screen.onkey(key="d", fun=snake.move_right)

# TODO Add scoreboard
score = Scoreboard()
game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(.1)

    snake.move()
    # TODO Detect the collision between snake and food
    if snake.head.distance(food) < 15:
        food.relocate()
        snake.extend()
        score.update_score()

    #Detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.hit_wall()

    # Detect collision with tail
    # you can use slicing
    # piano_keys = ["a","b","c","d","e","f","g"]
    # piano_keys[2:5]
    # = "c","d","e"
    # piano_keys[2:5:2]
    # = "c","e" /it skip one at the other
    # piano_keys[2:]
    # = "c","d","e,","f","g"
    # piano_keys[:5]
    # = "a", "b", "c", "d", "e"
    # piano_keys[::2]
    # = "a", "c", "e", "f"
    for segment in snake.snake[1:]:  # using slicing
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.hit_wall()


screen.exitonclick()
