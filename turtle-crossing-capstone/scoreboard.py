from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:

    def __init__(self):
        self.player_score = Turtle()
        self.player_score.hideturtle()
        self.player_score.color("black")
        self.player_score.pu()
        self.player_score.goto(-280, -280)
        self.score = 1
        self.player_score.write(f"Level: {self.score} ", font=FONT)

    def update_score(self):
        self.player_score.clear()
        self.score += 1
        self.player_score.write(f"Level: {self.score} ", font=FONT)

    def hit_car(self):
        self.player_score.goto(-150, 0)
        self.player_score.write("Your hit by a car!", font=FONT)
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact G
