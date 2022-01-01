from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, position, alignment):
        super().__init__()

        self.color("white")
        self.pu()
        self.score = 0
        self.goto(position)
        self.write(f"Score:  {self.score}", align=alignment, font=FONT)
        self.hideturtle()

    def add_score(self, position, alignment):
        self.score += 1
        self.clear()
        self.goto(position)
        self.write(f"Score:  {self.score}", align=alignment, font=FONT)
